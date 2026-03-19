document.addEventListener('DOMContentLoaded', function () {

    var currentPath = window.location.pathname;
    document.querySelectorAll('.navbar .nav-link').forEach(function (link) {
        if (link.getAttribute('href') === currentPath || (currentPath !== '/' && link.getAttribute('href') !== '/' && currentPath.startsWith(link.getAttribute('href')))) {
            link.classList.add('active');
        }
    });

    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            var bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 5000);
    });

    var amountInput = document.getElementById('id_amount');
    if (amountInput) {
        amountInput.addEventListener('input', function () {
            document.querySelectorAll('.amount-btn').forEach(function (btn) {
                btn.classList.remove('btn-danger', 'text-white');
                btn.classList.add('btn-outline-danger');
            });
        });
    }

    document.querySelectorAll('.gallery-card img').forEach(function (img) {
        img.style.cursor = 'zoom-in';
    });

    var revealTargets = document.querySelectorAll('.card, .page-hero .container > *, .table-responsive');
    revealTargets.forEach(function (el) {
        el.classList.add('reveal-item');
    });

    if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.08 });

        revealTargets.forEach(function (el) {
            observer.observe(el);
        });
    } else {
        revealTargets.forEach(function (el) {
            el.classList.add('is-visible');
        });
    }
});
