def calculate_dominat_probability(k, m, n):
    total = k + m + n
    prob_mm = (m / total)* ((m-1) / (total-1)) * 0.25
    prob_mn = (m / total)* (n / (total - 1)) * 2 * 0.5
    prob_nn = (n / total)* ((n-1) / (total - 1)) *1.0

    prob_recessive = prob_mm + prob_mn + prob_nn
    return 1 - prob_recessive

if __name__ == "__main__":
    file_path = "Bioinformatics Stronghold/rosalind_iprb.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        k, m, n = map(int, f.read().strip().split())

    result = calculate_dominat_probability(k, m, n)
    print(f"{result:4f}")
