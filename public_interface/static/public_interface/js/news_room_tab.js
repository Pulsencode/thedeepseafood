document.addEventListener("DOMContentLoaded", function () {
  // Initialize first slider
  initSliders();

  // Set up tab click handlers
  document.querySelector(".list_side").addEventListener("click", function (e) {
    const target = e.target.closest("a");
    if (!target) return;
    e.preventDefault();
    loadSection(target.hash);
  });

  // Handle initial page load
  const initialHash = window.location.hash || "#events";
  if (!window.location.hash) {
    window.history.replaceState(null, "", "#events");
  }
  loadSection(initialHash);
});

// AJAX-load a section based on its hash (#events, #company-news, #global-news)
function loadSection(hash) {
  const endpointMap = {
    "#events": "/get_events/",
    "#company-news": "/get_news/",
    "#global-news": "/get_global_news/",
  };

  $.ajax({
    url: endpointMap[hash],
    method: "GET",
    success: function (data) {
      if (data.status) {
        // Tear down existing sliders
        $(".slick_slider_1").slick("unslick");
        // Inject new content
        $("#newsroom-data").html(data.template);
        // Re-init sliders
        initSliders();
        // Sync URL & active tab
        updateHistory(hash);
        updateActiveTab(hash);
      }
    },
    error: function (xhr, status, error) {
      console.error("Error loading content:", error);
    },
  });
}

// Load-more handler integrated with spinner & error message
function loadmore(element) {
  var $button = $(element);
  var $container = $button.closest(".load-more-container");
  var $spinner = $container.find(".loading-indicator");
  var $linkHolder = $container.find(".load-more-content");
  var $errorMsg = $container.find(".error-message");

  var currentCount = $("#newsroom-data").children(
    ".news-box, .event-box"
  ).length;
  var limit = +$button.data("limit");
  var total = +$button.data("total");
  var type = $button.data("type"); // e.g. "company" or undefined

  console.log("Loading more:", { limit, total, type, currentCount });

  // Reset UI
  $errorMsg.addClass("d-none");
  $linkHolder.addClass("d-none");
  $spinner.removeClass("d-none");

  $.ajax({
    url: type ? "/load_more_news/" : "/load_more_events/",
    dataType: "json",
    data: {
      limit: limit,
      offset: currentCount,
      type: type || "",
    },
    success: function (res) {
      // Append new items
      $("#newsroom-data").append(res.data);
      // Re-init any new sliders
      initSliders();

      // Update counts
      var nowShowing = $("#newsroom-data").children(
        ".news-box, .event-box"
      ).length;
      console.log("Now showing:", nowShowing);

      // Clean up spinner & either remove or re-enable link
      $spinner.addClass("d-none");
      if (nowShowing >= total) {
        $container.remove();
      } else {
        $linkHolder.removeClass("d-none");
      }
    },
    error: function (xhr) {
      console.error("Load more failed:", xhr.responseText);

      // Hide spinner, show link & error
      $spinner.addClass("d-none");
      $linkHolder.removeClass("d-none");
      $errorMsg.removeClass("d-none");
    },
  });
}

function initSliders() {
  $(".slick_slider_1").not(".slick-initialized").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 3000,
    pauseOnFocus: false,
    pauseOnHover: false,
    pauseOnDotsHover: false,
  });
}

function updateActiveTab(hash) {
  $(".list_side a").removeClass("active");
  $(`.list_side a[href="${hash}"]`).addClass("active");
}

function updateHistory(hash) {
  if (window.location.hash !== hash) {
    window.history.pushState(null, "", hash);
  }
}

// Re-load content on browser back/forward
window.addEventListener("popstate", function () {
  loadSection(window.location.hash);
});
