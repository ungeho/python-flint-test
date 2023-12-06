from flint import *

# 2のべき乗の分母なので区間幅なし
print(arb(10.25))

# 2のべき乗の分母でない為、区間で表現される。
# しかし、10.3という入力による丸め誤差が発生する為注意が必要
# https://fredrikj.net/python-flint/general.html#inexact-numbers-and-numerical-evaluation
print(arb(10.3))

# 厳密に正しい値が欲しい場合は、arb("0.1")、arb("1/10")、arb(fmpq(1,10))のように実行する。
print(arb("1/3"))

# https://fredrikj.net/python-flint/general.html?highlight=showgood#inexact-numbers-and-numerical-evaluation
# showgood....与えられた関数(π)をgood()で正確に評価し、その結果を返す代わりに、区間の半径を明示せずに10進数で表示する。
# good....与えられた関数を評価し、precやdpsで指定された精度に対して正確な結果を得る。
# precとdpsの違い
# prec...bit単位の精度
# dps...10進数単位の精度
# 10進数で50桁まで正しいπの値を出力する。
showgood(lambda: arb.pi(), dps=50)


# 区間（半径）つきの50桁のπを得たい場合
# arbの精度を10進50桁に変更
ctx.dps = 50;
# arbに定数arb.pi()を渡して表示する。
print(arb(arb.pi()))

# bitで指定したい場合は下記のように
# 倍精度
# ctx.prec = 53;
# print(arb(arb.pi()))

# 精度の設定を戻したい場合（恐らく倍精度）
ctx.default()