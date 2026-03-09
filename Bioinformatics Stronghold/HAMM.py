def calculate_hamm_dis(s, t):
    mutation_count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            mutation_count += 1
    return mutation_count

if __name__ == "__main__":
    file_path = "bioinformatics Stronghold/rosalind_hamm.txt"
    with open(file_path, "r",encoding="utf-8") as f:
        lines = f.readlines()
        s = lines[0].strip()
        t = lines[1].strip()

result = calculate_hamm_dis(s, t)
print(result)