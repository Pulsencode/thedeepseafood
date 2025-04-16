// datatables
$(".data_table").DataTable({
  responsive: true,
  autoWidth: false,
  ordering: true, // short

  //for sorting icon disable and hide for first row
  //'columnDefs': [{ 'orderable': false, 'targets': 0 }], // hide sort icon on header of first column
  //'aaSorting': [[1, 'asc']],

  language: {
    search: "", // search label remove
    searchPlaceholder: "Search",
    paginate: {
      next: "&#8250;", // arrow
      previous: "&#8249;", // arrow
    },
  },
  dom: '<"datatable-header dt-buttons-right"fBl><"datatable-scroll"tS><"datatable-footer"ip>',
  buttons: {
    dom: {
      button: {
        className: "btn",
      },
    },
    buttons: [
      {
        extend: "print",
        /*
        customize: function (doc) {
          $(doc.document.body).find('table').css('font-size', '10pt');
          $(doc.document.body).find('table').css('border', '1px solid #000');
          $(doc.document.body).find('table td').css('border-left', '1px solid #000');
          $(doc.document.body).find('table td').css('border-top', '1px solid #000');
          $(doc.document.body).find('table td').css('border-right', '1px solid #000');
          $(doc.document.body).find('table td').css('border-bottom', '1px solid #000');
          $(doc.document.body).find('table td').css('text-align', 'left');
        },*/
        exportOptions: {
          columns: "thead th:not(.data_table_no_export)",
        },
      },
      {
        extend: "excel",
        exportOptions: {
          columns: "thead th:not(.data_table_no_export)",
        },
      },
      {
        extend: "csv",
        exportOptions: {
          columns: "thead th:not(.data_table_no_export)",
        },
      },
    ],
  },
});
