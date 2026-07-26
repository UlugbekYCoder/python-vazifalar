products = ['apple', 'banana', 'cucumber']
prices = [12_000, 23_000, 24_000]


def menu():
    print('\n1. Add product')
    print('2. Remove product')
    print('3. View cart')
    print('4. Checkout')
    print('5. Exit')

while True:
    menu()

    user_input = int(input("Please enter your choice (1,5): "))

    if user_input == 1:
        name = input("Enter product's name: ")
        price = int(input("Enter product's price: "))

        products.append(name)
        prices.append(price)

        print(f"Product '{name}' added")

    elif user_input == 2:
        name = input("Enter product's name: ")

        if name in products:
            index = products.index(name)

            prices.pop(index)
            products.remove(name)

            print(f"Product '{name} removed'")


        else:
            print("Product Not Found")



    elif user_input == 3:
        n = 1

        print("----Cart----")
        for name, price in zip(products, prices):
            print(f"{n}. {name} -> {price}")
            n += 1

        print("\nQuantity:", n-1)
        print("Total price:", sum(prices))

    elif user_input == 4:
        print("Thanks for your shopping!")

    elif user_input == 5:
        print("GoodBye!")
        break

    else:
        print("Please enter only between 1 and 5")







