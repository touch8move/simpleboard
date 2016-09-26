$(document).ready(function() {
    if($.trim($("#replyerrormsg").text()).length>0){
        $("#replyerrormsg").show("fast", function(){
            setTimeout(function(){
                $("#replyerrormsg").hide("fast");
            },3000);
        });
    }
});