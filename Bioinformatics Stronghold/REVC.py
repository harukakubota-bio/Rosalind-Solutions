file_path = "Bioinformatics Stronghold/rosalind_revc.txt"
with open(file_path, "r") as f:
    dna = f.read().strip()
    complement_dic = {"A":"T", "T":"A", "G":"C", "C":"G"}
    complement_dna = ""

    for base in dna:
        complement_dna += complement_dic[base]

    revers = complement_dna[::-1]
    print(revers)