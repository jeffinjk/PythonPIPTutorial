f=open("text.txt",'r')
text=f.read()
dic={}
for i in text:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
        
print(text) 
print(dic)       