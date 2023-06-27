#! /usr/bin/python3

file = open("wordfile.txt")
words = [line.rstrip().upper() for line in file]
# print(words[-10:])
letter_count = {}
for word in words:
    for char in word:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
print(letter_count)

word_dict = {}

for word in words:
    sum_letter_count = 0
    for letter in set(word):
        sum_letter_count += letter_count[letter]
    word_dict[word] = sum_letter_count

sorted_word_dict = sorted(word_dict.items(),key=lambda x:x[1], reverse = True)
for entry in sorted_word_dict[:10]:
    print(entry[0], entry[1])
    
# Save the 10 best starting words
best_starting_words = [entry[0] for entry in sorted_word_dict[:10]]
print(best_starting_words)
        
