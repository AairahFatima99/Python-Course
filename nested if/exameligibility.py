#take input for the student that he can atted the exam or not
medical_cause=input("did you have a medical cause Y or N: ")
#Take input of the attendence
atten = int(input("enter the attendence of the student: "))

#checking the user input predicting oyput accordingly

if medical_cause == 'Y' : #checking the condition 1
    print ("You are allowed")
else:
    if atten>= 75: #checking the condition 2
        print ("Allowed")
    else:
        print ("Not allowed")