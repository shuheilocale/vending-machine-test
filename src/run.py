"""
要件:
ユーザがお金を入れて、飲み物を指定すると、指定􏰀飲み物とお釣りを出す。

条件:
お金は硬貨( 10円、50円、100円、500円)􏰀みとする
飲み物は、水(100円)、コーラ(150円)、お茶(130円)の3種類から1つ選ぶ 
飲み物の在庫は各 3本ずつとし、売り切れの場合は投入金額を返金する
釣り銭は無限にあるものとする


インタフェース :
INPUT→飲み物の種別、投入金額 
OUTPUT→飲み物の取得結果、お釣り

仕様:
実行すると、ユーザの入力待ちになる
“飲み物の種別:投入金額”の形式で入力する
飲み物が買えた場合、「〜が買えました。お釣り􏰁〜円です。」と出力する
飲み物が買えなかった場合、「〜が買えません。〜円足りません。」と出力する
飲み物が売り切れだった場合、「〜􏰁売り切れです。〜円返金します。」と出力する
"""

from vending_machine import VendingMachine
import drinks



def run():
    vending_machine = VendingMachine()

    # 飲み物を補充する
    # TODO:関数にする
    additional_drinks = [drinks.Water(), drinks.Water(), drinks.Water(), 
     drinks.Cola(), drinks.Cola(), drinks.Cola(), 
     drinks.Tea(), drinks.Tea(), drinks.Tea()]

    for d in additional_drinks:
        vending_machine.AddDrink(d)

    # debug
    vending_machine.DisplayStock()


    print('購入する飲み物と、投入する金額を入力してください。形式：“飲み物の種別:投入金額”')
    
    # フォーマットチェック
    if False:
        input_str = input()

    if False:
        print('“飲み物の種別:投入金額”の形式で入力してください')
        return


    # お金を投入する
    #vending_machine.InputMoney()

    # 

    print('end')



if __name__ == '__main__':
    run()