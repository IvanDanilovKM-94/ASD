"""
код був написаний під час вебінару на тему "Python. Решение задачи о рюкзаке методом brute force"
авторство: https://geekbrains.ru/events/689
редакція: Данілов Іван Дмитрович КМ-94
"""

from itertools import combinations   # з модуля itertools імпортуємо ітератор для створення комбінацій

items = (                      # задаємо кортеж предметів 
   ('светр', 3, 50), 
   ('футболка', 0.1, 60),
   ('ліхтарик', 0.2, 70),
   ('книга', 1, 20),                 
   ('дощовик', 0.5, 50),
   ('карта', 0.3, 50),
   ('компас', 0.4, 40),
   ('консерви', 0.7, 70), 
   ('печиво', 2.8, 20),
   ('вода', 2.2, 25),
   ('термос', 0.25, 45),
)

total_volume = sum(list(zip(*items))[1]) #
""" 
Функція zip() бере ітератор в якості аргументу і повертає ітератор.  
Цей ітератор створює серію кортежів, що містять елементи з кожної ітерації.
У квадратних дужках вказано індекс зі списку items, що вказує на другий стовпчик - об'єм.
"""
max_volume = 6 # вказуємо максимальний об'єм рюкзака


def calcRucksackVol(rucksack):                   # функція для розрахунки поточного обсягу рюкзака
	total_volume = sum(list(zip(*rucksack))[1])
	return total_volume


def calcRucksackCost(rucksack):                   # функція для розрахунки поточної цінності речей рюкзака
	total_cost = sum(list(zip(*rucksack))[2])
	return total_cost


print("у розпорядженні {} предметів загальним обсягом {} л,які необхідно покласти в рюкзак {} літрів".\
     format(len(items), total_volume, max_volume))
"""
Метод format() був використанний для форматування рядка. 
Фігурні дужки вказують на те, що туди підставится значення, яке передається методу format()
"""

counter = 0               # лічильник комбінацій
max_cost = 0              # задаємо змінну, що означає максимальну цінність
result_items = []         # задаємо порожній список предметів, задля подальшого його наповнення
result_costs = []         # задаємо порожній список цінності предметів, задля подальшого його наповнення

for num in range(1, len(items) + 1):          #генерація чисел від 1 до числа, що дорівнює кількості предметів
   for i, combination in enumerate(combinations(items, num), 1):       # Функція enumerate () призначає індекс кожному елементу в ітерабельному об'єкті, який може бути використаний для посилання на елемент пізніше
       current_volume = calcRucksackVol(combination)                   # підрахунок об'єму поточної комбінації за допомогою виклику функції calcRucksackVol(), що приймає значення combination
       current_cost = calcRucksackCost(combination)                    # підрахунок цінності поточної комбінації за допомогою виклику функції calcRucksackCost(), що приймає значення combination
       if current_volume <= max_volume and current_cost >= max_cost:   # задання умови задачі: поточний об'єм <= максимальному об'єму рюкзака і поточна цінність >= раніше заданної максимальної
           counter += 1                                                # якщо виконуэться умова, то лічильник йде вперед на 1
           max_cost = current_cost                                     # поточну цінність присвоюємо максимальній
           result_items.append(combination)                            # заповнюємо список предметів комбінаціями 
           result_costs.append(current_cost)                           # заповнюємо список цінності предметів 
           print("комбінація {} набрала ціну {} и об'єм {:3.2f} л: {}".\
                 format(counter, current_cost, current_volume, combination))

max_cost_count = result_costs.count(max_cost)               # підраховуємо кількість досягнутих комбінацій з максимальною цінностю

print("вдалося {} раз досягти максимальної цінности {}".\
     format(max_cost_count, max_cost))


best_result = result_items[result_costs.index(max_cost)]     

print("Максимальний обсяг = ", round(calcRucksackVol(best_result),3))    # вивід максимального об'єму

[print(item) for item in best_result]        # генератор списку найкращого результату