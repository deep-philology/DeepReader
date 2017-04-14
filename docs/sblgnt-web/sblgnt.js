$(function() {
  var positions = [];
  $(".chapter").each(function(i, e) {
    positions[positions.length] = {
      start: $(e).offset().top,
      end: $(e).offset().top + $(e).height(),
      id: $(e).attr("id"),
      selected: null
    }
  });
  function update() {
    var window_start = $(window).scrollTop();
    var window_end = window_start + $(window).height();

    for (var i=0; i<positions.length; i++) {
      if (window_start < positions[i].end && window_end > positions[i].start) {
        if (!positions[i].selected) {
          $("a[href='#" + positions[i].id + "']").parent().addClass("active");
          positions[i].selected = true;
        }
      } else {
        if (positions[i].selected) {
          $("a[href='#" + positions[i].id + "']").parent().removeClass("active");
          positions[i].selected = false;
        }
      }
    }
  }
  $(window).bind("scroll", update);
  $(window).bind("resize", update);
  update();
  $(".verse_num").hover(
    function() {
      $("#text").addClass("lowlight");
      var verse = $(this).data("verse");
      $("#verse-" + verse).addClass("highlight");
    },
    function() {
      $("#text").removeClass("lowlight");
      var verse = $(this).data("verse");
      $("#verse-" + verse).removeClass("highlight");
    }
  );
  $(".word").hover(
    function() {
      var form = $(this).data("form");
      var pos = $(this).data("pos")
      var parse = $(this).data("parse");
      var lemma = $(this).data("lemma");
      $(this).after(' <span class="analysis"><div class="form">' + form + '</div><div class="pos">' + pos + '</div><div class="parse">' + parse + '</div><div class="lemma">' + lemma + '</div></span> ');
    },
    function() {
      $(".analysis").remove();
    }
  )
});
