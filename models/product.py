class Product:

    def __init__(self, product_name, product_description, in_stock, buy_cost, sell_cost, manufacturer, id = None):
        self.product_name = product_name
        self.product_description = product_description
        self.in_stock = in_stock
        self.buy_cost = buy_cost
        self.sell_cost = sell_cost
        self.manufacturer = manufacturer
        self.id = id