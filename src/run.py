"""
要件:
ユーザがお金を入れて、飲み物を指定すると、指定の飲み物とお釣りを出す。

条件:
お金は硬貨( 10円、50円、100円、500円)のみとする
飲み物は、水(100円)、コーラ(150円)、お茶(130円)の3種類から1つ選ぶ 
飲み物の在庫は各 3本ずつとし、売り切れの場合は投入金額を返金する
釣り銭は無限にあるものとする


インタフェース :
INPUT→飲み物の種別、投入金額 
OUTPUT→飲み物の取得結果、お釣り

仕様:
実行すると、ユーザの入力待ちになる
“飲み物の種別:投入金額”の形式で入力する
飲み物が買えた場合、「〜が買えました。お釣りは〜円です。」と出力する
飲み物が買えなかった場合、「〜が買えません。〜円足りません。」と出力する
飲み物が売り切れだった場合、「〜売り切れです。〜円返金します。」と出力する
"""

import os

from vending_machine import VendingMachine
from vending_machine import BuyResult
import drinks

def parse_input(input_str):
    
    words = input_str.split(':')
    if len(words) != 2:
        raise Exception(':の数が一致しません')
        
    drink_name = words[0]
    cash = words[1]
    
    if int(cash) < 0:
        raise Exception(':投入金額が０以上の整数ではありません')

    return drink_name, int(cash)


def run():
    price_list = {'水':100, 'コーラ':150, 'お茶':130}
    vending_machine = VendingMachine(price_list)

    # 飲み物を補充する
    # TODO:関数にする
    additional_drinks = \
    [drinks.Water(), drinks.Water(), drinks.Water(), 
     drinks.Cola(), drinks.Cola(), drinks.Cola(), 
     drinks.Tea(), drinks.Tea(), drinks.Tea()]

    for d in additional_drinks:
        vending_machine.add_drink(d)

    print('購入する飲み物と、投入する金額を入力してください。形式：“飲み物の種別:投入金額”')

    if os.environ['RUN_MODE'] == 'DEBUG':
        target_drink = 'お茶'
        cash = 130
        input_str = f'{target_drink}:{cash}'
    else:
        input_str = input()
        try:
            target_drink, cash = parse_input(input_str)
        except Exception as e:
            print('不正な入力です', e)
            return


    # お金を投入する
    ret = vending_machine.charge(cash)
    if not ret:
        print('硬貨を入れてください')
        return

    result, drink, change = vending_machine.exchange(target_drink)

    if result == BuyResult.SOLD_OUT:
        print(f'{target_drink}は売り切れです。{vending_machine.deposit}円返金します。')
    elif result == BuyResult.LACK:
        print(f'{target_drink}が買えません。{change}円足りません。')
    elif result == BuyResult.SUCCESS:
        print(f'{target_drink}が買えました。お釣りは{change}円です。')
    else:
        raise Exception()


if __name__ == '__main__':
    run()