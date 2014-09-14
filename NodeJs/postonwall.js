var request = require('request');

var APP_ID = "423245021044843";
var APP_SECRET = "6cd7f1e6a47930c0245a41b9772dbcb1";
ACCESS_TOKEN = 'CAACEdEose0cBAArtd7okkFWG4NT9r1DpCjWDqfW2AMSctotHN5JL7o7G5uZAZAZAQJHhcUYWftFOCRTaNOnlLo1sB74Qqdx6ZAjpi8tGLWUsKXUupgDfZB0lLVbRKsa6vWsnmknfETW3ynMuEeHT7eMXdsNmgQI7hGhhLRAEV4wZDZD';
request.get("https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id="+APP_ID+"&client_secret="+APP_SECRET,function(error,response,accessToken)
{
if (!(!error && response.statusCode == 200)) {
console.log(error);
}
{
if (!(!error && response.statusCode == 200)) {
console.log(error);
}
//To get the access token from access_token=555776051108082|IMTS2Pu70Fk0pVmSDp0aB_SouiE

console.log(ACCESS_TOKEN);
//request to fetch feed from thecloudgust
var url = 'https://graph.facebook.com/Shravanrachiraju/feed';

var params = {
access_token: ACCESS_TOKEN,
message: "Nithin Koram Edava"
};

request.post({url: url, qs: params}, function(error, response, feed)
{
if (!(!error && response.statusCode == 200)) {
console.log(error);
}
});
    }
});
