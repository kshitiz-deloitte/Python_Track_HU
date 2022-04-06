def longest_word(word_list):
    return max(word_list, key=len)


with open(r"C:\Users\kbhurtel\PycharmProjects\PythonTrack_HU\resources\a.txt") as f:
    lines = f.readlines()
longest_word_per_line = []

for i in range(len(lines)):
    word_list = list(lines[i].split(" "))
    longest_word_per_line.append(longest_word(word_list))


print("The longest word in the given file is:", longest_word(longest_word_per_line))

