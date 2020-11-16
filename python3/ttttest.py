import time
while True:
    print(time.strftime('%2M:%2S', time.localtime(time.time())))
    time.sleep(1)
    if '00'==time.strftime('%S', time.localtime(time.time())) or '30'==time.strftime('%S', time.localtime(time.time())):
        print('!!!!!!!!!!!!!!!!!!!!!'+time.strftime('%2H:%2M:%2S', time.localtime(time.time())))
