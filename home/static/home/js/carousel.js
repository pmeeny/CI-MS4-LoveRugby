/**
 * [Rotate images in carousel
 * Credit:  https://getbootstrap.com/docs/5.0/components/carousel/ ]
 */
var myCarousel = document.querySelector('#home-carousel');
var carousel = new bootstrap.Carousel(myCarousel, {
    interval: 5000,
    wrap: true
});