# 以下に、df.describe(exclude='number')を用いた具体的な例を示します。データフレームには、数値型と非数値型の列が含まれています。

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

# 数値型の列を除外してデータフレームを要約
desc_non_numeric = df.describe(exclude='number')

# 非数値型の列に関する統計情報を表示
print("統計情報（数値型の列を除外）:")
display(desc_non_numeric)

# この例では、データフレームには '名前'（オブジェクト型）、'都市'（オブジェクト型）、'性別'（オブジェクト型）などの非数値型の列があります。df.describe(exclude='number')を使用すると、数値型の列（'年齢'と'給与'）を除外して、非数値型の列に関する統計情報が提供されます。
# 出力は以下のようになります：

# オリジナルのデータフレーム:
#    名前  年齢   都市     給与 性別
# 0  太郎  28   東京  60000  男性
# 1  花子  35   大阪  80000  女性
# 2  次郎  22   札幌  50000  男性


# 統計情報（数値型の列を除外）:
#         名前  都市  性別
# count    3   3   3
# unique   3   3   2
# top     太郎  札幌  男性
# freq     1   1   2
# この出力では、非数値型の列に関するcount、unique、top、freqなどの統計情報が表示されています。