import socket
import platform

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("IP Address:", ip_address)
print("System:", platform.system())
print("Processor:", platform.processor())