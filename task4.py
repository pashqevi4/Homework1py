# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

juravliki_by_Petya = int(input())
juravliki_by_Seryoja = juravliki_by_Petya
juravliki_by_Katya = (juravliki_by_Petya + juravliki_by_Seryoja) * 2
total_juravliki = juravliki_by_Katya + juravliki_by_Petya + juravliki_by_Seryoja

print (total_juravliki)
