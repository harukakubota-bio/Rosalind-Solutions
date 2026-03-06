def parse_fasta(file_path):
    fasta_dic = {}
    current_id = ""

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                current_id = line[1:]
                fasta_dic[current_id] = "" 
            else:
                fasta_dic[current_id] += line
    return fasta_dic

def calculate_gc(dna):
    g_count = dna.count("G")
    c_count = dna.count("C")
    gc_count = (g_count + c_count) / len(dna) * 100
    return gc_count

if __name__ == "__main__":
    file_path = "Bioinformatics Stronghold/rosalind_gc.txt"
    fasta_data = parse_fasta(file_path)

    max_id = ""
    max_gc = 0.0
    
    for seq_id, dna in fasta_data.items():
        gc_val = calculate_gc(dna)

        if gc_val > max_gc:
            max_gc = gc_val
            max_id = seq_id

print(max_id)
print(max_gc)

