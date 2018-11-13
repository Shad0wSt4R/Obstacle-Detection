import numpy as np
import cv2
#import keras
#from keras import backend as K


def training():
    labels=[]

    # Fills an array of filenames to labels
    for i in range(7481):
        #print(i)
        if(i < 10):
            labels.append("00000" + str(i) + ".txt")
            print(labels[i])

        elif(i >= 10 and i < 100):
            labels.append("0000" + str(i) + ".txt")
            print(labels[i])

        elif(i >= 100 and i < 1000):
            labels.append("000" + str(i) + ".txt")
            print(labels[i])

        else:
            labels.append("00" + str(i) + ".txt")
            print(labels[i])


def testing():
    cap = cv2.VideoCapture('driving_vids/Downtown.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()

        # Makes the video grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Shows grayscaled video
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    print("Welcome to the Obstacle Detection Program!\n")
    choice = input("What you you like to do?\n\n1) Train\n2) Test\n\n>>")

    if(choice == "1"):
        training()
    
    elif(choice == "2"):
        testing()
    
    else:
        print("Invalid choice")


main()
