import keras
from keras.models import Sequential

def training():
    model = Sequential()

def testing():

def main():
    print("Welcome to the image recognition program. What would you like to do?\n"+
            "1. Train\n" +
            "2. Test\n\n")
    choice = input(">>")

    if(choice == 1):
        training()
    elif(choice == 2):
        testing()
    else:
        print("Invalid input!")

main()
