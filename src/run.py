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


def vending_machine_gen(price_list, additional_drinks):

    vending_machine = VendingMachine(price_list)   
    for d in additional_drinks:
        vending_machine.add_drink(d)  

    return vending_machine

def parse_input(input_str):
    words = input_str.split(':')

    if len(words) == 1:
        return input_str, 0

    elif len(words) != 2:
        raise Exception(':の数が一致しません')
        
    drink_name = words[0]
    cash = words[1]
    
    if int(cash) < 0:
        raise Exception(':投入金額が０以上の整数ではありません')

    return drink_name, int(cash)


def user_input():
    if os.environ['RUN_MODE'] == 'DEBUG':
        target_drink = 'お茶'
        cash = 1000
        input_str = f'{target_drink}:{cash}'
        print(input_str)
    else:
        input_str = input()
        try:
            target_drink, cash = parse_input(input_str)
        except Exception as e:
            print('不正な入力です', e)
            return
    return target_drink, cash

def exchange(vending_machine, target_drink):

    result, drink, change = vending_machine.exchange(target_drink)

    if result == BuyResult.SOLD_OUT:
        print(f'{target_drink}は売り切れです。残高は{vending_machine.deposit}円です。')
    elif result == BuyResult.LACK:
        print(f'{target_drink}が買えません。{change}円足りません。')
    elif result == BuyResult.SUCCESS:
        print(f'{target_drink}が買えました。残高は{change}円です。')
    elif result == BuyResult.FREE:
        print(f'{target_drink}が当たりました。残高は{change}円です。')
    else:
        raise Exception()


def run():

    # 自動販売機で取り扱うドリンクの設定
    price_list = {'水':100, 'コーラ':150, 'お茶':130}
    additional_drinks = \
    [drinks.Water(), drinks.Water(), drinks.Water(), 
     drinks.Cola(), drinks.Cola(), drinks.Cola(), 
     drinks.Tea(), drinks.Tea(), drinks.Tea()]

    vending_machine = vending_machine_gen(price_list, additional_drinks)


    # ユーザによる入力の受け付け
    print('購入する飲み物と、投入する金額を入力してください。形式：“飲み物の種別:投入金額”')
    target_drink, cash = user_input()

    # お金の投入
    ret = vending_machine.charge(cash)
    if not ret:
        print('硬貨を入れてください')
        return
        
    # ドリンクの購入
    exchange(vending_machine, target_drink)

    while vending_machine.can_exchange():
            
        # 追加購入
        print(f'追加購入しますか(残高{vending_machine.deposit}円)？：yes|no')
        input_str = input()

        if input_str == 'yes':
            # 追加購入するドリンクの入力
            print('購入する飲み物を入力してください。')
            target_drink, _ = user_input()
            exchange(vending_machine, target_drink)
        else:
            print(f'お釣りは{vending_machine.widthdraw()}円です。')
            return
        
      
    

if __name__ == '__main__':
    run()