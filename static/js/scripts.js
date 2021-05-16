function copyFunction() {
  var copyText = document.getElementById("{{photo.id}}.url");

  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */
  document.execCommand("copy");
  alert("Copied the text: " + copyText.value);
}
