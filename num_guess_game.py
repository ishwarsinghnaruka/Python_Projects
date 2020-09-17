import numpy as np
num_u = int(input("Guess a number"))
num_c = np.random.randint(1,100)
user_score = 50
while user_score>0:
    if num_c==num_u:
        print("U guess it right")
        print("Your Score is {}".format(user_score))
        break
    else:
        if num_c%5==0:
            print("number is divisible by 5")
        if num_c%2==0:
            print("Hint:num_c is even number")
        if num_c%2!=0:
            print("HINT:number is odd number")
        if abs(num_c-num_u)<10:
            print("HINT:number is between {} and {}".format(num_u-10,num_u+10))
        if len(str(num_c))==2:
            print("HINT:number is 2 digit number")
        if num_c<50:
            print("HINT:number is between 0 and 50")
        if num_c>50:
            print("HINT:number is between 50 and 100")
        user_score=user_score-10
        print("your Score is {}".format(user_score))
        num_u = int(input("Guess Again :"))
print("number is {}".format(num_c))