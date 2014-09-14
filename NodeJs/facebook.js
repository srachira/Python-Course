var request = require('request');

var APP_ID = "423245021044843";
var APP_SECRET = "6cd7f1e6a47930c0245a41b9772dbcb1";
request.get("https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id="+APP_ID+"&client_secret="+APP_SECRET,function(error,response,accessToken)
{
if (!(!error && response.statusCode == 200)) {
console.log(error);
}
//To get the access token from access_token=555776051108082|IMTS2Pu70Fk0pVmSDp0aB_SouiE
ACCESS_TOKEN = 'CAACEdEose0cBAArtd7okkFWG4NT9r1DpCjWDqfW2AMSctotHN5JL7o7G5uZAZAZAQJHhcUYWftFOCRTaNOnlLo1sB74Qqdx6ZAjpi8tGLWUsKXUupgDfZB0lLVbRKsa6vWsnmknfETW3ynMuEeHT7eMXdsNmgQI7hGhhLRAEV4wZDZD';
console.log(ACCESS_TOKEN);
//request to fetch feed from thecloudgust
var graph_url='Shravanrachiraju?fields=friends.fields(name,birthday)';
request.get("https://graph.facebook.com/"+graph_url+"&access_token="+ACCESS_TOKEN,function(error,response,feed)
{
if (!(!error && response.statusCode == 200)) {
console.log(error);
}
//this is the feed you will get
console.log(feed);
var json_data=JSON.parse(feed);
var frnds_data=json_data.friends.data;
var data_len=frnds_data.length;
var comp_data=new Date();

var final_data=new Array();
var j=0;
for (var i=0;i<data_len;i++){
    var bir=new Date(frnds_data[i].birthday);
    //console.log(bir.getMonth(),comp_data.getMonth());
    if (bir.getMonth()>=comp_data.getMonth() && bir.getMonth()<comp_data.getMonth()+1 )
	{
		if(bir.getDate()>comp_data.getDate() && bir.getDate()<=comp_data.getDate()+7)
        final_data[j++]=frnds_data[i].name +'  '+frnds_data[i].birthday+'\n';
    }
    
}
  var email   = require("emailjs");
    var server  = email.server.connect({
   user:    "shravan.rachiraju@gmail.com", 
   password:"123kingofkings", 
   host:    "smtp.gmail.com", 
   ssl:     true

});

// send the message and get a callback with an error or details of the message that was sent
server.send({
   text:    final_data.sort(), 
   from:    "shravan.rachiraju@gmail.com", 
   to:      "shravan.rachiraju@gmail.com",
   subject: "birthdays"
}, function(err, message) { console.log(err || message); });
    
//console.log(final_data.sort());
    
});
});