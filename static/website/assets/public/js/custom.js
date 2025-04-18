//
$('.equal_heights').each(function () {
  var $columns = $('.equal_height', this);
  var maxHeight = Math.max.apply(Math, $columns.map(function () {
    return $(this).height();
  }).get());
  $columns.height(maxHeight);
});

// specific_scroll
$(window).scroll(function () {
  if ($(this).scrollTop() > 300) {
    $('body').addClass("specific_scroll");
  }
  else {
    $('body').removeClass("specific_scroll");
  }
});

// up down scroll
$(window).ready(function () {
  var previousScroll = 0;
  $(window).scroll(function () {
    var currentScroll = $(this).scrollTop();
    if (currentScroll > previousScroll) {
      $('body').removeClass("up_scroll");
    }
    else {
      $('body').addClass("up_scroll");
    }
    previousScroll = currentScroll;
  });
}());


// sidebar
$('.toggle_sidebar').on('click', function () {
  $('body').toggleClass('sidebar_open');
});

// enquiry
$('.toggle_enquiry').on('click', function () {
  $('body').toggleClass('enquiry_open');
});

// modal_show_file
$("body").on("click", ".show_file_btn", function (event) {
  $('#file_src').attr('src', $(this).data('file-src'));
  $('#modal_show_file').find('#file_src');
  $('#modal_show_file').modal('show');
});
$(".remove_src").click(function () {
  $('#file_src').replaceWith($('#file_src').clone().attr('src', ''));
});

// modal_show_file_2
$("body").on("click", ".show_file_btn_2", function (event) {
  $('#file_src_2').attr('src', $(this).data('file-src'));
  $('#modal_show_file_2').find('#file_src_2');
  $('#modal_show_file_2').modal('show');
});
$(".remove_src_2").click(function () {
  $('#file_src_2').replaceWith($('#file_src_2').clone().attr('src', ''));
});

// WOW
$(document).ready(function(){
  new WOW().init();     
}); 
function addWowDelay() { 
  $('.wow_item').each(function(i) { d = i * .2 ; $(this).attr('data-wow-delay', d + "ms");
   }); 
} addWowDelay();

//
$(function () {
  $(".expand-btns .button").click(function () {
    $this = $(this);
    // Do something for the button.
    //console.log("You have clicked me. So wait for 3 seconds.");
    // After doing something, disable.
    $this.toggleClass("btn_enable");
    
    setTimeout(function () {
      //console.log("Now you can click me again.");
      $this.toggleClass("btn_enable");
    }, 2000);
  });
});

// load_more_item
$(document).ready(function() {
  var pagelength = 4;
  var pageIndex = 10;
  //hide all tr greater than page length
  var selector = ".load_more_item tbody tr:gt(" + pagelength + ")";
  $(selector).hide();
  
  $(".btn_load").click(function(){
    $(this).hide();
  	var itemsCount = ((pageIndex * pagelength) + pagelength);   
  	var selector = ".load_more_item tbody tr:lt(" + itemsCount + ")";
  	$(selector).show();
    pageIndex++;
  });
});

// country_tab
$(document).ready(() => {
  let url = location.href.replace(/\/$/, "");
  if (location.hash) {
    const hash = url.split("#");
    $('.country_tab button[data-bs-target="#'+hash[1]+'"]').tab("show");
    url = location.href.replace(/\/#/, "#");
    history.replaceState(null, null, url);
    setTimeout(() => {
      $(window).scrollTop(0);
    }, 400);
  } 
  
});

// country_tab
$('.country_tab button').click(function() {  
  var $selector = $('.country_tab button[data-bs-target="' + $(this).attr("data-bs-target") + '"]').not(this);
  var nav = $selector.closest('.country_tab');
  nav.find('button').removeClass("active");
  $selector.addClass("active");
  $('html, body').animate({
    scrollTop: $("#our_branches").offset().top
});

});
$(".footer-country button").click(function() {
  $('html, body').animate({
      scrollTop: $("#our_branches").offset().top
  });
});