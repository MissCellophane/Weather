$(document).ready(function(){
    $("#login").click(function(){
        var id=$("#id").val();
        var psw=$("#psw").val();
        console.log(id);
        $.post('/apis/login_check', {ID:id, PSW:psw}, function(res){
            if (res.status){
                alert("登录成功");
            }
            else{
                alert("用户名或密码不正确");
            }
        });
    });

    $('#register').click(function(){
        var id = $("#id").val();
        var psw = $("#psw").val();
        $.post('/apis/register', {ID: id, PSW: psw}, function(res){
            if (!res.status){
                alert("注册成功");
                $("input").val('');
            }
            else{
                alert("用户名已存在");
            }
        });
    }) ;
});
