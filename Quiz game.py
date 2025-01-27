print("Welcome to the Quiz!")  


playing = input("Do you want to play the game? (yes/no): ")

# the user's input only

if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()

print("Okay, let's start!")
score = 0
#Question 1
answer = input("What is the brain of Computer? ")
if answer.lower()== "CPU":
    print("Correct")
    score +=1
else:
    print("Wrong")

#Question 2
answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct")
    score +=1
else:
    print("Wrong")

#Question 3
answer = input("Which is the largest search engine? ")
if answer.lower() == "google":
    print("Correct")
    score +=1
else:
    print("Wrong")

#Question 4
answer = input("What is the main function of RAM?")
if answer.lower() == "random access memory":
    print("Correct")
    score +=1
else:
    print("Wrong")

#Question 5
answer = input("CPU stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score +=1
else:
    print("Wrong")

print ("you got "+ str(score) + " Questions Corect!")
print ("you got "+ str((score/5)*100) + "%")