function getCookie(c_name) {
   var i,x,y,ARRcookies=document.cookie.split(";");
   for (i=0;i<ARRcookies.length;i++){
      x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
      y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
      x=x.replace(/^\s+|\s+$/g,"");
      if (x==c_name) {
        return unescape(y);
      }
   }
}

function setCookie(c_name,value,exdays) {
   var exdate=new Date();
   exdate.setDate(exdate.getDate() + exdays);
   var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
   document.cookie=c_name + "=" + c_value;
}

function checkForm(form){
   var search = form.children[1].value;
   if (search == null) {
      return false;
   }
   if (search == "elon musk") {``
      alert("Currently off-planet");
   }
   return true;
}

function splash() {
   if (getCookie("first_visit") != "true") {
      document.cookie = "first_visit=true";
      location.href="http://127.0.0.1:8000/";    
  }
}