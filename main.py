import random

password_length = input('Введите длину пароля:' + '\n')
password_length = int(password_length)

characters = """+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюя
		АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"""

password = ""   

for index in range(password_length):
    password = password + random.choice(characters)

print("Сгенерированный пароль: {}".format(password))
