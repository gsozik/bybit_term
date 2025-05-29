from pybit.unified_trading import HTTP
import pybit
import keys

session = HTTP(
    testnet=False,
    api_key=keys.api_key,
    api_secret=keys.secret_key,
)


def getOpen():
    positions = session.get_positions(
        category="linear",  # или "inverse", или "option" — в зависимости от рынка
        settleCoin="USDT"
    )
    for pos in positions['result']['list']:
        print(f"Тикер: {pos['symbol']}")
        print(f"Сторона: {pos['side']}")
        print(f"Размер позиции: {pos['size']} - {pos['positionIM']} USDT")
        print(f"Цена открытия: {pos['avgPrice']}")
        print(f"Цена сейчас: {pos['markPrice']}")
        print(f"Стоп-лосс: {pos['stopLoss']}")
        print(f"PNL: {pos['unrealisedPnl']}")
        print("-" * 20)


def placeOrder(
        symbol: str,
        side: str,  # 'Buy' или 'Sell'
        qty: float,
        price: float = None,
        time_in_force: str = "GTC",  # 'GTC', 'IOC', 'FOK'
        order_type='Limit',  # 'Market' или 'Limit'
):
    payload = {
        "category": "linear",  # для USDT деривативов
        "symbol": symbol,
        "side": side,
        "orderType": order_type,
        "qty": qty,
        "price": price,
        "timeInForce": time_in_force,
    }

    response = session.place_order(**payload)
    return response
