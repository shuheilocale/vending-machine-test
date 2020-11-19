import enum

import drinks

class BuyResult(enum.Enum):
    # 売り切れ
    SOLD_OUT = enum.auto()
    # 不足
    LACK = enum.auto()
    # 購入成功
    SUCCESS = enum.auto()
    

class VendingMachine():

    def __init__(self, price_list):

        # ドリンクと金額リスト
        self.price_list = price_list

        # 補充しているドリンク
        self.stocks = {}

        # 顧客が投入したお金
        self.deposit = 0


    def add_drink(self, drink: drinks.Drink):
        """
        ドリンクを補充する

        Parameters
        ----------
        drink
            補充するドリンク
        """

        # 当たり付きドリンクがあるかもしれないので、
        # あえてインスタンスとして保持する
        if drink.name in self.stocks:
            self.stocks[drink.name].append(drink)
        else:
            self.stocks[drink.name] = [drink]

    def charge(self, cash: int) -> bool:
        """
        お金を投入する。

        Parameters
        ----------
        cash : int
            投入するお金

        Returns
        -------
        False/True : bool
            False:投入成功、True:投入成功
        """
        # 最安硬貨が10円なので、10の倍数以外は受け付けない
        if cash % 10 != 0:
            return False
        
        self.deposit += cash
        return True


    def exchange(self, drink_name: str):
        """
        ドリンクを購入する

        Parameters
        ----------
        drink_name : str
            購入するドリンクの名前

        Returns
        -------
        BuyResult : Enume
            購入結果
        drink : Drink
            ドリンク(購入できない場合はNone)
        deposit or charge : int
            売り切れの場合はチャージされているお金
            残高が足りない場合は不足金
            正常に購入できた場合はお釣り           
        """
        
        if not drink_name in self.price_list:
            raise Exception('リストに登録されていない飲み物が選択されました')

        # 売り切れの場合
        if not (drink_name in self.stocks and len(self.stocks[drink_name]) > 0):
            return BuyResult.SOLD_OUT, None, self.deposit
        
        price = self.price_list[drink_name]

        change = self.deposit - price

        # 残高が足りない場合
        if change < 0:
            return BuyResult.LACK, None, -change

        # 正常に購入できた場合
        drink = self.stocks[drink_name].pop(0)
        self.deposit -= price
        return BuyResult.SUCCESS, drink, change


    def display_stock(self):
       
        for k, v in self.stocks.items():
            print(k, len(v))

        
