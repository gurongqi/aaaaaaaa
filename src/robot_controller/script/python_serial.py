import serial
import time
import sys
ser=serial.Serial('/dev/ttyUSB0',9600)
# while True:
# 	a=int(time.time()*1000)
# 	ser.write(str(a)+'|')
# 	print a
# 	time.sleep(0.02)
# a=''
# for i in range(10):
# 	for j in range(10):
# 		a+=str(j)
# a+='|'
# ser.write(a)
# a='0_500,1_1500,|'
# ser.write(a)
b=0
number=sys.argv[1]
angle=sys.argv[2]
while True:
	if b==0:
		a=number+'_'+angle+',|'
		#a='0_500,1_500,|'
		ser.write(a)
		b=1
	elif b==1:
		a=number+'_'+angle+',|'
		#a='0_1500,1_1500,|'
		ser.write(a)
		b=0
	time.sleep(0.05)
