$(function() {
  $(".unit").on("click", function() {
    $(this).children("p.gls").toggleClass("show");
  });
});
