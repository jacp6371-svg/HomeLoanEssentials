// Homepage: choosing a service row pre-fills the Service field in the contact form.
document.querySelectorAll('[data-service]').forEach(function (link) {
  link.addEventListener('click', function () {
    var select = document.getElementById('cf-service');
    if (select) select.value = link.getAttribute('data-service');
  });
});
