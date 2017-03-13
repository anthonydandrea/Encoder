import sys

CHAR_STRING = " \t\n\"\\abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^&*()_-+={[}]|:;'<,>.?/" 

dict1 = dict()
dict2 = dict()

digit1 = 0
digit2 = 0
digit3 = 0

for char in CHAR_STRING:

    dict1[char] = str(digit1)+str(digit2)+str(digit3);
    dict2[str(digit1)+str(digit2)+str(digit3)] = char

    digit3+=1

    if digit3 == 10:
        digit2+=1
        digit3=0

    if digit2 == 10:
        digit1 +=1
        digit2 = 0
    
    

class Encoder():
    def __init__(self,t=None,d=None,a=None):
        self.tree = t
        self.dict = d
        self.altdict = a

    def encode(self,F,key=1):
        newFile = open("encodedFile.txt",'w')
        FILE = open(F,'r')
        for line in FILE:
            for char in line:
                if not char in self.dict:
                    print("char",char," not found")
                else:
                    newFile.write(self.dict[char])

    def decode(self,F,key=1):
        newFile = open("decodedFile.txt",'w')
        FILE = open(F,'r')
        for line in FILE:
            for index in range(0,len(line),3):
                if not line[index:index+3] in self.altdict:
                    print('Encoded char @',line[index:index+3],'not found.')
                else:
                    newFile.write(self.altdict[line[index:index+3]])


files = sys.argv

def OpenFile():
    if len(files) != 2:
        print("Incorrect argument number given")
        return False

    try:
        open(files[1],"r")
        return True
    except IOError:
        print("Cannot open requested file")
        return False

enc = Encoder(None,dict1,dict2)

