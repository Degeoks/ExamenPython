window.fbAsyncInit = function() {
    FB.init({
        appId      : '1177380505758179',
        cookie     : true,
        xfbml      : true,
        version    : 'v3.2'
    });

    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });  
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

function statusChangeCallback(response){
    if(response.status === 'connected'){
        receiveInfo();
    }else{
        console.log('Not Logged')
    }
}

function checkLoginState(){
    FB.getLoginStatus(function(response){
        statusChangeCallback(response);
    });
}

function receiveInfo(){
    FB.api(
        '/me',
        'GET',
        {"fields":"id,first_name,last_name"},
        function(response) {
            var nombreUsuario = response.first_name+" "+response.last_name;
            var sesion = document.getElementById("usuario");
            document.write(nombreUsuario);
        }
    );
}