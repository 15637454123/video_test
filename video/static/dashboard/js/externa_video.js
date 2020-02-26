
var videoEreaStatic = false;
var videoEreaArea = $('#video-deit-area');

$('#open-add-video-btn').click(function(){
    if (!videoEreaStatic){
        videoEreaArea.show();
        videoEreaStatic = true;
    }else{
        videoEreaArea.hide();
        videoEreaStatic = false;
    }
});