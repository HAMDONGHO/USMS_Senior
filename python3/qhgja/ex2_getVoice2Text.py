#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 2: STT - getVoice2Text """

from __future__ import print_function
import grpc
import gigagenieRPC_pb2
import gigagenieRPC_pb2_grpc
import MicrophoneStream as MS
import user_auth as UA
import audioop
import os
import time
import ex1_kwstest as kws
from ctypes import *

HOST = 'gate.gigagenie.ai'
PORT = 4080
RATE = 16000
CHUNK = 512

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  dummy_var = 0
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)

def generate_request():
    with MS.MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
    
        for content in audio_generator:
            message = gigagenieRPC_pb2.reqVoice()
            message.audioContent = content
            yield message
            
            rms = audioop.rms(content,2)
            #print_rms(rms)

def getVoice2Text():	
    print ("\n주문하실 메뉴를 말씀해주세요\n")
    channel = grpc.secure_channel('{}:{}'.format(HOST, PORT), UA.getCredentials())
    stub = gigagenieRPC_pb2_grpc.GigagenieStub(channel)
    request = generate_request()
    resultText = ''
    for response in stub.getVoice2Text(request):
        if response.resultCd == 200: # partial
            print('resultCd=%d | recognizedText= %s' 
                  % (response.resultCd, response.recognizedText))
            resultText = response.recognizedText
        elif response.resultCd == 201: # final
            print('resultCd=%d | recognizedText= %s' 
                  % (response.resultCd, response.recognizedText))
            resultText = response.recognizedText
            break
        else:
            print('resultCd=%d | recognizedText= %s' 
                  % (response.resultCd, response.recognizedText))
            break

    print ("\n\n인식결과 : %30s " % (resultText))
    return resultText

def main():
    # STT
    KWSID = ['기가지니', '지니야', '친구야', '자기야']
    print ("\n안녕하세요!! BesTwo에 오신 것을 환영합니다!!! \n\n")
    file = open('/home/pi/ai-makers-kit/python3/Text/texttttt.txt', 'w')
    while(1):
        file = open('/home/pi/ai-makers-kit/python3/Text/texttttt.txt', 'a')
        recog = kws.btn_test(KWSID[0])
        if recog == 200:
            text = getVoice2Text()
            file.write(text + ' ' + time.strftime('table number : 1 - %H:%M:%S - %Y-%m-%d', time.localtime(time.time())) + '\n')
        file.close()
        kws.BuzzerOn()
        
        

if __name__ == '__main__':
    main()

