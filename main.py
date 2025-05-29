from functions import getOpen, placeOrder

while True:
    print("\nМеню действий")
    print("1. Посмотреть открытые сделки")
    print("2. Посмотреть открытые ордера")
    print("3. Создать ордер")
    choice = input("Выберите действие (1–6): ").strip()

    if choice == "1":
        print('Все открытые сделки: \n')
        getOpen()

    elif choice == "2":
        print('asd')

    elif choice == "3":
        print('\nТорговая пара на которую вы хотите разместить ордер? Пример ввода: KAVAUSDT, TONUSDT, BTCUSDT')
        symbol = input()
        print('В какую сторону вы хотите открыть сделку? Пример: Buy или Sell')
        side = input()
        print('Сколько монет вы хотите купить?')
        qty = float(input())
        print('По какой цене вы хотите купить 1 монету?')
        price = float(input())
        placeOrder(symbol, side, qty, price)

