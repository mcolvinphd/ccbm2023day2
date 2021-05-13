##seqs=["UUCGCCGACUGA","AUGCCUUGA","AUGCGGUGAUAA"]
##for seq in seqs:
##    print(seq)
##    if seq.startswith("AUG"):
##        print("Has start codon")
##    if seq.count("UGA")>=0 and not seq.endswith("UGA"):
##        print("Has selenocysteine")



s=input("Enter DNA string")
comp={"G":"C","C":"G","A":"T","T":"A"}
slist=list(s)
rs=""
for i in slist:
  rs=comp[i]+rs
if rs==s:
    print("DNA palindrome")
else:
    print("Not DNA palindrome")
