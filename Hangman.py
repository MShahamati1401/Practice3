import random
guessworng = 0
start_char = 0

f = open('words.txt', 'r')
content = f.read().split()
words = random.choice(content)
print(words)

f.close()
list_temp = []
for char in words:
    list_temp.append("_")
print(list_temp)
print(len(list_temp))
print("Numbers Character Guess Words")
print("[",end="")
for char in words:
    print("_", end="")
print("]")
get_user_char = []
while guessworng < 7:
    get_user_char = input(f"Numbers Guess Worng {guessworng} as 7 Please Inter character:")
    get_user_char = get_user_char.lower()
    user_guess =get_user_char[0]
    if user_guess in words:
        char_count = words.count(user_guess)
        print(f"char_count {char_count}")
        for i in range(char_count):
            temp_index = words.index(user_guess, start_char)
            print(f"temp_index {temp_index}")
            start_char = temp_index + 1
            list_temp.pop(temp_index)
            list_temp.insert(temp_index, user_guess)
        print(list_temp)
        start_char = 0
        output = "".join(list_temp)
        if output == words:
            print("YOU WINNER")
        continue
    guessworng +=1
else:
    print("YOU Loser")
