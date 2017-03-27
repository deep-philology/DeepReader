$(function() {
  $(".toggle").on("click", function() {
    $("body").toggleClass($(this).data("target"));
    return false;
  });
});
