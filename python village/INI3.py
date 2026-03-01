file_path = r"C:\Users\kuboh\Downloads\rosalind_ini3.txt"
with open(file_path, "r") as f:
     lines = f.readlines()
     s = lines[0].strip()
     a, b, c, d = map(int, lines[1].split())
word1 = s[a : b+1]
word2 = s[c : d+1]
print(word1 +" "+ word2)