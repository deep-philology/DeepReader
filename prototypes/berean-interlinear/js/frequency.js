$(function() {
  $(".freq-toggle").on("click", function() {
    var limit = parseInt($(this).data("limit"));
    $("p.gls").each(function() {
      var freq = parseInt($(this).data("freq"));
      if (freq < limit) {
        $(this).addClass("show");
      } else {
        $(this).removeClass("show");
      }
    });
  });
});
