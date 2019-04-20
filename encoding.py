#encoding tecnique

chara=raw_input("enter a sentence")

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
print(elist)
dlist=list(elist)
#decoding 

print("decoding")

def get_key(val): 
    for key, value in thisdic.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
    
p=0


while p!=len(dlist):
  jj=dlist[p]
  hh=get_key(jj)
  dlist.append(hh)
  p=p+1

for x in dlist:
  print(x)




