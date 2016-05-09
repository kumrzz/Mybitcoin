import struct
import time
import random
import hashlib
import socket
import os

#below edited(coz I am in testnet) per windows command:
# C:\Progra~1\Bitcoin\daemon\bitcoin-cli getpeerinfo
version = struct.pack("L", 70002)

services = struct.pack("Q", 0)

timestamp = struct.pack("Q", time.time())

addr_recv_services = struct.pack("Q", 0) #services

addr_recv_ip = struct.pack(">16s", "127.0.0.1")

#below edited from 8333(coz I am in testnet)
addr_recv_port = struct.pack(">H", 18333)

addr_trans_services = struct.pack("Q", 0) #services

addr_trans_ip = struct.pack(">16s", "127.0.0.1")

#below edited from 8333(coz I am in testnet)
addr_trans_port = struct.pack(">H", 18333)

nonce = struct.pack("Q", random.getrandbits(64))

#not updating agent as this is fine @ zero
user_agent_bytes = struct.pack("B", 0)

#below edited(coz I am in testnet) per windows command:
# C:\Progra~1\Bitcoin\daemon\bitcoin-cli getpeerinfo
starting_height = struct.pack("L", 827541)

relay = struct.pack("?", False)

payload = version + services + timestamp + addr_recv_services + addr_recv_ip + addr_recv_port + addr_trans_services + addr_trans_ip + addr_trans_port + nonce + user_agent_bytes + starting_height + relay

#magic = "F9BEB4D9".decode("hex") coz I am in testnet:
magic = "0B110907".decode("hex")

command = "version" + 5 * "\00"

length = struct.pack("L", len(payload))

check = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]

msg = magic + command + length + check + payload

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#below two edited(coz I am in testnet) per windows command:
# C:\Progra~1\Bitcoin\daemon\bitcoin-cli getpeerinfo
HOST = "137.116.160.176"
PORT = 18333

s.connect((HOST, PORT))

s.send(msg)

s.recv(1024)
