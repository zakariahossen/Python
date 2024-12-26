# It will count how many words in a sentence.
def word_count(sentence):
    # create a variable to store the count data
    count = 0
    # throw the sentence in a for loop to check the charecters
    for char in sentence:
        if char == ' ':
            count += 1
    # increase one in count for the last word.
    count += 1
    return count

user_sen = input("Input your texts: ")
result = word_count(user_sen)
print(result)
