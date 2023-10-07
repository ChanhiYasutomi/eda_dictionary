# .sample() メソッドは、データフレームやシリーズ内のランダムなサンプルを取得するためのPandasのメソッドです。
# このメソッドは、データのランダムな部分集合を抽出するのに便利です。以下に、.sample() メソッドの具体的な例を示します。
# まず、サンプルデータを作成します：
import pandas as pd

data = {'ID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 45]}

df = pd.DataFrame(data)

# このデータフレーム df は、ID、名前、年齢の列を持つ簡単なデータを表しています。
# 次に、.sample() メソッドを使用してランダムなサンプルを抽出します。例えば、2つのランダムな行を抽出する場合を考えてみましょう：
sampled_rows = df.sample(n=2)  # nは抽出するサンプル数を指定します

display(sampled_rows)

# このコードでは、n パラメータを使用して2つのランダムな行を抽出しています。結果は、データフレーム sampled_rows として表示されます。
# 実行するたびに異なる2つの行が抽出されることがあります。
# 以下は、実行結果の一例です：

#    ID     Name  Age
# 0   1    Alice   25
# 4   5      Eva   45

# .sample() メソッドは、ランダムなサンプルを抽出するだけでなく、さまざまなオプションを提供しています。たとえば、特定の列からランダムなサンプルを抽出したり、確率的なサンプリングを行ったりすることも可能です。