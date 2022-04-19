from django.test import TestCase

# Create your tests here.

word = "hangman game"
print(word)
new_word = ""
for x in range(len(word)):
    if word[x] != " ":
        new_word += "_ "

print(new_word)
test = ""

word = word.split()
first = word[0]
second = word[1]

for x in range(len(first)):
    test += "_ "

print(test)


# word = "hangman game"
# word = word.split()
# print(word[0])
# print(word[1])




