# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход делает человек.
# За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

import random as rand

print(f"В корзине 120 конфет.")
def candygame(candy_in_box, max_take_candy):

    while candy_in_box != 0:
        player_take = input("Твоя очередь брать конфеты: ")
        player_take = int(player_take)
        if 0 < player_take < candy_in_box + 1:
            candy_in_box -= player_take
            if candy_in_box > 0:
                print(f"Вы взяли {player_take} конфет(ы).")
            else:
                print(f"Вы взяли {player_take + candy_in_box} конфет(ы).")
                print(f"Вы победили!")
                candy_in_box = 0
                break

            bot_take = rand.randint(1, max_take_candy + 1)
            candy_in_box -= bot_take
            if candy_in_box > 0:
                print(f"Бот взял {bot_take} конфет(ы).")
                print(f"Осталось {candy_in_box} конфет(ы)!")
            else:
                print(f"Бот взял {bot_take + candy_in_box} конфет(ы).")
                print(f"Бот победил!")
                candy_in_box = 0
                break
        else:
            print("Вы взяли неверное количество конфет! Возьмите ещё раз, можно от 1 до 28!")

candygame(120, 28)