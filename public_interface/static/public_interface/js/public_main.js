//news filter in details page

$(document).ready(function () {
  $("#myInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".news-item p").filter(function () {
      $(this)
        .parent()
        .parent()
        .toggle($(this).text().toLowerCase().startsWith(value));
    });
  });
});

//filter in blog page

$(document).ready(function () {
  $("#myInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".blog-items").each(function () {
      var titleText = $(this).find("p").text().toLowerCase();
      var isVisible = titleText.startsWith(value);
      $(this).toggle(isVisible);
    });
  });
});

//promotion filter in details page

$(document).ready(function () {
  $("#myInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".promotion-item p").filter(function () {
      $(this)
        .parent()
        .parent()
        .toggle($(this).text().toLowerCase().startsWith(value));
    });
  });
});

//career filter

function filtercareer() {
  // Get values from the form
  var selectedJobTitle = $("#jobTitleSelect").val();
  var selectedJobType = $("#jobTypeSelect").val();
  var location = $('select[name="location"]').val().toLowerCase().trim();

  $("#searchResults .software-eng").each(function () {
    var jobTitle = $(this).find("h3.ctitle").text();
    var jobType = $(this)
      .find("p.ctype")
      .map(function () {
        return $(this).text();
      })
      .get();

    var jobLocation = $(this).find("p.loc").text().trim().toLowerCase();

    // Check if the current job matches the selected filters
    var titleMatches =
      selectedJobTitle === "" ||
      jobTitle.toLowerCase().trim() === selectedJobTitle.toLowerCase().trim();
    var typeMatches =
      selectedJobType === "" || jobType.indexOf(selectedJobType) !== -1;

    var locationMatches = location === "" || jobLocation.includes(location);

    // Show or hide the job result based on the filter conditions
    if (titleMatches && typeMatches && locationMatches) {
      $(this).show();
    } else {
      $(this).hide();
    }
  });
}

//career model for getting job title
function show_modal(title) {
  $("#applied").val(title);
  $("#career_modal").modal("show");
}

