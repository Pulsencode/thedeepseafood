document.addEventListener("DOMContentLoaded", function () {
  const tabs = document.querySelectorAll(".prod_tab_sc a");
  const contentContainer = document.getElementById("newsroom-data");
  let currentType = "events";
  let currentOffset = 0;
  const limit = 4;

  function initSliders() {
    $(".slick_slider_1").not(".slick-initialized").slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: true,
      arrows: false,
      autoplay: true,
      autoplaySpeed: 3000,
    });
  }

  async function loadContent(url) {
    try {
      contentContainer.innerHTML = '<div class="loading-spinner"></div>';

      const response = await fetch(url, {
        headers: { "X-Requested-With": "XMLHttpRequest" },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      if (data.error) {
        throw new Error(data.error);
      }

      contentContainer.innerHTML = data.template;

      if (url.includes("events")) {
        initSliders();
      }
    } catch (error) {
      console.error("Error:", error);
      contentContainer.innerHTML = `<div class="error">Error loading content: ${error.message}</div>`;
    }
  }

  async function handleLoadMore() {
    try {
      const loadMoreBtn = document.querySelector(".news-load-more");
      const type = loadMoreBtn.dataset.type;
      const limit = parseInt(loadMoreBtn.dataset.limit);
      const currentOffset = document.querySelectorAll(".news-box").length;

      const params = new URLSearchParams({
        offset: currentOffset,
        limit: limit,
        type: type,
      });

      const response = await fetch(`/load_more_news/?${params}`);
      const data = await response.json();

      if (data.error) throw new Error(data.error);

      // Append new items
      const tempDiv = document.createElement("div");
      tempDiv.innerHTML = data.data;
      document
        .getElementById("newsroom-data")
        .querySelector(".row")
        .appendChild(tempDiv);

      // Update load more button
      if (!data.has_more) {
        loadMoreBtn.parentElement.remove();
      }
    } catch (error) {
      console.error("Load more error:", error);
    }
  }

  function handleTabClick(e) {
    e.preventDefault();
    const tab = e.currentTarget;
    const target = tab.getAttribute("href");

    tabs.forEach((t) => t.classList.remove("active"));
    tab.classList.add("active");

    currentOffset = 0;
    currentType = target.substring(1).replace("-news", "");

    let endpoint;
    switch (target) {
      case "#events":
        endpoint = "/get_events/";
        break;
      case "#company-news":
        endpoint = "/get_news/";
        break;
      case "#global-news":
        endpoint = "/get_global_news/";
        break;
      default:
        return;
    }

    loadContent(endpoint);
  }

  tabs.forEach((tab) => {
    tab.addEventListener("click", handleTabClick);
  });

  document
    .querySelector(".news-load-more")
    ?.addEventListener("click", function (e) {
      e.preventDefault();
      handleLoadMore();
    });

  if (window.location.hash) {
    const initialTab = document.querySelector(
      `a[href="${window.location.hash}"]`
    );
    if (initialTab) initialTab.click();
  } else {
    document.querySelector(".prod_tab_sc a.active").click();
  }
});
