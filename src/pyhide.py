from time import strftime as gtime
import random as rand
import string as s

class Hide:

	global offset, PWD
	
	def __init__(self):
		nums = ""
		for n in range(0, 100):
			nums += str(n)
		self.offset = int(int(rand.choice(nums))*10+rand.random())
		while(self.offset >= 100): self.offset-=1
		self.PWD = "REDACTED"
		file = open("dbinfo.txt", "w")
		file.write("Writing commenced at "+gtime("%H:%M:%S"))
		file.close()
    
	def hide(self):
		with open("dbinfo.txt", "w") as file:
			for i in range(0, 100):
				if(i == self.offset):
					print("Offset: {offset}\tPWD: {pwd}".format(offset=self.offset, pwd=self.PWD))
					file.write(self.PWD)
				else:
					string = ""
					for j in range(0,len(self.PWD)-1):
						string += rand.choice(s.letters)
					print(string)
					file.write(string)
				file.write("\n")
        
	def get_offset(self):
		db_info = {}
		file = open("dbinfo.txt", "r")
		i = 0
		line = file.readline()
		while(line != "" and line != "\n"):
			if(i == self.offset):
				db_info[0] = line.rstrip()
				db_info[1] = i
				file.close()
				return db_info
			line = file.readline()
			i += 1
		file.close()
		print("No password stored in db_info.txt")
		return {"error", -1}
    
hider = Hide()
hider.hide()
db_info = hider.get_offset()
print("At offset: {}. Offset = {}".format(db_info[0], db_info[1]))
