
#This programs create an Unsecure i.e. HTTP Socket connection with server and fetches the text mentioned text file on the server 
#its not at all a robust option but simply a short implementation of sockets for quick access to https site 

#importing socket
import socket
#importing regex
import re

#Creating a Socket object 
try :
	My_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as er:
	print(str(er))
	quit()


#Taking Http URL from user
URL = input('Enter http url path of your text file\n')
if URL.startswith('http://'):
	Host = re.findall('http://(\S+)/', URL)
	print(Host)
	Hostname = Host[0]
	Port = 80

#Creating a Socket connection 
try :
	My_Sock.connect((Hostname,Port))
	print('Connected Succesfully\n')
except Exception as er:
	print(str(er))
	print('Connection Failed\n')
	quit()

#Getiing Directory from user to save file
User_File = input('Kindly Enter Directory to store file\n')
File_Name = f'{User_File.strip()}/{Hostname.strip()}.txt'
print('Writing to',File_Name,'\n')

#Creating GET request command 
#This is equal to GET http://data.pr4e.org/mbox.txt with protocol HTTP/1.0 "Enter Enter" just like GET from telnet
try :
	cmd = f'GET {URL} HTTP/1.0\r\n\r\n'.encode() #By Deafult encodes to "UTF-8"
except Exception as er:
	print(str(er))
	print('GET Command Failed\n')
	quit()

#Sending the request to Host
My_Sock.send(cmd)

#writing to file
file = open(File_Name,'w+')

#receiving response untill its empty 
#Note that \n or new line also has a length of 1
while True:
	#Receiving 1024 bytes at a time from the socket
	#also decoding the same in unicode
	
	try :
		message = My_Sock.recv(1024).decode()
	except Exception as er:
		print(str(er))
		print('Cannot receive message\n')
		quit()

	if len(message)<1:
		print('----------------------------------------------EOL----------------------------------------------------')
		break

	file.write(message)

print('Data fetched Succesfully\n')
#closing connection
My_Sock.close()



