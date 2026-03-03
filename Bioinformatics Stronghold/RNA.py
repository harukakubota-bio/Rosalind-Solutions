file_path = "Bioinformatics Stronghold/rosalind_rna.txt"
with open(file_path, "r") as f:
    dna = f.read().strip()
    print(dna.replace("T", "U"))