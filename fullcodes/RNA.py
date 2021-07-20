seqs=["UUCGCCGACUGA","AUGCCUUGA","AUGCGGUGAUAA"]
for seq in seqs:
    print(seq)
    if seq.startswith("AUG"):
        print("Has start codon")
    if seq.count("UGA")>=0 and not seq.endswith("UGA"):
        print("Has selenocysteine")