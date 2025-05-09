// Target the phone number field with the ID 'id_phone_number'
const phoneInput = document.querySelector("#id_phone_number");
const iti = window.intlTelInput(phoneInput, {
  initialCountry: "auto",
  geoIpLookup: function (callback) {
    fetch("https://ipapi.co/json")
      .then((res) => res.json())
      .then((data) => callback(data.country_code))
      .catch(() => callback("us")); // Fallback to US if IP lookup fails
  },
  utilsScript:
    "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});

// Update the phone number field with the full international number before form submission
document.querySelector("form").addEventListener("submit", function () {
  const fullNumber = iti.getNumber();
  phoneInput.value = fullNumber;
});
