file_path = "python village/rosalind_ini4.txt"
with open(file_path, "r") as f:
    line = f.read().strip()
    a, b = map(int, line.split())

sum = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        sum += i
    
print(sum)