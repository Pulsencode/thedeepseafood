function initializePhoneInputs() {
  const phoneInputs = document.querySelectorAll(
    "#id_phone_number, #id_phone_number_application"
  );
  const itiInstances = [];

  phoneInputs.forEach((input) => {
    // Destroy existing instance if it exists
    if (input.intlTelInputInstance) {
      input.intlTelInputInstance.destroy();
      delete input.intlTelInputInstance;
    }

    // Initialize new instance
    const iti = window.intlTelInput(input, {
      initialCountry: "auto",
      autoPlaceholder: "off",
      geoIpLookup: function (callback) {
        fetch("https://ipapi.co/json")
          .then((res) => res.json())
          .then((data) => callback(data.country_code))
          .catch(() => callback("us"));
      },
      utilsScript:
        "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
    });

    // Store instance reference
    input.intlTelInputInstance = iti;
    itiInstances.push(iti);

    // Update phone number before form submission
    const form = input.closest("form");
    if (form) {
      form.addEventListener("submit", function (e) {
        input.value = iti.getNumber();
      });
    }
  });
}

// Initialize on page load
document.addEventListener("DOMContentLoaded", initializePhoneInputs);

// Make function available for AJAX reinitialization
window.initializePhoneInputs = initializePhoneInputs;
