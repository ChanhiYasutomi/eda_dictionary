# .rank()は、Pandasライブラリで提供されているメソッドで、データフレームやシリーズ内の要素の順位（ランク）を計算するために使用されます。
# 要素の値に基づいて順位を割り当て、同じ値の要素に対しては平均順位を割り当てることができます。これはデータの順位を評価したり、ランキングを作成したりする際に便利です。
# 以下に、.rank()の具体的な使用例を示します：

import pandas as pd

# サンプルデータを作成
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Score': [85, 92, 78, 92, 88]}
df = pd.DataFrame(data)

# Score列を基準に順位を計算（デフォルトは昇順）
# df['Rank'] = df['Score'].rank()

# Score列を基準に降順で順位を計算
df['Rank_sort'] = df['Score'].rank(ascending=False,method = "first")

# df['Score'].rank()メソッドにはいくつかのオプション引数があり、要素の順位計算方法をカスタマイズするために使用できます。以下に一般的なオプション引数を示します：

# method: 要素の順位計算方法を指定します。以下の方法が選択できます。
# 'average'（デフォルト）: 同じ値を持つ要素には平均順位を割り当てます。
# 'min': 同じ値を持つ要素には最小の順位を割り当てます。
# 'max': 同じ値を持つ要素には最大の順位を割り当てます。
# 'first': 同じ値を持つ要素には最初に出現した要素に順位1を割り当て、それ以降の要素は順に順位を割り当てます。
# 'dense': 同じ値を持つ要素には同じ順位を付与する。その後の順位は飛ばされない。
# na_option: 欠損値（NaN）をどのように扱うかを指定します。デフォルトは'keep'で、欠損値をそのままにして順位計算を行います。'top'を指定すると、欠損値は最も高い順位（1位）に割り当てられます。'bottom'を指定すると、欠損値は最も低い順位に割り当てられます。
# これらのオプション引数を使用して、df['Score'].rank()メソッドの動作をカスタマイズできます。たとえば、以下のようにして特定の順位計算方法を指定できます：

# 最大順位を割り当てて欠損値を一番上に配置
df['Rank'] = df['Score'].rank(ascending=False, method='max', na_option='top')
# このコードでは、methodオプションで最大順位を使用し、na_optionオプションで欠損値を一番上に配置しています。
