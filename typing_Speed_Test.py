from time import *
import random as r
print(time())

def mistake(par,user):
    error = 0
    for i in range(len(par)):
        try:
            if par[i] != user[i]:
                error += 1
        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_s - time_e
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)


test = ["A Paragraph is a self-contained unit of discourse in wrriting","Welcome to the tryping speed","My name is Bushra Khan"]
test1 = r.choice(test)
print("***** typing speed *****")
print(test1)
print()
print()
time1 = time()
testinput = input("Enter: ")
time2 = time()
print('Speed: ',speed_time(time1,time2,testinput),"w/sec")
print("Error: ",mistake(test1,testinput))