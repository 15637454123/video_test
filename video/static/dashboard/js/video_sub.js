var inputNumber = $('#number');
var inputUrl = $('#url');
var inputId = $('#videosub-input-id');

$('.update-btn').click(function(){
    var videosubId = $(this).attr('data-id');
    var videosubNumber = parseInt($(this).attr('data-number'));
    var videosubUrl = $(this).attr('data-url');

    inputNumber.val(videosubNumber);
    inputUrl.val(videosubUrl);
    inputId.val(videosubId);
});