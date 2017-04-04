$(function() {
  $(".freq-toggle").on("click", function() {
    $(".freq-toggle").removeClass("selected");
    $(this).addClass("selected");
    var limit = parseInt($(this).data("limit"));
    $(".gls").each(function() {
      var freq = parseInt($(this).data("freq"));
      if (freq < limit) {
        $(this).addClass("show");
      } else {
        $(this).removeClass("show");
      }
    });
  });
});
