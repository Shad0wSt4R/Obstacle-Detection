import numpy as np
import cv2
from keras.models import Sequential
from keras.layers import Dense, Activation

def deskew(img):
    m = cv2.imread(img, 0)
    print(m)
    if abs(m['mu02']) < 1e-2:
        # no deskewing needed. 
        return img.copy()
    # Calculate skew based on central momemts. 
    skew = m['mu11']/m['mu02']
    # Calculate affine transform to correct skewness. 
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
    # Apply affine transform
    img = cv2.warpAffine(img, M, (SZ, SZ), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    return img

def Hog():
    winSize = (20,20)
    blockSize = (10,10)
    blockStride = (5,5)
    cellSize = (10,10)
    nbins = 9
    derivAperture = 1
    winSigma = -1.
    histogramNormType = 0
    L2HysThreshold = 0.2
    gammaCorrection = 1
    nlevels = 64
    useSignedGradients = True

    return cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels, useSignedGradients)

def training():
    PATH_TO_LABELS = "training/label_2/"
    PATH_TO_IMAGES = "training/image_2/"
    ARRSIZE=7481
    labels=[]
    images=[]

    print("Filling arrays...")

    # Fills an array of filenames to labels
    for i in range(ARRSIZE):
        if(i < 10):
            labels.append("00000" + str(i) + ".txt")

        elif(i >= 10 and i < 100):
            labels.append("0000" + str(i) + ".txt")

        elif(i >= 100 and i < 1000):
            labels.append("000" + str(i) + ".txt")

        else:
            labels.append("00" + str(i) + ".txt")

        # Fills an array full of image filenames
    for i in range(ARRSIZE):
        if(i < 10):
            images.append("00000" + str(i) + ".png")

        elif(i >= 10 and i < 100):
            images.append("0000" + str(i) + ".png")

        elif(i >= 100 and i < 1000):
            images.append("000" + str(i) + ".png")

        else:
            images.append("00" + str(i) + ".png")

    # We will be using a Support Vector Machine for training
    svm = cv2.ml.SVM_create()
    svm.setType(cv2.ml.SVM_C_SVC)
    svm.setKernel(cv2.ml.SVM_RBF)

    # image preprocessing
    processed_img = np.array(ARRSIZE)
    hog_img = np.array(ARRSIZE)
    hog = Hog()

    # Processes the images through a deskewing function
    for i in images:
        np.append(processed_img, deskew(i))

    # Applies the HOG descriptor
    for i in processed_img:
        np.append(hog_img, hog.compute(i))

    #training
    svm.trainAuto(hog_img, cv2.ml.ROW_SAMPLE, svmResp, 10, svm.getDefaultGridPtr(0), svm.getDefaultGridPtr(1), 0, 0, 0, 0, False)

    svm.save("digits_svm_model.yml")

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
