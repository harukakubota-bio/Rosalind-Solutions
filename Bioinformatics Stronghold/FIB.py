def count_rabbits_pairs(n, k):
    prev2, prev1 = 1, 1
    for _ in range(3, n+1):
        current = prev1 + (k * prev2)
        prev2, prev1 = prev1, current
    return current

if __name__ == "__main__":
    file_path = "Bioinformatics Stronghold/rosalind_fib.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        n, k = map(int, f.read().strip().split())

    result = count_rabbits_pairs(n, k)
    print(result)
