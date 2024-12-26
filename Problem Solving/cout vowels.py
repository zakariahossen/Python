# this function will count how many vowels in your name/word/sentence
def count_vowels(name):
    count = 0
    # create a list of vowels
    vowels = ["a", "e", "i", "o", "u", "A", 'E', 'I', 'O', 'U']
    for char in name:
        if char in vowels:
            count = count + 1
    return count

user_name = input("Your name: ")
result = count_vowels(user_name)
print(f'there is {result} vowels in {user_name}')
