import cv2
import time


def delay(delay_time):
    timeout = delay_time   # [seconds]
    timeout_start = time.time()
    print(time.strftime("%c"))
    while time.time() < timeout_start + timeout:
        test = 0
        if test == 3:
            break
            test -= 1
    print(time.strftime("%c"))


def videoCapture(vidName):
    time_start = time.time()
    cap = cv2.VideoCapture(0)
    if (cap.isOpened() == False):
        print("Unable to read camera feed")
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    print('Recording ' + vidName)
    out = cv2.VideoWriter(vidName,
        cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (frame_width, frame_height))

    while time.time() < time_start + closing_time:
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            #cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    print('Recording complete')
    cap.release()
    out.release()


print(time.strftime("%c"))
closing_time = 10
counter = 0
while True:
    videoCapture('vid'+str(counter)+'.mkv')
    counter += 1


# this loop is here because sometimes cv2 has problems destroying windows
# if you call it once. so to be safe I call it 10 times
for _ in range(10):
    cv2.destroyAllWindows()
