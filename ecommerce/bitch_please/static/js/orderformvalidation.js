function validateForm() {
  var x = document.forms["myForm"]["address"].value;
  if (x.length < 20) {
    alert("Please enter valid address");
    return false;
  }
}