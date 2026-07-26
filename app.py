# # decimal
# from decimal import Decimal
#
# a = Decimal("0.1")
# b = Decimal("0.2")
#
# print(a + b)
#
#
#
# currencies = {
#         "USD": 12019.40,
#         "EUR": 13663.70,
#         "GBP": 10500.00,
#         "JPY": 1800000.00,
#         "CAD": 16200.00,
#         "AUD": 18100.00,
#         "CHF": 11400.00,
#         "CNY": 86500.00,
#         "INR": 1000000.00,
#         "SGD": 16100.00,
#     }
#
#
# def converter(som, kurs):
#     if kurs not in currencies:
#         return "Kurs mavjud emas"
#
#     # inner-function
#     def get_commission():
#         valyuta = currencies[kurs]
#         result = (som / valyuta) * 0.99
#
#         return f"{round(result, 3)} {kurs}\nKomissiya 1 foiz"
#
#     return get_commission()
#
#
# print(converter(12000, "USD"))
