
// slick_slider_4
$('.slick_slider_4').slick({
  infinite: false,
  slidesToShow: 4,
  slidesToScroll: 1,
  dots: false,
  arrows: false,
  responsive: [
    {
      breakpoint: 1199,
      settings: {
       slidesToShow: 3,
      },
    },
   {
    breakpoint: 991,
    settings: {
     slidesToShow: 2,
    },
  },
  {
    breakpoint: 767,
    settings: {
     slidesToShow: 1,
    },
  },
 ],
});