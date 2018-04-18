// 点击按钮后获取勾选多选框的值
$(function(){
	// 设置属性值
	$("#add").click(function() {
        var select_lession = new Array();
        //　将勾选的值放入select_lession数组中
		$("input:checkbox[name='select']:checked").each(function(i,n) {
			select_lession[i] = $(this).val();
		});
		$("div.modal-body").empty();
		//遍历数组　添加到div中
        $.each(select_lession,function(i,select_lession){
           $("div.modal-body").append("<p>"+select_lession+"</p>");
        });
        $("#save").click(function(){
       $.ajax({
                 type:"post",
                 dataType:'JSON',
                 url:"/select",
                 chche:false,
                 async:true,
                 data: {
                 'student_name':$(".student_value").val(),
                 'lession_name': JSON.stringify(select_lession),
                 },
        success: function(data) {
                    var exists = data.exists_lession;
                    if (exists.length>0){
                        alert("以下课程重复:\n"+exists
                        +"添加了以下课程:\n"+data.insert_lession);
                        window.location.reload();
                    }
                    else{
                        window.location.reload();
                    }
                 }
            });
            return false;
    });
	});
});

// 退选课程
$(function(){
    $("#remove_lession").click(function(){
         $.ajax({
                 type:"post",
                 dataType:'JSON',
                 url:"/remove_lession",
                 chche:false,
                 async:true,
                 data: {
                 'student':$("input[name='student']").val(),
                 'lession': $("input[name='lession']").val(),
                 },
        success: function(data) {
                     alert("退选成功");
                     window.location.reload();
                 }
            });
            return false;
    });
})

