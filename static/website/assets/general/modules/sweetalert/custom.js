$("body").on("click", ".swal_btn_delete", function (event) {
  var ids = $(this).data("class")
  swal({
    title: "Are you sure ?",
    text: "Are you sure you wanted to delete Content ?",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: '#f56905',
    confirmButtonText: 'Yes, delete it!',
    closeOnConfirm: false
  },
    function () {
      $.ajax({
        headers: csrf_header,
        url: window.delete_url.replace('0', ids) + '?return=' + window.current_url_encoded,
        type: "POST",
        data: {
        },
        success: function (data) {
          swal({ title: "Delete!", text: "This data has been deleted!", type: "success" },
            function () {
              location.reload();
            }
          );
        }
      });

    });
})



// swal_btn_deactivate
$("body").on("click", ".swal_btn_deactivate", function (event) {
  var ids = $(this).data("id")
  swal({
    title: "Are you sure ?",
    text: "Are you sure you wanted to deactivate/activate Content ?",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: '#f56905',
    confirmButtonText: 'Yes, deactivate/activate it!',
    closeOnConfirm: false
  },
    function () {
      $.ajax({
        headers: csrf_header,
        url: window.disable_url.replace('0', ids) + '?return=' + window.encoded_url,
        type: "POST",
        data: {
        },
        success: function (data) {
          swal({ title: "deactivated/activated!", text: "This data has been deactivated/activated!", type: "success" },
            function () {
              location.reload();
            }
          );
        }
      });

    });
})

// swal_btn_enable_disable
$('.swal_btn_enable_disable').click(function () {
  var ids = $(this).data("class")
  swal({
    title: "Are you sure ?",
    text: "Are you sure you wanted to enable/disable Content ?",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: '#f56905',
    confirmButtonText: 'Yes, enable/disable it!',
    closeOnConfirm: false
  },
    function () {
      $.ajax({
        headers: csrf_header,
        data: {
        },
        success: function (data) {
          swal({ title: "enable/disable!", text: "This data has been enable/disable!", type: "success" },
            function () {
              location.reload();
            }
          );
        }
      });

    });
})

// swal_btn_activate_deactivate
$('.swal_btn_activate_deactivate').click(function () {
  var ids = $(this).data("class")
  swal({
    title: "Are you sure ?",
    text: "Are you sure you wanted to activate/deactivate Content ?",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: '#f56905',
    confirmButtonText: 'Yes, activate/deactivate it!',
    closeOnConfirm: false
  },
    function () {
      $.ajax({
        headers: csrf_header,
        data: {
        },
        success: function (data) {
          swal({ title: "activate/deactivate!", text: "This data has been activate/deactivate!", type: "success" },
            function () {
              location.reload();
            }
          );
        }
      });

    });
})

// swal_btn_mark_unmark
$('.swal_btn_mark_unmark').click(function () {
  var ids = $(this).data("id")
  swal({
    title: "Are you sure ?",
    text: "Are you sure you wanted to mark/unmark Content ?",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: '#f56905',
    confirmButtonText: 'Yes, mark/unmark it!',
    closeOnConfirm: false
  },
    function () {
      $.ajax({
        headers: csrf_header,
        url: window.recommended_course_url.replace('0', ids) + '?return=' + window.encoded_url,
        type: "POST",
        data: {
        },
        success: function (data) {
          swal({ title: "mark/unmark!", text: "This data has been mark/unmark!", type: "success" },
            function () {
              location.reload();
            }
          );
        }
      });

    });
})

// swal_btn_mark_unmark
$('.swal_btn_best_seller').click(function () {
  var ids = $(this).data("id")
  swal({
    title: "Are you sure ?",
    text: "Are you sure you wanted to mark/unmark Content as Best Seller?",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: '#f56905',
    confirmButtonText: 'Yes, mark/unmark it!',
    closeOnConfirm: false
  },
    function () {
      $.ajax({
        headers: csrf_header,
        url: window.best_seller_course_url.replace('0', ids) + '?return=' + window.encoded_url,
        type: "POST",
        data: {
        },
        success: function (data) {
          swal({ title: "mark/unmark!", text: "This data has been mark/unmark!", type: "success" },
            function () {
              location.reload();
            }
          );
        }
      });

    });
})

// swal_btn_active_remove
$('.swal_btn_active_remove').click(function () {
  var ids = $(this).data("class")
  swal({
    title: "Are you sure ?",
    text: "Are you sure you wanted to active/remove Content ?",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: '#f56905',
    confirmButtonText: 'Yes, active/remove it!',
    closeOnConfirm: false
  },
    function () {
      $.ajax({
        headers: csrf_header,
        data: {
        },
        success: function (data) {
          swal({ title: "active/remove!", text: "This data has been active/remove!", type: "success" },
            function () {
              location.reload();
            }
          );
        }
      });

    });
})