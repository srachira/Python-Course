var tfeed = require('twit');
var feed = new tfeed({
consumer_key:'GOJuHPXg0h2Wd3AdAHtH2w',
consumer_secret:'VwLa5FSTn8dUwpDx9yLpSO14CEovoEdHgCAYVxgc',
access_token:'157673848-QsDGdtI1MoBGtJ5tbC4ySWWa9JRENiZk0BVxPHab',
access_token_secret:'mM3huIMUI2hwwAg6moUTiqnmoGpOBx6RV3jLZS4p4'
});
feed.get('statuses/user_timeline', {screen_name:'iamsrk', count: 5}, function(err,msg){
//if (err) {
//	console.log(err);
//}
//console.log(msg);
var tweets="Last 5 tweets of King SRK\n";
for(var i=0;i<msg.length;i++){
tweets+=String(i+1)+'. '+msg[i]["text"]+"\n";
}
//console.log(tweets);
var request=require('request');

var APP_ID="404313973011593";
var APP_SECRET="1e634f3b4312fe4cebf5ffe19b541ba5";
request.get("https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id="+APP_ID+"&client_secret="+APP_SECRET,function(error,response,accessToken)
{
if (!(!error && response.statusCode == 200)) {
console.log(error);
}
console.log(tweets);
ACCESS_TOKEN = 'CAACEdEose0cBABlAUVw12h7YlYiAXr1a231Bwys2RZArpiCevQn367WaFhWgZATPWFIvapH0T3yw6YPCnC4JTEmPKj0EhDyZABLfZAZCyvqJIBCsUgTJ2RM37XHY9gn6onuXuSyTxpTwrB18HqN2a9sc7Yr5Ic0VEhAlzj4qxYwZDZD';
var url = 'https://graph.facebook.com/Shravanrachiraju/feed';
var params = {
access_token: ACCESS_TOKEN,
message: tweets
};
request.post({url: url,qs: params},function(error,response,feed)
{
if (!(!error && response.statusCode == 200)) {
console.log(error);
}
//this is the feed you will get
console.log(feed);
})
});
});