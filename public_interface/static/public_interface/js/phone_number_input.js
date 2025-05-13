const phoneInputs = document.querySelectorAll(
  "#id_phone_number, #id_phone_number_application"
);
const itiInstances = []; // Store instances for later use

phoneInputs.forEach((input) => {
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

  itiInstances.push(iti); // Store the instance

  // Update the correct input before its form submission
  input.closest("form").addEventListener("submit", function (e) {
    input.value = iti.getNumber();
  });
});
