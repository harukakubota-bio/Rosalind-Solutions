file_path = "python village/rosalind_ini6.txt"
with open(file_path, "r") as f:
    words = f.read().strip().split()
    dic = {}

for word in  words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word]  =1
    
for key, value in dic.items():
    print(key+ " "+str(value))
    
