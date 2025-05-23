t=open("text.txt","r")
s=t.read()
words=s.split()
wcount=len(words)
no_sentance=0
no_syllable=0
for char in s:
    if char in [".", "?", "!", ":", ";"]:
        no_sentance+=1
    if char.lower() in ["a", "e", "i", "o", "u","A","E","I","O","U"]:
        no_syllable+=1
F=206.835-1.015*(wcount/no_sentance)-84.6*(no_syllable/wcount)
G=0.39*(wcount/no_sentance)+11.8*(no_syllable/wcount)-15.59
print("F: ",F)
print("G: ",G)
if G>=0 and G<=30:
    print("College level ")
elif G>=50 and G<=60:
    print("School level ")        
elif G>=90 and G<=100:
    print("4th grade ")