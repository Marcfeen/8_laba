import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

length = input('Введите количество символов для пароля:' + '\n')

for char in range(length):
  password += random.choice(chars)
print(password)
  
