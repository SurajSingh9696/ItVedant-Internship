import json
import hmac
import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Donation
from .forms import DonationForm


def donate_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.status = 'pending'
            donation.save()
            if settings.RAZORPAY_KEY_ID:
                try:
                    import razorpay
                    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
                    order_amount = int(donation.amount * 100)
                    rz_order = client.order.create({'amount': order_amount, 'currency': 'INR', 'payment_capture': 1})
                    donation.razorpay_order_id = rz_order['id']
                    donation.save()
                    context = {
                        'donation': donation,
                        'razorpay_key': settings.RAZORPAY_KEY_ID,
                        'razorpay_order_id': rz_order['id'],
                        'amount': order_amount,
                    }
                    return render(request, 'donations/payment.html', context)
                except Exception:
                    pass
            donation.status = 'completed'
            donation.save()
            return redirect('donation_success', pk=donation.pk)
    else:
        form = DonationForm()
    return render(request, 'donations/donate.html', {'form': form, 'razorpay_key': settings.RAZORPAY_KEY_ID})


@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        razorpay_order_id = data.get('razorpay_order_id', '')
        razorpay_payment_id = data.get('razorpay_payment_id', '')
        razorpay_signature = data.get('razorpay_signature', '')
        key_secret = settings.RAZORPAY_KEY_SECRET.encode()
        generated_signature = hmac.new(
            key_secret,
            f'{razorpay_order_id}|{razorpay_payment_id}'.encode(),
            hashlib.sha256
        ).hexdigest()
        if generated_signature == razorpay_signature:
            donation = Donation.objects.get(razorpay_order_id=razorpay_order_id)
            donation.razorpay_payment_id = razorpay_payment_id
            donation.status = 'completed'
            donation.save()
            return JsonResponse({'status': 'success', 'pk': donation.pk})
        return JsonResponse({'status': 'failed'}, status=400)
    return JsonResponse({'status': 'invalid'}, status=400)


def donation_success(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    return render(request, 'donations/success.html', {'donation': donation})

