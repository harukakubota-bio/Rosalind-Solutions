file_path = "Bioinformatics Stronghold/rosalind_dna.txt"
with open(file_path, "r") as f:
    dna = f.read().strip()

print(f"{dna.count("A")} {dna.count("C")} {dna.count("G")} {dna.count("T")}")