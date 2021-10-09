from menu_item import MenuItem

#Warisan class MenuItem
class Drink(MenuItem):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'ml)'
