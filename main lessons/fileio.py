file_path = r"C:\Users\TAKTIM\myfile.txt"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
