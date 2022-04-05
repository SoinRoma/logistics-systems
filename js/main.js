const items = document.querySelectorAll(".accordion button");

// Аккордион - FAQ
function toggleAccordion() {
    const itemToggle = this.getAttribute('aria-expanded');

    for (i = 0; i < items.length; i++) {
        items[i].setAttribute('aria-expanded', 'false');
    }

    if (itemToggle === 'false') {
        this.setAttribute('aria-expanded', 'true');
    }
}

items.forEach(item => item.addEventListener('click', toggleAccordion));

// Якорные ссылки
$("#menu-header").on("click", "a", function (event) {
    event.preventDefault();
    let id = $(this).attr('href');
    let top = $(id).offset().top - 100;
    $('body,html').animate({scrollTop: top}, 1000);
});

$("#menu-right-header").on("click", "a", function (event) {
    event.preventDefault();
    let id = $(this).attr('href');
    let top = $(id).offset().top - 100;
    $('body,html').animate({scrollTop: top}, 1000);
});


// Инициализация для модальных окон
$(document).ready(function () {
    $('.requestModal').magnificPopup({
        removalDelay: 500,
        callbacks: {
            beforeOpen: function () {
                this.st.mainClass = this.st.el.attr('data-effect');
            }
        },
        midClick: true
    });

    $(".closeBtn").click(function () {
        $.magnificPopup.close();
    });
});
