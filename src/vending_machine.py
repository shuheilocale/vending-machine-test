class VendingMachine():

    def __init__(self, price_list):
        self.stocks = {}
        self.price_list = price_list


    def AddDrink(self, drink):

        # 当たり付きドリンクがあるかもしれないので、
        # あえてインスタンスとして保持する
        if drink.name in self.stocks:
            self.stocks[drink.name].append(drink)
        else:
            self.stocks[drink.name] = [drink]

    def Exchange(self, drink_name : str, input_amount : int):
        """
        ret 飲み物、　返却するお金
        """
        
        if not drink_name in self.price_list:
            return None, None

        # ストックがなければ
        if not drink_name in self.stocks or len(self.stocks[drink_name]) == 0:
            print(f'{drink_name}は売り切れです。{input_amount}円返金します。')
            return None, input_amount
        
        price = self.price_list[drink_name]

        change = input_amount - price

        if change < 0:
            print(f'{drink_name}が買えません。{-change}円足りません。')
            return None, input_amount

        drink = self.stocks[drink_name].pop(0)
        print(f'{drink_name}が買えました。お釣りは{change}円です。')
        return drink, change

    def __CalcCahnge(self):
        pass
        

    def __PopDrink(self, drink):
        pass

    def DisplayStock(self):
       
        for k, v in self.stocks.items():
            print(k, len(v))

        
