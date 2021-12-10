

ty= input("")
listn=input("")

mylist=[int(n) for n in listn.split()]



a = {}
for i in mylist:
  if mylist.count(i)==1:
    a[i] = mylist.count(i)

print(len(a))
