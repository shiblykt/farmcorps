function signup_validate(){

    s = 1

    fName = document.getElementById('userFirstName').value
    if(fName==""){
      document.getElementById('userFirstName').style.border = '3px solid red'
        s = 0
    }else{
        document.getElementById('userFirstName').style.border = '3px solid green'
    }

    lName = document.getElementById('userLastName').value
    if(lName==""){
        document.getElementById('userLastName').style.border = '3px solid red'
        s = 0
    }else{
        document.getElementById('userLastName').style.border = '3px solid green'
    }

    var re =  /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
    mail = document.getElementById('userEmail').value
    if(mail.match(re)){
      document.getElementById('userEmail').style.border = '3px solid green'
    }else{
        document.getElementById('userEmail').style.border = '3px solid red'
        s = 0
    }
    
    mobile = document.getElementById('userMobile').value
    if(mobile==""){
        document.getElementById('userMobile').style.border = '3px solid red'
        s = 0
    }else{
        document.getElementById('userMobile').style.border = '3px solid green'
    }

    var rep = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,15}$/
    passwd = document.getElementById('userPassword').value
    passwd2 = document.getElementById('userPassword2').value
    if(passwd.match(rep)){
        document.getElementById('userPassword').style.border = '3px solid green'
    }else{
        document.getElementById('userPassword').style.border = '3px solid red'
        s = 0
    }
    if(passwd2.match(rep)){
        document.getElementById('userPassword2').style.border = '3px solid green'
    }else{
        document.getElementById('userPassword2').style.border = '3px solid red'
        s = 0
    }

 

    if(passwd != passwd2){
        document.getElementById('userPassword').style.border = '3px solid red'
        document.getElementById('msgpasswd').innerHTML = 'password mismatch!'
        document.getElementById('msgpasswd').style.color = 'red'
        document.getElementById('userPassword2').style.border = '3px solid red'
        s = 0
    }else{
        document.getElementById('msgpasswd').innerHTML = ''
    }
    
    address = document.getElementById('userAddress').value
    if(address==""){
        document.getElementById('userAddress').style.border = '3px solid red'
        s = 0
    }else{
        document.getElementById('userAddress').style.border = '3px solid green'
    }

    city = document.getElementById('userCity').value
    if(city==""){
        document.getElementById('userCity').style.border = '3px solid red'
        s = 0
    }else{
        document.getElementById('userCity').style.border = '3px solid green'
    }


    var r = /^[0-9]{6}$/
    pin = document.getElementById('userPin').value
    if(pin.match(r)){
        document.getElementById('userPin').style.border = '3px solid green'
    }else{
        document.getElementById('userPin').style.border = '3px solid red'
        s = 0
    }

    if(s==0){
        return false
    }
}

