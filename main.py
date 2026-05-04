class Kampyuter:
    def __init__(self, nomi, xotira):
        self.nomi = nomi
        self.__xotira = xotira

    def yuklash(self, gb):
        self.__xotira -= gb

    def ochirish(self, gb):
        self.__xotira += gb

    def info(self):
        print(f"Nomi: {self.nomi}")
        print(f"Xotira: {self.__xotira}")


k1 = Kampyuter("Macbook", 356)
k1.yuklash(100)
k1.info()

k1.ochirish(200)
k1.info()
