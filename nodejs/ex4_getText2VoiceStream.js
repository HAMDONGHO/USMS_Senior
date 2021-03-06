const Speaker=require('speaker');
const pcmplay=new Speaker({
	channels:1,
	bitDepth:16,
	sampleRate:16000
});

const aikit=require('./aimakerskitutil');
const client_id='Y2xpZW50X2lkMTU4NzA5MDkyMTYyMg==';
const client_key='Y2xpZW50X2tleTE1ODcwOTA5MjE2MjI=';
const client_secret='Y2xpZW50X3NlY3JldDE1ODcwOTA5MjE2MjI=';
const json_path='/home/pi/Downloads/clientKey.json';
const cert_path='../data/ca-bundle.pem';
const proto_path='../data/gigagenieRPC.proto';

//aikit.initialize(client_id,client_key,client_secret,cert_path,proto_path);
aikit.initializeJson(json_path,cert_path,proto_path);
kttts=aikit.getText2VoiceStream({text:'안녕하세요. 반갑습니다.',lang:0,mode:0});
kttts.on('error',(error)=>{
                console.log('Error:'+error);
});
kttts.on('data',(data)=>{
                if(data.streamingResponse==='resOptions' && data.resOptions.resultCd===200) console.log('Stream send. format:'+data.resOptions.format);
                if(data.streamingResponse==='audioContent') {
			pcmplay.write(data.audioContent);
		} else console.log('msg received:'+JSON.stringify(data));
});
kttts.on('end',()=>{
        console.log('pcm end');
});
function finish(){
	console.log('tts played');
};
setTimeout(finish,5000);
