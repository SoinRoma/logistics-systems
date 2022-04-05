$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        loop: true,
        responsive: {
            0: {
                items: 1
            },
            490: {
                items: 2
            },
            670: {
                items: 4
            },
            990: {
                items: 3
            },
            1300: {
                items: 4
            }
        }
    });
});
