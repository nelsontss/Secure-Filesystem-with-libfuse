from cryptography.fernet import Fernet
key = Fernet.generate_key()

for i in range(1,16):
	f = Fernet(key)
	file = open("Teste/teste"+str(i),"rb")
	encrypted = f.encrypt(file.read())
	file.close()

	file = open("Teste/teste"+str(i), "wb")
	file.write(encrypted)

	file.close();