// You should not be using jQuery yet. This is just here so I don't forget to make it.

$(function(){
  $('body').css({
    background: 'black',
    color: 'white'
  });
  
  $('body').append(
    $('<p>').text('Hello, world!')
      .css({
        'font-size': '3em'
      })
  });
});