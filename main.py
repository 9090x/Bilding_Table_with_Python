from prettytable import PrettyTable
from matplotlib import pyplot as plt


table = PrettyTable()
table.field_names = ["№", "нэйм", "прайс", "валуе", "фул прайс"]

products = []
pay = []

for и in range(3):
    продукт = input("введите название продукта: ")
    прайс = int(input("укажите цену продукта: "))
    квалити = int(input("укажите количество продукта: "))
    table.add_row([и + 1, продукт, прайс, квалити, прайс * квалити])

    products.append(продукт)
    pay.append(прайс * квалити)

print(table)

plt.bar(products, pay, color="green")
plt.show()

