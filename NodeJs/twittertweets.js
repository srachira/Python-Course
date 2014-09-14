var Twit = require('twit');

var T = new Twit({
    consumer_key:         'ZEHDFKGxBtiUPSo5BRS6A',
    consumer_secret:      '2rgQGHMZOubrfwt3DRSHlCSvoW4A8ErEYVoIKNLHM8',
    access_token:         '119364106-wBGL5fg7HOPiVDWP74RAfrnLT4ztudtJDtrn4tlz',
    access_token_secret:  'NPd1Hy1g5RIWRElOJ5CUSRuExrwsAnPvI42BKuYzU'
});


T.get('search/tweets', { q:'banana',count:3 }, function(err, reply) {
    console.log(reply);

});