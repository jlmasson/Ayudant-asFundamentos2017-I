import random
import string

def pickword(x):
        a=0
        a=open(x, "r").readlines()
        a=a[random.randint(0,len(a))]
        a=list(a.strip().upper())
        return a

def start(x):
        y=[]
        for i in x:
                y.append("0")
        return y

def letter():
        x= input("\nWhat is your guess?: ")
        while x not in string.ascii_letters:
                x= input("Please chose just a letter: ")
        return x.upper()

def checkguess(guess,word,state,pastletters,tries):
        if guess not in word:
                pastletters.append(guess)
                tries+=1
        else:
                for i in range(len(word)):
                        if guess==word[i]:
                                del state[i]
                                state.insert(i,guess)
        return state, pastletters, tries

def checkend(state):
        x=0
        if "0" not in state:
                x=1
        return x
        
def makestate(x,pastletters):
        print(" ")
        for i in range(len(x)):
                if x[i]=="0":
                        print("__",end=" ")
                else:
                        print(" "+x[i]+" ",end=" ")
        print("\n")
        print("your previous wrong guesses: "+ str(list(pastletters)))

def hangman(tries):
        if tries>0:
                print("| ¬ ")
        if tries>6:
                print("|  ! ")
        if tries>1:
                print("| O ")
        if tries==2:
                print("| T")
        if tries ==3:
                print("|/T")
        if tries >3:
                print("|/T\ ")
        if tries ==5:
                print("|/ ")
        if tries ==6:
                print("|/  \ ")
        if tries ==7:
                print("  /  \ ")
                      
word=pickword("ex30.txt")
state=start(word)
end=0
tries=0
again="yes"
pastletters=[]

while again in["yes", "Yes", "y"]:
        while end == 0 and tries<7:
                guess=letter()
                temp=checkguess(guess,word,state,pastletters,tries)
                state=temp[0]
                pastletters=temp[1]
                tries=temp[2]
                makestate(state,pastletters)
                end=checkend(state)
                hangman(tries)
                ##if end ==0:
                        ##print("You have made "+str(tries)+" wrong guesses")
        if tries ==7:
                print("\nOops, you failed this time !")
        else:
                print("\nCongrats, you found the word!")
        again=input("\nWant to play again?: ")
        if again in["yes", "Yes", "y"]:
                end = 0
                word=pickword("ex30.txt")
                state=start(word)
                tries=0
                pastletters=[]
