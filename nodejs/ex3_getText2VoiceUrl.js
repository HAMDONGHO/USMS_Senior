const aikit=require('./aimakerskitutil');
const client_id='Y2xpZW50X2lkMTU4NzA5MDkyMTYyMg==';
const client_key='Y2xpZW50X2tleTE1ODcwOTA5MjE2MjI=';
const client_secret='Y2xpZW50X3NlY3JldDE1ODcwOTA5MjE2MjI=';
const json_path='/home/pi/Downloads/clientKey.json';
const cert_path='../data/ca-bundle.pem';
const proto_path='../data/gigagenieRPC.proto';

//aikit.initialize(client_id,client_key,client_secret,cert_path,proto_path);
aikit.initializeJson(json_path,cert_path,proto_path);
aikit.getText2VoiceUrl({lang:0,text:'안녕하세요. 만나서 반갑습니다.'},(err,msg)=>{
	console.log('err:'+JSON.stringify(err)+' msg:'+JSON.stringify(msg));
})
