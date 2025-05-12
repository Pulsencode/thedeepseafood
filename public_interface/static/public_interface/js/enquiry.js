    $(document).ready(function () {
      const responseModal = new bootstrap.Modal('#responseModal');
      let timeoutId;

      $("#contact_form").submit(function (event) {
        event.preventDefault();
        const $form = $(this);

        $.ajax({
          type: "POST",
          url: $form.attr("action"),
          data: $form.serialize(),
          success: function (response) {
            showModal("Success", "Enquiry submitted successfully!", "success");
            $form[0].reset();
          },
          error: function (xhr) {
            const errorMessage =
              JSON.parse(xhr.responseText).message || "An error occurred.";
            showModal("Error", errorMessage, "danger");
          }
        });
      });

      function showModal(title, message, type) {
        const modal = $('#responseModal');
        const iconStatus = modal.find('.icon-status');
        
        // Reset modal content
        modal.find('.fa-check-circle, .fa-times-circle').addClass('d-none');
        modal.find('.modal-title').text(title);
        modal.find('.modal-message').text(message);
        
        // Update styling based on type
        const isSuccess = type === 'success';

        iconStatus.find(isSuccess ? '.fa-check-circle' : '.fa-times-circle').removeClass('d-none');
        modal.find('.progress-bar').addClass(isSuccess ? 'bg-success' : 'bg-danger')
        // Show and animate progress bar
        modal.find('.progress').show().css('width', '0%');
        modal.find('.progress-bar').css('width', '100%');
        
        // Clear existing timeout
        if (timeoutId) clearTimeout(timeoutId);
        
        // Show modal
        responseModal.show();
        
        // Auto-hide after delay
        timeoutId = setTimeout(() => {
          responseModal.hide();
        }, type === 'success' ? 3000 : 5000);
      }

      // Reset modal on close
      $('#responseModal').on('hidden.bs.modal', function () {
        $(this).find('.progress-bar').removeClass('bg-success bg-danger');
      });
    });