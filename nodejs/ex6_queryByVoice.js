const record=require('node-record-lpcm16');
const aikit=require('./aimakerskitutil');
const client_id='Y2xpZW50X2lkMTU4NzA5MDkyMTYyMg==';
const client_key='Y2xpZW50X2tleTE1ODcwOTA5MjE2MjI=';
const client_secret='Y2xpZW50X3NlY3JldDE1ODcwOTA5MjE2MjI=';
const json_path='/home/pi/Downloads/clientKey.json';
const cert_path='../data/ca-bundle.pem';
const proto_path='../data/gigagenieRPC.proto';

//aikit.initialize(client_id,client_key,client_secret,cert_path,proto_path);
aikit.initializeJson(json_path,cert_path,proto_path);
function initMic(){
        return record.start({
                sampleRateHertz: 16000,
                threshold: 0,
                verbose: false,
                recordProgram: 'arecord',
                silence: '10.0',
        })
};

const query=aikit.queryByVoice((err,msg)=>{
	if(err){
		console.log(JSON.stringify(err));
	} else {
		console.log('Msg:'+JSON.stringify(msg));
	}
	record.stop();
})
query.write({reqOptions:{lang:0,userSession:'12345',deviceId:'D06190914TP808IQKtzq'}});
const mic=initMic();
mic.on('data',(data)=>{
	query.write({audioContent:data});
});
console.log('say something');
