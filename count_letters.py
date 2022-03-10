# The function counts letters in the word as argument

# Create map where letters as key and occurrence as value
# Run through the word letter by letter and increase occurrence value


def count_letters(word):
    rc = {}
    for letter in word:
        if letter not in rc:
            rc[letter] = 0
        rc[letter] += 1

    return rc;


print(count_letters("hello"))
print(count_letters("abc"))
print(count_letters("aabbss"))
print(count_letters(""))
