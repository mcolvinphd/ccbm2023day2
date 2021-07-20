s=input("Enter DNA string ")
comp={"G":"C","C":"G","A":"T","T":"A"}
slist=list(s)
rs=""
for i in slist:
  rs=comp[i]+rs
if rs==s:
    print("DNA palindrome")
else:
    print("Not DNA palindrome")