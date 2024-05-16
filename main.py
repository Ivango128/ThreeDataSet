import pandas as pd
import matplotlib.pyplot as plt
from googletrans import Translator

# Создаем объект переводчик
translator = Translator()

df = pd.read_csv('menu.csv')

#print(df.info())
pd.set_option('display.max_rows', None)

# 1 гипотеза: В магдональдс присутствют блюда которые превыщают дневную норму холестерина

count_item_Cholesterol = 0

def get_count_cholesterol(row): # функция считает сколько и какие блюда нарушают норму холестерина
    global count_item_Cholesterol
    if row['Cholesterol (% Daily Value)'] >= 100:
        count_item_Cholesterol += 1
        #переводим с английского на русский
        item = translator.translate(row['Item'], src='en', dest='ru').text
        return item
    return 0


df['Max_Cholesterol'] = df.apply(get_count_cholesterol, axis = 1)

# Отфильтруем только продукты с ненулевым значением в столбце 'Max_Cholesterol'
non_zero_max_cholesterol = df[df['Max_Cholesterol'] != 0]

# Создание графика
plt.figure(figsize=(10, 6))
plt.bar(non_zero_max_cholesterol['Max_Cholesterol'], non_zero_max_cholesterol['Cholesterol (% Daily Value)'], color='skyblue')
plt.title('Значение холестерина (% от дневной нормы) для продуктов с максимальным холестерином')
plt.xlabel('Продукт')
plt.ylabel('Холестерин (% от дневной нормы)')
plt.xticks(rotation=45, ha='right')  # Поворот подписей по оси X для лучшей читаемости
plt.tight_layout()  # Для улучшения компактности графика
plt.show()
# Таким образом по первому графику мы видим, что в макдональдс есть продукты нарушаюшие
# дневную норму холестерина, и их нельзя употреблять в пишу


# Гепотиза 2: В меню макдональдс больше всего продуктов в категории "Chicken & Fish" и "Beef & Pork", так как макдональдс это бургерная

# Подсчет количества продуктов в каждой категории
category_counts = df['Category'].value_counts()
print('Кол.-во продуктов в категориях "Курица и рыба" и "Говядина и свинина"', category_counts['Chicken & Fish'] + category_counts['Beef & Pork'])

# Создание графика
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Количество продуктов в каждой категории')
plt.xlabel('Категория')
plt.ylabel('Количество продуктов')
plt.xticks(rotation=45, ha='right')  # Поворот подписей по оси X для лучшей читаемости
plt.tight_layout()  # Для улучшения компактности графика
plt.show()

# В результате мы получаем информацию, что больше всего продуктов в категории "Кофе чай"


# 3 гипотеза: В магдональдс присутствют блюда которые превыщают дневную норму холестерина насыщенных жиров
def get_count_dietary_fiber(row):
    global count_item_dietary_fiber
    if row['Saturated Fat (% Daily Value)'] >= 100:
        # Переводим с английского на русский
        item = translator.translate(row['Item'], src='en', dest='ru').text
        return item
    return 0

# Применяем функцию к каждой строке датафрейма
df['Max_Dietary_Fiber'] = df.apply(get_count_dietary_fiber, axis=1)

# Отфильтровываем только продукты с ненулевым значением в столбце 'Max_Dietary_Fiber'
non_zero_max_dietary_fiber = df[df['Max_Dietary_Fiber'] != 0]

# Создание графика
plt.figure(figsize=(10, 6))
plt.bar(non_zero_max_dietary_fiber['Max_Dietary_Fiber'], non_zero_max_dietary_fiber['Saturated Fat (% Daily Value)'], color='skyblue')
plt.title('Значение пищевых волокон (% от дневной нормы) для продуктов с максимальным содержанием')
plt.xlabel('Продукт')
plt.ylabel('Пищевые волокна (% от дневной нормы)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
