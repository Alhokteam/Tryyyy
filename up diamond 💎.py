import os, sys
import socket
import re, select
import time, threading

lvl = None

like = None

lvlnew = None

#Tele@MinhDataa

SOCKS_VERSION = 5


# 76, 84 | Lvl = True | LT

#[👑FF0000]Thành Miinh
print("Tool có những chức năng cày level team5 kc ảo")
print("Nghi /lvl để dùng cày lv /5 để dùng team5 /kc để dùng kc ảo")
print("Mua Tool Ib Tele@MinhDataa")
print("Mua Tool Ib Zalo 0337641745")


DataSquad = None

def gen_squad(clisocks, packet: str):
	header = packet[0:62]
	lastpacket = packet[64:]
	squadcount = "04"
	
	NewSquadData = header + squadcount + lastpacket
	clisocks.send(bytes.fromhex(NewSquadData))

def gen_msg(packet, content):
	content = content.encode("utf-8")
	content = content.hex()
	
	header = packet[0:8]
	packetLength = packet[8:10]
	packetBody = packet[10:32]
	pyloadbodyLength = packet[32:34]
	pyloadbody2 = packet[34:62]
	pyloadlength = packet[62:64]
	
	pyloadtext= re.findall(r"{}(.*?)28".format(pyloadlength) , packet[50:])[0]
	pyloadTile = packet[int(int(len(pyloadtext))+64):]
	
	NewTextLength = (hex((int(f"0x{pyloadlength}", 16) - int(len(pyloadtext)//2) ) + int(len(content)//2))[2:])
	if len(NewTextLength) == 1:
		NewTextLength = "0"+str(NewTextLength)
	
	NewpaketLength = hex(((int(f"0x{packetLength}", 16) - int((len(pyloadtext))//2) ) ) + int(len(content)//2) )[2:]
	NewPyloadLength = hex(((int(f"0x{pyloadbodyLength}", 16) - int(len(pyloadtext)//2)))+ int(len(content)//2) )[2:]
	NewMsgPacket = header + NewpaketLength + packetBody + NewPyloadLength + pyloadbody2 + NewTextLength + content + pyloadTile
	return str(NewMsgPacket)
	
def gen_msgv2(packet , replay):

	replay = replay.encode('utf-8')
	replay = replay.hex()
	
	
	hedar = packet[0:8]
	packetLength = packet[8:10] #
	paketBody = packet[10:32]
	pyloadbodyLength = packet[32:34]
	pyloadbody2= packet[34:60]
	
	pyloadlength = packet[60:62]
	pyloadtext= re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
	pyloadTile = packet[int(int(len(pyloadtext))+62):]
	
	
	NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
	if len(NewTextLength) == 1:
		NewTextLength = "0"+str(NewTextLength)
	
	NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
	NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)))+ int(len(replay)//2) )[2:]
	
	finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile
	
	return str(finallyPacket)
	
def send_msg(sock, packet, content, delay:int):
	time.sleep(delay)
	try:
		sock.send(bytes.fromhex(gen_msg(packet, content)))
		sock.send(bytes.fromhex(gen_msgv2(packet, content)))
	except Exception as e:
		print(e)
		pass

# [ LVL UP VAR ]
Listt = []
Increase = False
IsStarted = False
StartData = None
ServerSocket = None
StopData = b'\x03\x15\x00\x00\x00\x10\t\x1e\xb7N\xef9\xb7WN5\x96\x02\xb0g\x0c\xa8'


# [ LVL UP DEF ]
def timesleep():
	time.sleep(27)
	if IsStarted == True:
		ServerSocket.send(StartData)
		
def enter_game_and_RM():
	global Listt
	for data in Listt:
		MainC.send(data)
		Listt.remove(data)
	time.sleep(6)
	IStarted = False
	ServerSocket.send(StartData)
	t = threading.Thread(target=timesleep, args=()).start()

def break_the_matchmaking(server):
	server.send(StopData)
	server.send(StopData)
	server.send(StopData)
	t = threading.Thread(target=enter_game_and_RM, args=()).start()

#[👑FF0000]Thành Miinh

class Proxy:
	
	def __init__(self):
		self.username = "Alhok"
		self.password = "Alhok"
		self.packet = b''
		self.sendmode = 'client-0-'
		
	def handle_client(self, connection):
		global Increase, SpamMsg
		version, nmethods = connection.recv(2)
		#print(version)
		#print(nmethods)
		if version == 76 and nmethods == 84:
			Increase = True
		if version == 76 and nmethods == 70:
			Increase = False
		if version == 77 and nmethods == 84:
			SpamMsg = True
			print("Spam Msg: On")
		if version == 77 and nmethods == 70:
			SpamMsg = False
			print("Spam Msg: Off")
		else:
			methods = self.get_available_methods(nmethods, connection)
			if 2 in set(methods):
				connection.sendall(bytes([SOCKS_VERSION, 2]))
			else:
				connection.sendall(bytes([SOCKS_VERSION, 0]))
				
			if not self.verify_credentials(connection,methods):
				return
			try:
				version, cmd, _, address_type = connection.recv(4)
				
				if address_type == 1:
					address = socket.inet_ntoa(connection.recv(4))
				elif address_type == 3:
					domain_length = connection.recv(1)[0]
					address = connection.recv(domain_length)
					address = socket.gethostbyname(address)
					name= socket.gethostname()
					
					
				port = int.from_bytes(connection.recv(2), 'big', signed=False)
				port2 = port
				
				try:
					
					remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					remote.connect((address, port))
					
					print("* Connected to {} {}".format(address, port))
					bind_address = remote.getsockname()
					
					addr = int.from_bytes(socket.inet_aton(bind_address[0]), 'big', signed=False)
					port = bind_address[1]
					reply = b''.join([
						SOCKS_VERSION.to_bytes(1, 'big'),
						int(0).to_bytes(1, 'big'),
						int(0).to_bytes(1, 'big'),
						int(1).to_bytes(1, 'big'),
						addr.to_bytes(4, 'big'),
						port.to_bytes(2, 'big')
					])
				except Exception as e:
					reply = self.generate_failed_reply(address_type, 5)
					
				connection.sendall(reply)
				
				self.botdev(connection, remote,port2)
			except:
				pass
		
	def generate_failed_reply(self, address_type, error_number):
		return b''.join([
			SOCKS_VERSION.to_bytes(1, 'big'),
			error_number.to_bytes(1, 'big'),
			int(0).to_bytes(1, 'big'),
			address_type.to_bytes(1, 'big'),
			int(0).to_bytes(4, 'big'),
			int(0).to_bytes(4, 'big')
		])
		
	def verify_credentials(self, connection,methods):
		
		if 2 in methods:
			version = ord(connection.recv(1))
			
			username_len = ord(connection.recv(1))
			username = connection.recv(username_len).decode('utf-8')
			
			password_len = ord(connection.recv(1))
			password = connection.recv(password_len).decode('utf-8')
			# print(username,password)
			if username == self.username and password == self.password:
				
				response = bytes([version, 0])
				connection.sendall(response)
				return True
				
			response = bytes([version, 0])
			connection.sendall(response)
			return True
			
		else:
			version = 1
			response = bytes([version, 0])
			try:
				connection.sendall(response)
			except BrokenPipeError:
				pass
			return True
			
	def get_available_methods(self, nmethods, connection):
		methods = []
		for i in range(nmethods):
			try:
				methods.append(ord(connection.recv(1)))
			except:
				pass
		return methods
		
	def runs(self, host, port):
		try:
			var = 0
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind((host, port))
			s.listen()
			while True:
				var = var+1
				conn, addr = s.accept()
				t = threading.Thread(target=self.handle_client, args=(conn,))
				t.start()
				
					
		except Exception as e:
			print(e)
			
	#connect
	def botdev(self, client, remote, port):
		while True:
			r, w, e = select.select([client, remote], [], [])
			if client in r or remote in r:
				if client in r:
					global MainC, MainS, DataSquad
					global StartData, ServerSocket, Increase, IsStarted, Listt
					dataC = client.recv(10822)
					if port == 39699:
						MainC = client
						MainS = remote
					if "0301" in dataC.hex()[0:4] and len(dataC.hex()) >= 800:
						StartData = dataC
						ServerSocket = remote
						t = threading.Thread(target=timesleep, args=()).start()
						
					if remote.send(dataC) <= 0:
						break

				if remote in r:
					dataS = remote.recv(10822)
					# [ Start LevelUp ]
					if "0300" in dataS.hex()[0:4]:
						if b"Ranked Mode" in dataS:
							pass
						else:
							if len(dataS.hex()) <= 100:
								pass
							else:
								if Increase == True:
									Istarted = True
									Listt.append(dataS)
									t = threading.Thread(target=break_the_matchmaking, args=(ServerSocket,)).start()
								else:
									client.send(dataS)
					# [ End LevelUp ]
			
					
					if "1200" in dataS.hex()[0:4] and b"/hok" in dataS:
						MainC.send(bytes.fromhex("080000001608edaae28710100820022a0a08e7be0110b24f18c801"))
						
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[b][c][00FFFF]تـــم أضافــة الجــواهر  ✓", 0.2)).start()
						time.sleep(1)
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[b][c][FF00FF]  10.162 جوهرة", 0.4)).start()
						time.sleep(1)
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[b][c][FFFF00]Instagram : hok_ _f", 0.3)).start()
						time.sleep(1)
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[b][c][FF0000] by Alhok team (Nmr)", 0.4)).start()
						time.sleep(1)
  

						
				

           
						
					if client.send(dataS) <= 0:
						break


def vrxxbot():
	Proxy().runs('127.0.0.1', 7777)
		
vrxxbot() #Telegram @MinhData