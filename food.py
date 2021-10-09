from menu_item import MenuItem

#Warisan class MenuItem
class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count

    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kkal)'

    #Membuat class info kalori
    def calorie_info(self):
        print('kkal' + str(self.calorie_count))