print("welcome to your age calculator")
first_num=(input("enter the age you wish to live: \n"))
sec_num=(input("enter your current age: \n"))

first_num= int(first_num)
sec_num= int(sec_num)
if int(first_num == sec_num):
    print("current age and the age you which to live can't be the same")
if int(first_num < sec_num):
    print("current age should not be less than the age you wish to live")
if int(first_num > sec_num):
    print("you have "+str((first_num-sec_num)//10)+" more decade(s) to live")
    print("you have "+str(first_num-sec_num)+" more year(s) to live")
    print("you have "+str((first_num-sec_num)*12)+" more months(s) to live")
    print("you have "+str((first_num-sec_num)*52)+" more week(s) to live")
    print("you have "+str((first_num-sec_num)*365)+" more day(s) to live")
    print("you have "+str((first_num-sec_num)*8760)+" more hour(s) to live")
    print("you have "+str((first_num-sec_num)*525600)+" more minute(s) to live")
    print("you have "+str((first_num-sec_num)*31536000)+" more second(s) to live")

print("thank you for using this app! \n ENJOY THE REST OF YOUR LIFE")
    
