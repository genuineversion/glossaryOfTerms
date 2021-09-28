# This is a pension fund selector. 
# This is a python code for picking the appropriate pension fund that fits the investors profile

# This list holds the bucket of funds that can be recommended.
fundType=["RSA Fund I", "RSA Fund II", "RSA Fund III", "RSA Fund IV", "RSA Fund V", "RSA Fund VI"]

aboutFund={
    fundType[0]: "It is an aggressive fund with 20% to 75% of your pension funds would be invested in variable income instruments.",
    fundType[1]: "It is a balanced Fund with the intention of capital preservation while pursuing fair returns in the long run. Between 10% and 55% of your pension funds can be invested in variable income instrument",
    fundType[2]: "It is a conservative fund with the primary intention of capital preservation. Between 5% and 20% of your pension funds would be invested in variable income instruments.",
    fundType[3]: "It is an ultra-conservative Fund. Up to 10% of your pension funds can be invested in variable income instruments.",
    fundType[4]: "This fund is designed for active contributors in the informal space such as self -employed individuals.",
    fundType[5]: "This fund is designed for any active contributor who prefers his/her retirement savings to be invested in ethical, non-interest-bearing instruments"
}

#These are set of questions used in the pfs (pension fund selector) function.
qsts= [
    "Are you currently actively working?",
    "Are you in a salaried employment",
    "Do your religious beliefs have influence on the type of investments you can hold?",
    "Are you below 50 years of age?",
    "Will you feel bad and down if you lose just 10% of your invested amount?",
    "What about losing up to 20%, will you feel regret?",
    "If you lose above 20%, will you immediately like to switch to a less risk fund and not to try that same fund in the future?"
]
#These respresent options the users will choose from in response to each set of questions above.
options= [
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"]
]

# This is the function combining the questions and options as well as the logical statement to advise on the fund.
def pfs ():
    qst1=qsts[0] 
    print(qst1)
    response1=input(f"Select:{options[0]} \n")
    
    qst2=qsts[1]  
    print(qst2)
    response2=input(f"Select:{options[1]} \n")

    qst3=qsts[2]  
    print(qst3)
    response3=input(f"Select:{options[2]} \n")

    qst4=qsts[3]  
    print(qst4)
    response4=input(f"Select:{options[3]} \n")

    qst5=qsts[4]  
    print(qst5)
    response5=input(f"Select:{options[4]} \n")

    qst6=qsts[5]  
    print(qst6)
    response6=input(f"Select:{options[5]} \n")

    qst7=qsts[6]  
    print(qst7)
    response7=input(f"Select:{options[6]} \n")


    #determining the apprpriate pension fund based on user's selection. The print statement further combines the fund definition in the output (recommendation)

    if response1=="No":
        print(f"{fundType[3]}: \n{aboutFund[fundType[3]]}")

    elif response2=="No":
        print(f"{fundType[4]}: \n{aboutFund[fundType[4]]}")

    elif response3=="Yes":
        print(f"{fundType[5]}: \n{aboutFund[fundType[5]]}")

    elif response4=="No" and response5=="Yes":
        print(f"{fundType[2]}: \n{aboutFund[fundType[2]]}")

    elif response4=="No" and response5=="No":
        print(f"{fundType[1]}: \n{aboutFund[fundType[1]]}")

    elif response4=="Yes" and response7=="Yes":
        print(f"{fundType[1]}: \n{aboutFund[fundType[1]]}")

    elif response4=="Yes" and response5=="No":
        print(f"{fundType[0]}: \n{aboutFund[fundType[0]]}")

pfs() 
