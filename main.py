from email.mime import audio
import pyttsx3
import speech_recognition as sr
import controller as cnt
import cv2
import mediapipe as mp
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello I'm  your assistance. How may I help you?" )

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        audio=r.listen(source)
        try:
            print("Reconized........")
            query=r.recognize_google(audio, language='en-in')
        except Exception as e:
            print("Sorry! Something went wrong. Please try Again.")
            return "none"
        return query
def number():
    time.sleep(2.0)

    mp_draw=mp.solutions.drawing_utils
    mp_hand=mp.solutions.hands


    tipIds=[4,8,12,16,20]

    video=cv2.VideoCapture(0)

    with mp_hand.Hands(min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as hands:
        while True:
            ret,image=video.read()
            image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable=False
            results=hands.process(image)
            image.flags.writeable=True
            image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            lmList=[]
            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                    myHands=results.multi_hand_landmarks[0]
                    for id, lm in enumerate(myHands.landmark):
                        h,w,c=image.shape
                        cx,cy= int(lm.x*w), int(lm.y*h)
                        lmList.append([id,cx,cy])
                    mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
            fingers=[]
            if len(lmList)!=0:
                if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1,5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                total=fingers.count(1)
                cnt.led_number(total)
                if total==0:
                    #video.release()
                    #cv2.destroyAllWindows()
                    #main_controll()
                    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, "0", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                    cv2.putText(image, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                elif total==1:
                    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, "1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                    cv2.putText(image, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                elif total==2:
                    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, "2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                    cv2.putText(image, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                elif total==3:
                    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, "3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                    cv2.putText(image, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                elif total==4:
                    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, "4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                    cv2.putText(image, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                elif total==5:
                    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, "5", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                    cv2.putText(image, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                

            cv2.imshow("Frame",image)
            k=cv2.waitKey(1)
            if k==ord('q'):
                break
    video.release()
    cv2.destroyAllWindows()
def main_controll():
    while True:
        
        query=takeCommand().lower()

        if 'blue' in query:
            print("Blue LED on........")
            speak("Bule Led is on.......")
            cnt.led('b')
        
        elif 'yellow' in query:
            print("Yellow LED on........")
            speak("Yellow Led is on.......")
            cnt.led('y')
        
        elif 'green' in query:
            print("Green LED on........")
            speak("Green Led is on.......")
            cnt.led('g')
        
        elif 'red' in query:
            print("Red LED on........")
            speak("Red Led is on.......")
            cnt.led('r')
        
        elif 'white' in query:
            print("White LED on........")
            speak("White Led is on.......")
            cnt.led('w')
        
        elif 'light on' in query:
            print("all LED on........")
            speak("all Led is on.......")
            cnt.led('a')
        elif 'video' in query:
            print("Video is on.......")
            speak("Video is on.......")
            number()
        
        elif 'off' in query:
            print("Light off........")
            speak("all Lights are off.......")
            cnt.led(0)
        if 'exit' in query:
            print("exit.")
            cnt.led("e")
            speak("My job is done. Bye")
            break

if __name__=="__main__":
    main_controll()