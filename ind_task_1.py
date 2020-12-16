# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает английский текст из файла и выводит его на экран,
# заменив каждую первую букву слов, начинающихся с гласной буквы, на прописную.


if __name__ == '__main__':
    with open('files/text1.txt', 'r') as f:
        text = f.read()

    temp_lis = []
    for i, word in enumerate(text.split(" ")):
        word_lis = list(word)
        if word_lis[0] in ['a', 'e', 'o', 'i', 'u', 'y']:
            word_lis[0] = word_lis[0].upper()
        temp_lis.append(''.join(word_lis))
    text = ' '.join(temp_lis)
    print(text)



