# df.describe(include='number')は、データフレームの数値型の列に関する統計情報を提供します。
# このメソッドは、数値型の列に対する基本的な統計量（平均、標準偏差、最小値、25パーセンタイル、中央値（50パーセンタイル）、75パーセンタイル、最大値）を計算します。

import pandas as pd

# サンプルデータフレーム
data = {'名前': ['太郎', '花子', '次郎'],
        '年齢': [28, 35, 22],
        '都市': ['東京', '大阪', '札幌'],
        '給与': [60000, 80000, 50000]}

df = pd.DataFrame(data)

# 非数値型の列（オブジェクト型）を追加
df['性別'] = ['男性', '女性', '男性']

# オリジナルのデータフレームを表示
print("オリジナルのデータフレーム:")
display(df)
print("\n")

# 数値型の列に関する統計情報を表示
desc_numeric = df.describe(include='number')

# 数値型の列に関する統計情報を表示
print("統計情報（数値型の列を含む）:")
display(desc_numeric)

# この例では、データフレームには '年齢' と '給与' という数値型の列が含まれています。
# df.describe(include='number')を使用すると、これらの数値型の列に関する統計情報が提供されます。
# 出力は以下のようになります：

# オリジナルのデータフレーム:
#    名前  年齢   都市     給与 性別
# 0  太郎  28   東京  60000  男性
# 1  花子  35   大阪  80000  女性
# 2  次郎  22   札幌  50000  男性


# 統計情報（数値型の列を含む）:
#              年齢           給与
# count   3.000000      3.000000
# mean   28.333333  63333.333333
# std     6.806859  15275.499799
# min    22.000000  50000.000000
# 25%    25.000000  55000.000000
# 50%    28.000000  60000.000000
# 75%    31.500000  70000.000000
# max    35.000000  80000.000000
# この出力では、'年齢'と'給与'列に関する統計情報が表示されています。