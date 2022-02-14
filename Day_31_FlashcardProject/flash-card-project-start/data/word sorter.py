import csv
numbers = [str(n) for n in range(10)]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(numbers)
with open("chinese_words.txt", mode='r', encoding="utf-8") as data_file:
    content = data_file.read()
    new_content = ""
    for letter in content:
        if letter in numbers or letter in letters:
            pass
        else:
            new_content += letter

print(new_content)

# with open("chinese_words.txt", mode="w", encoding="utf-8") as data_file:
#     data_file.write(new_content)
#
