{% load static %}

<form method="post" class="form" action="{% url 'web:common:contact' %}" >{%csrf_token%}
  <div class="body">
    <div class="row">
     <div class="col-12">
      <input class="form-control text-blue" name="name" type="text" maxlength="50" placeholder="Your Name" required>
     </div>
     <div class="col-12">
      <input class="form-control text-blue" name="mobile_no" type="text" maxlength="15" placeholder="Phone Number" required>
     </div>
     <div class="col-12">
      <input class="form-control text-blue" name="email" type="email" maxlength="100" placeholder="Email" required>
     </div>
     <div class="col-12">
      <input class="form-control text-blue" name="location" type="text" maxlength="100" placeholder="Location" required>
     </div>
     <div class="col-12">
      <textarea class="form-control text-blue h-70-px" name="message" maxlength="500" placeholder="Message" required></textarea>
     </div>
    </div>
  </div>
  <div class="foot text-center">
    <input type="hidden" name="recaptcha_token">
    <button type="submit" style="display: none;" id="BTN_SUBMIT_HIDDEN"></button>
    <button type="button" onclick="submitWithReCaptcha()"  class="BTN_SUBMIT btn btn-primary font-lntermedium">Send Enquiry</button>
  </div>
</form>


{% block javascript %}
<script src="https://www.google.com/recaptcha/api.js?render={{recaptcha_site_key}}"></script>
<script>
  window.recaptcha_site_key="{{recaptcha_site_key}}";
  function submitWithReCaptcha() {
    if(window.captcha_loading) return;
    window.captcha_loading=true;
    grecaptcha.execute(window.recaptcha_site_key, {action: 'onlineadmission'}).then(function(token) {
      $('input[name="recaptcha_token"]').val(token);
      window.captcha_loading=false;
      $('#BTN_SUBMIT_HIDDEN').click();
    });
  }
</script>
{% endblock %}