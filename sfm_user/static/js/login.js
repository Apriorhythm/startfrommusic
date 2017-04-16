$(function(){  
	$('#loginButton').click(function(){

		var uid = $("#uid").val();  
		var password = $("#password").val();  

		alert(uid + " " + password);

		$.post('validate',{uid:uid, password:password},function(data){
			alert(data)
			if ("OK" == data)
				window.location.href = "/";
		});
	});  


	$('#registerButton').click(function(){
		window.location.href = "/user/register"
	});  
});
