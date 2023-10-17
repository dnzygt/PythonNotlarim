import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        print("Son",time_sec,"...")
        if time_sec == 1:
            time.sleep(1)
            print("Kalk Okul Var!!!")
            break

countdown(6)
