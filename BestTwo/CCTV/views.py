from django.shortcuts import render
from django.template import loader
from datetime import datetime
import requests
import cv2
import numpy as np
from django.http import StreamingHttpResponse
import threading
import os
import time

# Create your views here.

PATH = '/home/pi/bestwo/BestTwo/CCTV/templates/resources/images/'
directory = os.getcwd()
filepath = directory + '/resources/'
count = 0

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
            
    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
    
    def take_frame(self):
        now = datetime.now()
        fileName = now.strftime('%y%m%d_%H%M%S')
        cv2.imwrite("/home/pi/bestwo/BestTwo/CCTV/templates/resources/output"+fileName+".png", self.frame)


cam = VideoCamera()

def gen(camera):
    while True:
        frame = cam.get_frame()
        #nowsec=time.strftime('%S', time.localtime(time.time()))
        #print(nowsec)
        #fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #now = datetime.now()
        #fileName = now.strftime('%y%m%d_%H%M%S')
        #video = cv2.VideoWriter("/home/pi/bestwo/BestTwo/CCTV/templates/resources/output"+fileName+".avi", fourcc, 20.0, (640, 480))
        #if nowsec == '00':
        #    video.write(frame)
        cam.take_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
##@gzip.gzip_page
def cctv_stream(request):
    try:
        return StreamingHttpResponse(gen(()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass
    
    ##return render(request,'cctv.html', {})