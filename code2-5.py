#-*- coding: UTF-8 -*- 

# enter integer variable from a user
seconds = eval(input("input the nubmer [seconds]: "))

# get the values of the minutes and seconds
minutes = seconds // 60
remainingSeconds = seconds % 60

# show the result
print("About input sconds, ", seconds,"[sec], ==> minutes,", minutes, \
	"[minutes],", remainingSeconds,"[seconds]")
