# This is a mutual fund selector advisor. 
# This is a python code for advising on the most appropriate fund that fits the investors profile

# This list holds the bucket of funds that can be recommended.
fundType=["Money Market Fund", "Fixed Income Fund", "Equity Fund", "Balanced Fund", "Ethical Fund"]

#These are set of questions used in the fsa (fund selection advisor) function.
qsts= [
    "Do your religious beliefs have influence on the type of investments you can hold?",
    "Are you below 50 years of age?",
    "Are you employed or self-employed",
    "Will you feel bad and down if you lose just 10% of your invested amount?",
    "What about losing up to 20%, will you feel regret?",
    "If you lose above 20%, will you cease to try that investment in the future?",
    "How long do you intend holding your investment?"
]
#These respresent options the users will choose from in response to each set of questions above.
options= [
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"],
    ["a: a year or less", "b: btw one to two years", "c: above two years"]
]

# This is the function combining the questions and options as well as the logical statement to advise on the fund.
def fsa ():
    qst1=qsts[0] 
    print(qst1)
    response1=input(f"Select :{options[0]} \n")
    
    qst2=qsts[1]  
    print(qst2)
    response2=input(f"Select :{options[1]} \n")

    qst3=qsts[2]  
    print(qst3)
    response3=input(f"Select :{options[2]} \n")

    qst4=qsts[3]  
    print(qst4)
    response4=input(f"Select :{options[3]} \n")

    qst5=qsts[4]  
    print(qst5)
    response5=input(f"Select :{options[4]} \n")

    qst6=qsts[5]  
    print(qst6)
    response6=input(f"Select :{options[5]} \n")

    qst7=qsts[6]  
    print(qst7)
    response7=input(f"Select :{options[6]} \n")


    #determining the apprpriate fund based on user's selection

    if response1=="Yes":
        print(fundType[4])
    elif response2=="No" or response3=="No" or response7=="a":
        print(fundType[0])
    elif response4=="Yes":
        print(fundType[0])
    elif response4=="No" and response7=="a":
        print(fundType[0])
    elif response4=="No" and response7=="b":
        print(fundType[1])
    elif response4=="No" and response5=="Yes" and (response7=="b" or response7=="c"):
        print(fundType[1])

    elif response4=="No" and response5=="No" and response6=="Yes" and (response7=="b" or response7=="c"):
        print(fundType[3])

    elif response4=="No" and response5=="No" and response6=="No" and response7=="b":
        print(fundType[3])

    elif response4=="No" and response5=="No" and response6=="No" and response7=="c":
        print(fundType[2])

    


fsa() 
