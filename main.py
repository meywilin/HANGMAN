import random

list_of_words = [
    "абрикос", "бамбук", "велосипед", "галактика", "дельфин",
    "единорог", "жасмин", "зебра", "изумруд", "календарь",
    "лампочка", "магнит", "ноутбук", "облако", "парусник",
    "радуга", "самовар", "телескоп", "университет", "фонарик",
    "холодильник", "циферблат", "черепаха", "шампунь", "щелкунчик",
    "экскаватор", "юла", "якорь", "барсук", "вертолёт",
    "гербарий", "дирижабль", "ёжик", "журавль", "зеркало",
    "инкубатор", "компас", "лаборатория", "микроскоп", "навигатор",
    "одуванчик", "пирамида", "ракета", "самолёт", "термометр",
    "улитка", "фартук", "хищник", "цапля", "чучело",
    "шторм", "щука", "эхо", "юг", "ягода"
]


num_word = random.randint(0, len(list_of_words))
word = list_of_words[num_word]
hidden_word = "_ " * len(word)
            
print(word)
hidden_word_list = hidden_word.split(" ")
del hidden_word_list[-1]
print(hidden_word_list)

count = 0
attempts = 8
already_been_letters = []
word_list = []
for letter in word:
    word_list.append(letter)
run = True
while run:
    
    letter_request = input("Введите букву:").lower()
    
    if letter_request in already_been_letters:
        print("Вы уже писали эту букву!")

    for letter in word:
        count += 1
        print(count)
        
        if letter_request == letter:
            already_been_letters.append(letter_request)
            hidden_word_list[count-1] = hidden_word_list[count-1].replace("_", letter_request)
            
            
        elif letter_request not in word:
            count = 0
            if letter_request in already_been_letters:
                continue
                count = 0
            else:
                print("такой буквы нет")
                attempts -= 1
                print("Количетсво попыток:", attempts)
                count = 0
                already_been_letters.append(letter_request)

        if word_list == hidden_word_list and attempts > 0:
            print("Вы отгадали слово!")
            run = False
            break
        elif attempts == 0:
            print("Вы проиграли! Загаданное слово:", word)
            run = False
            break 

        
                
        if count == len(word):
            count = 0

   
            
    print(hidden_word_list)    
    
