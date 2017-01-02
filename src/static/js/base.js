/*-- like button --*/
/*
Reference Code
title: Periscope Likes Tutorial
date: Jun 6, 2015
author: Zan Ilic
available at: http://zanilic.com/periscope-likes-tutorial-jquery-css3
*/

$(document).ready(function() {
$('button').on('click', function() {
  // change button type by clicking
  $('.heart-shaped').toggle();

  // initailize
  var rand = Math.floor((Math.random() * 100) + 1);
  var flows = ["flows"];
  var colors = ["heart-particle-col"];
  var timing = (1.3).toFixed(1);

  // Animate Particle
  $('<div class="heart-particle part-' + rand + ' ' + colors[Math.floor((Math.random()))] + '" style="font-size:' + Math.floor(Math.random() * (28 - 12)) + 'px;"><i class="fa fa-heart"></i><i class="fa fa-heart"></i></div>').appendTo('.heart-particle-box').css({
    animation: "" + flows[Math.floor((Math.random()))] + " " + timing + "s linear"
  });
  $('.part-' + rand).show();
  // Remove Particle
  setTimeout(function() {
    $('.part-' + rand).remove();
  }, timing * 1000 - 100);
});
});


/* like counting */
$(document).ready(function() {
    $('.post-likes').click(function() {
        var id;
        id = $(this).attr('data-post-id');
        $.get('/like-blog/', {
            post_id: id
        }, function(data) {
            $('.like_count_blog').html(data);
        });
    });
}
