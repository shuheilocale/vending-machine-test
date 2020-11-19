自動販売機スクリプト

* ベース課題(v1.0)
* 応用課題(v2.0)

# 自動販売機スクリプトv1.0

## 要件

ユーザがお金を入れて、飲み物を指定すると、指定の飲み物とお釣りを出す。

## 条件
* お金は硬貨(10円、50円、100円、500円)のみとする
* 飲み物は、水(100円)、コーラ(150円)、お茶(130円)の3種類から1つ選ぶ 
* 飲み物の在庫は各 3本ずつとし、売り切れの場合は投入金額を返金する
* 釣り銭は無限にあるものとする

## インタフェース

* INPUT
  * 飲み物の種別、投入金額 
* OUTPUT
  * 飲み物の取得結果、お釣り

## 仕様

* 実行すると、ユーザの入力待ちになる
* “飲み物の種別:投入金額”の形式で入力する
* 飲み物が買えた場合、「〜が買えました。お釣りは〜円です。」と出力する
* 飲み物が買えなかった場合、「〜が買えません。〜円足りません。」と出力する
* 飲み物が売り切れだった場合、「〜売り切れです。〜円返金します。」と出力する

## 実行方法

```
git clone https://github.com/shuheilocale/vending-machine-test.git -b v1.0
cd vending-machine-test
chmod +x build.sh
chmod +x run.sh
./build.sh
./run.sh
```

## 実行例

```
購入する飲み物と、投入する金額を入力してください。形式：“飲み物の種別:投入金額”
お茶:130
お茶が買えました。お釣りは0円です。
```

# 自動販売機スクリプトv2.0

v1からの変更点のみ記載する。

## 条件

* 1000円が使えるように拡張する
* 残金が飲み物の最低料金を超えていれば、追加で購入できるようにする
* :1/10で全額返金されるくじを実装する

## 実行方法

```
git clone https://github.com/shuheilocale/vending-machine-test.git -b v2.0
cd vending-machine-test
chmod +x build.sh
chmod +x run.sh
./build.sh
./run.sh
```

## 実行例

```
購入する飲み物と、投入する金額を入力してください。形式：“飲み物の種別:投入金額”
コーラ:1000
コーラが買えました。残高は850円です。
追加購入しますか(残高850円)？：yes|no
yes
購入する飲み物を入力してください。
水
水が買えました。残高は750円です。
追加購入しますか(残高750円)？：yes|no
yes
購入する飲み物を入力してください。
お茶
お茶が買えました。残高は620円です。
追加購入しますか(残高620円)？：yes|no
no
お釣りは620円です。
```