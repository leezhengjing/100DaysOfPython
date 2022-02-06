with open("file1.txt", mode="r") as file1:
    file1_content = file1.readlines()
    edited_content_1 = []
    for item in file1_content:
        edited_content_1.append(int(item.strip("\n")))

with open("file2.txt", mode="r") as file2:
    file2_content = file2.readlines()
    edited_content_2 = []
    for item in file2_content:
        edited_content_2.append(int(item.strip("\n")))

result = [n for n in edited_content_1 if n in edited_content_2]

# Write your code above 👆

print(result)


