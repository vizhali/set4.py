stng4=input()
bob=0
for z in range(len(stng4)):
  if(stng4[z].isdigit() or stng4[z].isalpha() or stng4[z]==(" ")):
    continue
  else:
   bob+=1
print(bob)
