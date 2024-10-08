# write a function that will convert kilometers to miles and miles to kilometers

def mileTokilo(mile):
    print(f'kilometer: {mile * 1.60934}')

def kiloTomile(kilo):
    print(f'mile: {kilo * 0.621371}')

while True:
    select = input("For 'k' to 'm' write 1 and for 'm' to 'k' write 2: ")
    if select == "1":
        user = float(input("kilometer: "))
        kiloTomile(user)
    elif select == "2":
        user = float(input("mile: "))
        mileTokilo(user)
    else:
        print("Something went wrong. Please try again.")
