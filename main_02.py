# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки.
# В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

#        |    фраза  |    фраза    |   фраза    |
#          | |  |  |   |   |   | |   |  |  |  |  слога
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
#           1   2  3   4   5   6     7  8  9  10   Слова
#Ритм есть, если
#Парам пам-пам  -> True
def has_rhythm(stroka):
    phrase = stroka.split()
    if len(phrase) > 1:
        count_of_a = list()
        for i in range(0, len(phrase)):
            count_of_a.append(phrase[i].count('а'))
        if len(set(count_of_a)) == 1: print('Парам пам-пам')
        else: print("Пам парам")
    else: print("Количество фраз должно быть больше одной!")
    
has_rhythm(stroka)