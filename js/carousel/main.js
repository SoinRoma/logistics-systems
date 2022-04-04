$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        loop: true,
        responsive: {
            0: {
                items: 1
            },
            640: {
                items: 2
            },
            795: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    });
});
