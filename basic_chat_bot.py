import datetime
import os
name = input("Enter your name: ")
def display_running_time():
        os.system("cls")
        while(1000):
            os.system('cls')
            current_date = datetime.datetime.now()
            print(current_date.time())
            
while(True):


    




    print()
    Avl_ques = ''' 
    ***** Available Questions are*****
    how are you?
    who are you?
    what is ur age?
    what's today date and time?
    which ai based assistant is the best?
    display a running time
    
    '''
    print()
    print(Avl_ques)





    

    question = input("Enter ur query to the basic AI: ")

    if(question.lower() == 'how are you?' ):
        print("I am fine {} \n\t What about you?".format(name))
        inp = input("Are you fine?: ")
        if(inp.lower() == "yes"):
            print(f"Glad to listen to that man!!! {name}")
        else:
            print("No problem \nWinning comes only after some struggles")


    elif(question.lower() == 'who are you?'):
        print(f"{name} This is A basic chat responding AI and I am here to respond to your questions !")

    elif(question.lower() == 'what is ur age?'):
        print(f"{name} I was created by the person Prakash he created me during 8 of the november in 2022")
        year_of_birth = int(input("Enter your year of birth: "))
        current_d_t_y = datetime.datetime.now()
        current_year = current_d_t_y.year
        print(f"Your age might be {current_year - year_of_birth}\n Tell me if i am correct\n ")
        ack = input("Enter 'yes' if i am correct\nEnter 'no' if i am not correct: ")
        ack = ack.lower()
        if(ack == 'yes'):
            print("Thankyou ! I am very glad to answer to ur questions ")
        else:
            print("UFF ! no problem sometimes mistakes makes me perfect as i am learning from myself")
    elif(question.lower() == "what's today date and time?"):
        print(f"Today's Date and time is {datetime.datetime.now()}")
    elif(question.lower() == "which ai based assistant is the best?"):
        print("At present \n Googles 'Google Assistant'\nApples 'Siri'\nAmazons 'Alexa'\nWindows 'COrtona'\nSamsung's 'Bixby' All are trying to do the best\nWe can't say which is better among what\n")
    elif(question.lower() == "display a running time"):
        display_running_time()

        

        

    
        
