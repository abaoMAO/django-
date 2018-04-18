$(function(){
    $("#save").click(function(){
         $.ajax({
                 type:"post",
                 dataType:'JSON',
                 url:"/modify_score",
                 chche:false,
                 async:true,
                 data: {
                    'student':$("input[name='student']").val(),
                    'lession':$("input[name='lession']").val(),
                    'score' : $("input[name='score']").val(),
                 },
        success: function(data) {

                     //window.location.reload();
                 }
            });
            return false;
    });
})
