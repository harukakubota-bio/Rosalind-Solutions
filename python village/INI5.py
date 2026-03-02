file_path = "python village/rosalind_ini5.txt"
output_path = "python village/output_ini5.txt" 

with open(file_path, "r") as f:
    lines = f.readlines()

with open(output_path, "w") as out_f:
    for line in lines[1::2]:
        out_f.write(line)

print("出力が完了。 output_ini5.txt を確認してください。")