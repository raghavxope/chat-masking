
from __future__ import print_function
    
#encoding tecnique

chara=input("enter a sentence")
print("")

thisdic={
  "a":"apple",
  "b":"bag",
  "c":"carrot",
  "d":"dodge",
  "e":"eat",
  "f":"fat",
  "g":"garbage",
  "h":"hot",
  "i":"ice",
  "j":"jackfruit",
  "k":"k",
  "l":"liquid",
  "m":"man",
  "n":"narcotics",
  "o":"or",
  "p":"paste",
  "q":"quater",
  "r":"rough",
  "s":"sharp",
  "t":"tastes",
  "u":"you",
  "v":"we",
  "x":"no",
  "y":"why",
  "z":"zzzz",
  " ":" "
}
elist=[]
dlist=[]



pos=0

while pos!=len(chara):
    gg=thisdic[chara[pos]]
    elist.append((gg))
    pos=pos+1

for y in elist: print(y, end =" ")
 

#decoding 
print("")
print("decoding")


def get_key(val): 
    for key, value in thisdic.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
   

p=0
while p!=len(elist):
  jj=elist[p]
  dlist.append(get_key(jj))
  p=p+1


for x in dlist:
  print(x, end =" ")
