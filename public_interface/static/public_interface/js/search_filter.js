 $(document).ready(function () {
  function fetchProducts(type = '', search = '') {
    $.ajax({
      url: window.location.pathname,  // works for home or product page
      data: {
        type: type,
        search: search
      },
      headers: {
        "X-Requested-With": "XMLHttpRequest"
      },
      success: function (response) {
        // Support both home and product page containers
        if ($('#prodlist').length) {
          $('#prodlist').html(response.html);
        } else if ($('#index_product').length) {
          $('#index_product').html(response.html);
        }
      },
      error: function () {
        alert("Something went wrong. Please try again.");
      }
    });
  }

  // Handle filter buttons
  $('#filter button').click(function (e) {
    e.preventDefault();
    let type = $(this).val();
    let search = $('#inputvalue').val ? $('#inputvalue').val() : '';
    fetchProducts(type, search);

    $('#filter button').removeClass('active');
    $(this).addClass('active');
  });

  // Handle search (only for product page)
  $('#search_form').submit(function (e) {
    e.preventDefault();
    let type = $('#filter button.active').val() || '';
    let search = $('#inputvalue').val();
    fetchProducts(type, search);
    $('#inputvalue').val('');
  });
});