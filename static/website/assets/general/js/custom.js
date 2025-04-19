$(document).ready(function () {
  // pre-loader script
  $(".pre_loader").fadeOut("slow");

  // active link
  for (var i = 0; i < document.links.length; i++) {
    if (document.links[i].href == document.URL) {
      $(document.links[i]).addClass("active");
    }
  }
});

// mobile_device
$(document).ready(function () {
  if (
    /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
      navigator.userAgent
    )
  ) {
    $("body").addClass("mobile_device");
  }
});

// date_pick
$(document).ready(function () {
  $(".date_pick").datepicker({
    // changeMonth: true,
    changeYear: true,
    yearRange: "1950:" + (new Date().getFullYear() + 2).toString(),
  });
  $(".today_date").datepicker().datepicker("setDate", new Date());
});

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
          '<div class="col-lg-3 col-md-4 col-6 pt-20"><div class="item card-hover-up"><img width="" height="" alt="" class="img-primary" src=' +
            values["image"] +
            '><div class="info"><div class="title font-lntermedium">' +
            values["name"] +
            '</div><a class="btn btn-icon"><span>View Item</span><img width="" height="" alt="" src="/static/public/images/icons/right-arrow-blue.png"></a></div><a class="primary-btn" href="/product-view/?product=' +
            values["id"] +
            '"></a></div></div>'
        );
      });

      $(".APPENDPRO").append(
        '<div class="col-lg-3 col-md-4 col-6 pt-20"><div class="item card-hover-up more-card"><img width="" height="" alt="" class="img-primary" src="/static/public/images/index/products/new-card1.jpg"><div class="info bg-blue pt-4 pb-4"><a class="btn btn-icon text-center"><span class="title font-lntermedium text-white">VIEW MORE</span><i class="fa fa-angle-double-right fs-20 text-white" aria-hidden="true"></i></a></div><div class="more-card-overlay"></div><a class="primary-btn" href="/products/"></a></div></div>'
      );
    },
  });
}
