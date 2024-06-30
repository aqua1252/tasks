string1="幸gbky福jd"

string= list(string1)
print(string)
chars=[]
charindex=[]

def append1(str1,i):
    chars.append(string[i])
    charindex.append(i)
    
def pop1(i):
    string.pop(i)  
    
def isascii(string):
    for i in range(len(string)):
        if ord(string[i]) > 128:
            append1(string[i],i)
            pop1(i)
            
isascii(string)            
string=string[::-1]
for i in range(0,len(charindex)):
    string.insert(charindex[i],chars[i])
print(string)    