function loadProductContent(element) {
  var type = $(element).data("name");
  $("#loadMoreButton").hide();
  $.ajax({
    type: "GET",
    url: "/get_product_content/",
    data: { type: type }, // Use 'category_id' here

    success: function (data) {
      if (data.status) {
        $("#MixItUp").html(data.template);
        $(".nav-item a").removeClass("active");
        $(element).addClass("active");
        if (data.total_count > 4) {
          $("#loadMoreButton").show();
        } else {
          $("#loadMoreButton").hide();
        }
      } else {
        $("#MixItUp").html(data.template);
        // Handle errors or display a message
        console.error("Error loading product content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading product content:", status, error);
    },
  });
}

//load more products

function loadmoreproduct(buttonElement) {
  var _currentProducts = $("#MixItUp").children(".mix").length;
  var _limit = $(buttonElement).data("limit");
  var _total = $(buttonElement).data("total");
  var type = $("#prod").find(".btn.active").data("name");

  $.ajax({
    url: "/load_more_product/",
    data: {
      limit: _limit,
      offset: _currentProducts,
      type: type,
    },
    dataType: "json",
    beforeSend: function () {
      $("#loadMoreButton").attr("disabled", true);
    },
    success: function (res) {
      $("#MixItUp").append(res.data);
      $("#loadMoreButton").attr("disabled", false);

      var _totalshowing = $("#MixItUp").children(".mix").length;

      if (_totalshowing == res.total_count) {
        $("#loadMoreButton").hide();
      }
    },
  });
}

//brand page product detail modal
function show_details(id) {
  $("#view_modal").modal("show");
  $.ajax({
    type: "GET",
    url: "/get_product_details/",
    data: { id: id },

    success: function (data) {
      if (data.status) {
        $("#pdetails").html(data.template);
      } else {
        $("#pdetails").html(data.template);
        // Handle errors or display a message
        console.error("Error loading product content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading product content:", status, error);
    },
  });
}

function loadpmodaldata(element) {
  $("a.category-link").removeClass("active");
  $(element).addClass("active");

  var cid = $(element).data("category-id");
  var id = $("#pid").val();

  $.ajax({
    type: "GET",
    url: "/get_modal_product_details/",
    data: {
      cid: cid,
      id: id,
    },

    success: function (data) {
      if (data.status) {
        $("#modalpdata").html(data.template);
      } else {
        $("#modalpdata").html(data.template);
        // Handle errors or display a message
        console.error("Error loading product content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading product content:", status, error);
    },
  });
}

//fetching products for index

function get_product_list(value, element) {
  $("a.nav-link").removeClass("active");
  $(element).addClass("active");
  var ptype = value;
  $.ajax({
    type: "GET",
    url: "/get_product_index/",
    data: { ptype: ptype },

    success: function (data) {
      if (data.status) {
        $("#index_product").html(data.template);
      } else {
        $("#index_product").html(data.template);
        // Handle errors or display a message
        console.error("Error loading product content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading product content:", status, error);
    },
  });
}

//fetching products for product page

function getprodu(value, element) {
  $("a.nav-link").removeClass("active");
  $(element).addClass("active");

  var ptype = value;
  $("#prodtype").val(value);
  $.ajax({
    type: "GET",
    url: "/get_product_lists/",
    data: { ptype: ptype },

    success: function (data) {
      if (data.status) {
        $("#prodlist").html(data.template);
      } else {
        $("#prodlist").html(data.template);
        // Handle errors or display a message
        console.error("Error loading product content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading product content:", status, error);
    },
  });
}

//switch product category in product detail page

function switchprodcategory(element) {
  $("a.category-link").removeClass("active");
  $(element).addClass("active");

  var cid = $(element).data("category-id");
  var pid = $(element).data("pid");

  $.ajax({
    type: "GET",
    url: "/product_details_switch/",
    data: {
      cid: cid,
      pid: pid,
    },

    success: function (data) {
      if (data.status) {
        $("#prod").html(data.template);
      } else {
        $("#prod").html(data.template);
        // Handle errors or display a message
        console.error("Error loading product content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading product content:", status, error);
    },
  });
}

//news room page scripts
document.addEventListener("DOMContentLoaded", function () {
  document
    .querySelector('.exhibition a[href="#events"]')
    .addEventListener("click", function (e) {
      e.preventDefault();
      getEvents();
    });

  document
    .querySelector('.company a[href="#company-news"]')
    .addEventListener("click", function (e) {
      e.preventDefault();
      getNews();
    });

  document
    .querySelector('.global a[href="#global-news"]')
    .addEventListener("click", function (e) {
      e.preventDefault();
      getGlobalNews();
    });
});

function getEvents() {
  $(".company a").removeClass("active");
  $(".global a").removeClass("active");
  $('.exhibition a[href="#events"]').addClass("active");
  $.ajax({
    type: "GET",
    url: "/get_events/",
    data: {},

    success: function (data) {
      if (data.status) {
        $("#newsroom-data").empty();
        $("#newsroom-data").html(data.template);
      } else {
        $("#newsroom-data").html(data.template);
        // Handle errors or display a message
        console.error("Error loading content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading  content:", status, error);
    },
  });
}

function getNews() {
  $(".global a").removeClass("active");
  $(".exhibition a").removeClass("active");
  $('.company a[href="#company-news"]').addClass("active");
  $.ajax({
    type: "GET",
    url: "/get_news/",
    data: {},

    success: function (data) {
      if (data.status) {
        $("#newsroom-data").empty();
        $("#newsroom-data").html(data.template);
        if (data.total_news < 3) {
          $("#loadMore").hide();
        } else {
          $("#loadMore").show();
        }
      } else {
        $("#newsroom-data").html(data.template);
        // Handle errors or display a message
        console.error("Error loading content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading  content:", status, error);
    },
  });
}
function getGlobalNews() {
  $(".company a").removeClass("active");
  $(".exhibition a").removeClass("active");
  $('.global a[href="#global-news"]').addClass("active");
  $.ajax({
    type: "GET",
    url: "/get_global_news/",
    data: {},

    success: function (data) {
      if (data.status) {
        $("#newsroom-data").empty();
        $("#newsroom-data").html(data.template);
        if (data.total_news < 3) {
          $("#loadMore").hide();
        } else {
          $("#loadMore").show();
        }
      } else {
        $("#newsroom-data").html(data.template);
        // Handle errors or display a message
        console.error("Error loading content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading  content:", status, error);
    },
  });
}

function getPromotions() {
  $.ajax({
    type: "GET",
    url: "/get_promotions/",
    data: {},

    success: function (data) {
      if (data.status) {
        $("#newsroom-data").empty();
        $("#newsroom-data").html(data.template);
      } else {
        $("#newsroom-data").html(data.template);
        // Handle errors or display a message
        console.error("Error loading content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading  content:", status, error);
    },
  });
}

//loadmore news

function loadmore(element) {
  var _currentnews = $("#newsroom-data").children(".news-box").length;
  var _limit = $(element).data("limit");
  var _total = $(element).data("total");
  var _type = $(element).data("type");
  $("#loadMore").remove();

  $.ajax({
    url: "/load_more_news/",
    data: {
      limit: _limit,
      offset: _currentnews,
      type: _type,
    },
    dataType: "json",
    beforeSend: function () {
      $("#loadMore").attr("disabled", true);
    },
    success: function (res) {
      $("#newsroom-data").append(res.data);
      $("#loadMore").attr("disabled", false);

      var _totalshowing = $("#newsroom-data").children(".news-box").length;
      if (_totalshowing == _total) {
        $("#loadMore").remove();
      }
    },
  });
}

//loadmore events

function loadmoreEvents(element) {
  var _currentnews = $("#newsroom-data").children(".news-box").length;
  var _limit = $(element).data("limit");
  var _total = $(element).data("total");
  // var _type = $(element).data('type');
  $("#loadMore").remove();

  $.ajax({
    url: "/load_more_events/",
    data: {
      limit: _limit,
      offset: _currentnews,
      // type:_type
    },
    dataType: "json",
    beforeSend: function () {
      $("#loadMore").attr("disabled", true);
    },
    success: function (res) {
      $("#newsroom-data").append(res.data);
      $("#loadMore").attr("disabled", false);

      var _totalshowing = $("#newsroom-data").children(".news-box").length;
      if (_totalshowing == _total) {
        $("#loadMore").remove();
      }
    },
  });
}

//product search

function searchproduct() {
  var input = $("#inputvalue").val();
  var type = $("#prodtype").val();
  $.ajax({
    type: "GET",
    url: "/search_product/",
    data: {
      input: input,
      type: type,
    },

    success: function (data) {
      if (data.status) {
        $("#prodlist").html(data.template);
      } else {
        $("#prodlist").html(data.template);
        // Handle errors or display a message
        console.error("Error loading product content.");
      }
    },
    error: function (xhr, status, error) {
      // Handle errors or display a message
      console.error("Error loading product content:", status, error);
    },
  });
}

function readmore(counter) {
  $("#desc" + counter).toggleClass("line_2");
  if ($("#desc" + counter).hasClass("line_2")) {
    $("#readmore-btn" + counter).html("Read More");
  } else {
    $("#readmore-btn" + counter).html("Read Less");
  }
}

// function readless(counter) {

// $('#fullDesc' + counter).hide();
// $('#desc' + counter).show();
// }

//email validation error clearing and showing
function clearerrors() {
  errors = document.getElementsByClassName("formerror");
  for (let item of errors) {
    item.innerHTML = "";
  }
}

function seterror(id, error) {
  Element = document.getElementById(id);
  Element.getElementsByClassName("formerror")[0].innerHTML = error;
}

//restricting submit button

document
  .getElementById("contactform")
  .addEventListener("submit", function (event) {
    // Clear errors before validation
    clearerrors();

    var email = document.forms["contactform"]["email"].value;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Validate email
    if (!email.match(emailRegex)) {
      seterror("email", "Enter a valid email address");
      event.preventDefault(); // Prevent form submission if validation fails
    } else {
      // Additional functions to be executed if email validation is successful

      // Disable the submit button when the form is submitted
      document.getElementById("submitButton").disabled = true;

      // Reset the form and enable the submit button after 3 seconds
      setTimeout(function () {
        document.getElementById("contactform").reset();
        document.getElementById("submitButton").disabled = false;
      }, 3000);
    }
  });

//restrict document upload in career section
function fileupload() {
  var fileName = $('input[name="attachment"]').val();
  if (fileName !== "") {
    if (!isAllowedExtension(fileName)) {
      alert("Only document formats (doc, docx, pdf, txt) are allowed.");
      $('input[name="attachment"]').val(""); // Clear the file input
    }
  }
}

// Function to check if the file extension is allowed
function isAllowedExtension(fileName) {
  var allowedExtensions = ["doc", "docx", "pdf", "txt"];
  var fileExtension = fileName.split(".").pop().toLowerCase();
  return allowedExtensions.includes(fileExtension);
}

//
$(".equal_heights").each(function () {
  var $columns = $(".equal_height", this);
  var maxHeight = Math.max.apply(
    Math,
    $columns
      .map(function () {
        return $(this).height();
      })
      .get()
  );
  $columns.height(maxHeight);
});

// specific_scroll
$(window).scroll(function () {
  if ($(this).scrollTop() > 300) {
    $("body").addClass("specific_scroll");
  } else {
    $("body").removeClass("specific_scroll");
  }
});

// up down scroll
$(window).ready(
  (function () {
    var previousScroll = 0;
    $(window).scroll(function () {
      var currentScroll = $(this).scrollTop();
      if (currentScroll > previousScroll) {
        $("body").removeClass("up_scroll");
      } else {
        $("body").addClass("up_scroll");
      }
      previousScroll = currentScroll;
    });
  })()
);

// sidebar
$(".toggle_sidebar").on("click", function () {
  $("body").toggleClass("sidebar_open");
});

// enquiry
$(".toggle_enquiry").on("click", function () {
  $("body").toggleClass("enquiry_open");
});

// modal_show_file
$("body").on("click", ".show_file_btn", function (event) {
  $("#file_src").attr("src", $(this).data("file-src"));
  $("#modal_show_file").find("#file_src");
  $("#modal_show_file").modal("show");
});
$(".remove_src").click(function () {
  $("#file_src").replaceWith($("#file_src").clone().attr("src", ""));
});

// modal_show_file_2
$("body").on("click", ".show_file_btn_2", function (event) {
  $("#file_src_2").attr("src", $(this).data("file-src"));
  $("#modal_show_file_2").find("#file_src_2");
  $("#modal_show_file_2").modal("show");
});
$(".remove_src_2").click(function () {
  $("#file_src_2").replaceWith($("#file_src_2").clone().attr("src", ""));
});

// WOW
$(document).ready(function () {
  new WOW().init();
});
function addWowDelay() {
  $(".wow_item").each(function (i) {
    d = i * 0.2;
    $(this).attr("data-wow-delay", d + "ms");
  });
}
addWowDelay();

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
$(document).ready(function () {
  var pagelength = 4;
  var pageIndex = 10;
  //hide all tr greater than page length
  var selector = ".load_more_item tbody tr:gt(" + pagelength + ")";
  $(selector).hide();

  $(".btn_load").click(function () {
    $(this).hide();
    var itemsCount = pageIndex * pagelength + pagelength;
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
    $('.country_tab button[data-bs-target="#' + hash[1] + '"]').tab("show");
    url = location.href.replace(/\/#/, "#");
    history.replaceState(null, null, url);
    setTimeout(() => {
      $(window).scrollTop(0);
    }, 400);
  }
});

// country_tab
$(".country_tab button").click(function () {
  var $selector = $(
    '.country_tab button[data-bs-target="' +
      $(this).attr("data-bs-target") +
      '"]'
  ).not(this);
  var nav = $selector.closest(".country_tab");
  nav.find("button").removeClass("active");
  $selector.addClass("active");
  $("html, body").animate({
    scrollTop: $("#our_branches").offset().top,
  });
});
$(".footer-country button").click(function () {
  $("html, body").animate({
    scrollTop: $("#our_branches").offset().top,
  });
});
