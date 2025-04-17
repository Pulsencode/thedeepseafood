$(document).ready(function () {
  // pre-loader script 
    $(".pre_loader").fadeOut("slow");
  
  // active link 
    for (var i = 0; i < document.links.length; i++) {
     if (document.links[i].href == document.URL) {
   $(document.links[i]).addClass('active');
   }}
 
 });

// mobile_device
$(document).ready(function () {
  if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    $('body').addClass("mobile_device");
  }
});

// sidebar
$(document).ready(function() {
  // Toggle sidebar
  $('#mainSidebarToggle').click(function(e) {
    e.preventDefault();
    $('.main-sidebar, .sidebar-overlay').addClass('active');
  });

  // Close sidebar
  $('#mainSidebarClose, .sidebar-overlay').click(function(e) {
    e.preventDefault();
    $('.main-sidebar, .sidebar-overlay').removeClass('active');
  });

  // Close on ESC key
  $(document).keyup(function(e) {
    if (e.keyCode === 27) {
      $('.main-sidebar, .sidebar-overlay').removeClass('active');
    }
  });
});

// date_pick  
$(document).ready(function () {
  $(".date_pick").datepicker({
    // changeMonth: true,
    changeYear: true,
    yearRange: '1950:' + (new Date().getFullYear() + 2).toString()
  });
  $(".today_date").datepicker().datepicker("setDate", new Date());
});

// slick slider --home brands
$(".slick-slidera").slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  dots: false,
  arrows: true,
  autoplay: true,
  autoplaySpeed: 3000,
  pauseOnFocus: false,
  pauseOnHover: true,
  pauseOnDotsHover: false,
  responsive: [
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 3,
      },
    },
    {
      breakpoint: 767,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 575,
      settings: {
        slidesToShow: 2,
      },
    },
  ],
});

gsap.utils.toArray(".animate_count").forEach((element) => {
  let clean = (v) => (v + "").replace(/[^\d\.-]/gi, ""), // get rid of anything except numbers and periods
    num = clean(element.getAttribute("data-number")),
    decimals = (num.split(".")[1] || "").length,
    proxy = { val: parseFloat(clean(element.innerText)) || 0 };
  gsap.to(proxy, {
    val: +num,
    duration: 2,
    scrollTrigger: {
      trigger: element,
      toggleActions: "restart none none none",
    },
    onUpdate: () => (element.innerText = formatNumber(proxy.val, decimals)),
  });
});

function formatNumber(value, decimals) {
  let s = (+value).toLocaleString("en-US").split(".");
  return decimals
    ? s[0] + "." + ((s[1] || "") + "00000000").substr(0, decimals)
    : s[0];
}

function get_product_list(src) {
  var category = $(src).data("id");
  var dom = "http" + "://" + "thedeepseafood.com";
  if (category == "all") {
    $(".ALLCAT").addClass("active");
    $(".CATSELE").removeClass("active");
  } else {
    $(".ALLCAT").removeClass("active");
    $(".CATSELE").removeClass("active");

    $("#CAT" + category).addClass("active");
  }
  $(".APPENDPRO").empty();
  $.ajax({
    url: "/get-products/",
    type: "GET",
    data: {
      category: category,
    },
    success: function (data) {
      var ret = data["products"];

      $.each(ret, function (key, values) {
        ids = values["id"];
        $(".APPENDPRO").append(
          '<div class="col-lg-3 col-md-4 col-6 pt-20"><div class="item card-hover-up"><img width="" height="" alt="" class="img-primary" src=' + values["image"] + '><div class="info"><div class="title font-lntermedium">' +
            values["name"] +
            '</div><a class="btn btn-icon"><span>View Item</span><img width="" height="" alt="" src="/static/public/images/icons/right-arrow-blue.png"></a></div><a class="primary-btn" href="/product-view/?product=' + values["id"] + '"></a></div></div>'
        );
      });

      $(".APPENDPRO").append(
        '<div class="col-lg-3 col-md-4 col-6 pt-20"><div class="item card-hover-up more-card"><img width="" height="" alt="" class="img-primary" src="/static/public/images/index/products/new-card1.jpg"><div class="info bg-blue pt-4 pb-4"><a class="btn btn-icon text-center"><span class="title font-lntermedium text-white">VIEW MORE</span><i class="fa fa-angle-double-right fs-20 text-white" aria-hidden="true"></i></a></div><div class="more-card-overlay"></div><a class="primary-btn" href="/products/"></a></div></div>'
      );
    },
  });
}


// Init slick slider + animation
$('.slider').slick({
  autoplay: true,
  speed: 1500,
  lazyLoad: 'progressive',
  arrows: false,
  dots: false,
	loop:true,  
	pauseOnHover:false,
	prevArrow: '<div class="slick-nav prev-arrow"><i></i><svg><use xlink:href="#circle"></svg></div>',
	nextArrow: '<div class="slick-nav next-arrow"><i></i><svg><use xlink:href="#circle"></svg></div>',
}).slickAnimation();



$('.slick-nav').on('click touch', function(e) {

    e.preventDefault();

    let arrow = $(this);

    if(!arrow.hasClass('animate')) {
        arrow.addClass('animate');
        setTimeout(() => {
            arrow.removeClass('animate');
        }, 1600);
    }

});