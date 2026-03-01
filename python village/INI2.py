file_path = "rosalind_ini2.txt"
with open(file_path, "r") as f:
    line = f.read().strip()
    a, b = map(int, line.split())

result = a**2 + b**2
print(result)

