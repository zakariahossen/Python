import random 
print("input 'q' to exit, anytime")
score = 0
running = True
while running:
    rand_num = random.randint(0,10)
    gamer = input("Guess a number between 0 to 10: ")
    if gamer == "q":
        print("Game Over")
        break
    
    intGamer = int(gamer)
    if intGamer == rand_num:
        score += 10
        print(f'you won. Score {score}')
    else:
        print(f'you are wrong, the number was {rand_num} and your score{score}')
