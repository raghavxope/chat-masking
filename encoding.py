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



pos=0

while pos!=len(chara):
    gg=thisdic[chara[pos]]
    elist.append((gg))
    pos=pos+1
print(elist)




