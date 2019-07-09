x7=input()
m=0
for i in range(len(x7)):
 if(x7[i].isdigit() or x7[i].isalpha() or x7[i]==(" ")):
  continue
 else:
  m+=1
print(m)
