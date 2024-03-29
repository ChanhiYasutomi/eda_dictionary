# pd.cut 関数は、連続したデータをビン（区間）に分割するために使用される Pandas の関数です。これにより、データを異なる範囲に分類してカテゴリに変換することができます。以下に具体例を示します。
# まず、ランダムな数値からなるデータを作成し、それを pd.cut を使用してビンに分割します。
import pandas as pd
import numpy as np

# ランダムなデータの生成
np.random.seed(42)
data = np.random.randint(0, 100, 20)

# ビンの範囲を指定
bins = [0, 20, 40, 60, 80, 100]

# pd.cutを使用してデータをビンに分割
category = pd.cut(data, bins)

# 結果を表示
df = pd.DataFrame({'Data': data, 'Category': category})
print(df)

# この例では、0から100の範囲で20個のランダムな整数を生成し、pd.cut を使用してビンに分割しています。指定した bins パラメータに基づいて、各データポイントは対応するビン（区間）に分類されます。結果は新しい DataFrame に格納されています。
# ビンには左側の値は含まれ、右側の値は含まれません。例えば、20は[20, 40)の範囲に含まれますが、40は含まれません。結果として得られた DataFrame には、各データポイントがどのビンに分類されたかが表示されます。



# pd.cut を使用して、データを指定したビンに分割し、各ビンにラベルを付ける例を説明します。
# 具体例として、累積売上率がある DataFrame からデータを取得し、それを pd.cut を使用してビンに分割します。
import pandas as pd

# サンプルデータを作成
data = {'cum_sales_rate': [0.2, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95, 1.0]}
data_sorted = pd.DataFrame(data)

# pd.cutを使用してデータをビンに分割し、ラベルを付ける
data_sorted['Category'] = pd.cut(data_sorted['cum_sales_rate'], bins=[0, 0.7, 0.9, 1.0], labels=['A', 'B', 'C'])

# 結果を表示
display(data_sorted)
# この例では、cum_sales_rate 列の累積売上率に基づいて、ビン [0, 0.7), [0.7, 0.9), [0.9, 1.0] に分割しています。
# 各ビンにはそれぞれ 'A', 'B', 'C' というラベルが付けられます。この結果として、新しい 'Category' 列が DataFrame に追加され、各データポイントがどのビンに分類されたかが示されます。



import pandas as pd
import numpy as np

# ダミーデータを作成
data = {'purchase_count': np.random.randint(0, 1000, size=10)}
df = pd.DataFrame(data)

df.iloc[0,0] = 0
df.iloc[1,0] = 200
df.iloc[2,0] = 201
df.iloc[3,0] = 400

# =============================================
# パラメータ
# =============================================
columname = 'purchase_count'
start     = 0
bin       = 200
max       = df[columname].max()
# =============================================

# 区間のラベルを作成
labels = [f'{i+1}-{i+bin}' for i in range(start, max+1, bin)]
# {i+1} と書かざるを得ないため、0 スタートにならない。よってここだけ上書きして修正する
labels[0] = f'{start}-{start+bin}'

# purchase_countカラムを0始まりでbinずつに区切った値を作成
# include_lowest=true で下側の区間に含まれるようにする
# df[columname+'_bins'] = pd.cut(df[columname], bins=range(start, max + bin + 1, bin), labels=labels)
df[columname+'_bins'] = pd.cut(df[columname], bins=range(start, max + bin + 1, bin), labels=labels, include_lowest=True)

# 欠損数
print(df[columname+'_bins'].isnull().sum())

# このコードは、指定した列（purchase_count）の値を特定のビン（区間）に分割して新しい列を作成し、各値を対応するビンに配置しています。以下にコードの詳細と出力の説明を示します。
# pd.DataFrame(data) を使用してダミーデータフレーム df を作成します。このデータフレームには purchase_count カラムが含まれています。

# ビンのパラメータを指定します。
# start: ビンの開始値
# bin: 各ビンの幅
# max: データセット内の最大値
# 区間のラベルを作成します。このラベルは各ビンの範囲を表します。例えば、"0-200" は 0 から 200 までの値が含まれるビンを表します。ただし、0 から始まるビンのラベルは "{i+1}-{i+bin}" の形式になります。

# pd.cut() 関数を使用して、purchase_count カラムの値をビンに分割し、新しいカラム purchase_count_bins に格納します。bins パラメータには各ビンの境界を示すリストが指定され、labels パラメータにはビンのラベルが指定されます。include_lowest=True に設定されているため、各ビンは下側の区間に含まれます。

# 最後に、purchase_count_bins カラム内の欠損値の数を出力します。この行は、欠損値の数が表示されます。

# このコードを実行すると、purchase_count_bins カラムが作成され、各値が対応するビンに配置されます。また、欠損値の数も表示されます。

# 丸める場合は以下の処理を追加
# 新しいカテゴリーを追加するときはまずstr型に修正する
# Categoricalデータ型からstr型に変換
df[columname+'_bins'] = df[columname+'_bins'].astype(str)

# 下限の上書き
df.loc[df[columname] <= 200, columname+'_bins'] = '-200'

# 上限の上書き
df.loc[df[columname] >=750, columname+'_bins'] = '750-'

# 大小関係を考慮して、良い感じにクロス集計するにはカテゴリ型にしないといけないので戻す
df[columname+'_bins'] = df[columname+'_bins'].astype('category')

df_grouped = df.groupby([columname+'_bins'])[columname].agg(["count","sum"])

# 提供されたコードは、ビンに値を丸める追加の処理を含んでいます。具体的には、ビン内の値をカテゴリー（Categorical）データ型に変換し、一部の値を指定した条件で上書きしています。その後、カテゴリー型に戻し、クロス集計を行っています。以下に詳細な説明を示します。

# df[columname+'_bins'] = df[columname+'_bins'].astype(str):
# purchase_count_bins カラム内の値を文字列型（str）に変換します。これは後で一部の値を上書きする際に必要です。

# df.loc[df[columname] <= 200, columname+'_bins'] = '-200':
# purchase_count カラムの値が 200 以下の場合、対応する行の purchase_count_bins カラムの値を '-200' に上書きします。つまり、200 以下の値はビン '-200' に分類されます。

# df.loc[df[columname] >=750, columname+'_bins'] = '750-':
# purchase_count カラムの値が 750 以上の場合、対応する行の purchase_count_bins カラムの値を '750-' に上書きします。つまり、750 以上の値はビン '750-' に分類されます。

# df[columname+'_bins'] = df[columname+'_bins'].astype('category'):
# 上記の操作で一時的に文字列型に変換した purchase_count_bins カラムの値を再度カテゴリー型に変換します。これは、大小関係を考慮してクロス集計を行うために必要なステップです。

# df_grouped = df.groupby([columname+'_bins'])[columname].agg(["count","sum"]):
# 最終的に、カテゴリー型に変換された purchase_count_bins カラムを使用して、purchase_count カラムのクロス集計を行います。各ビン内のデータ数（'count'）と合計値（'sum'）が計算されます。

# この追加の処理により、特定の条件に基づいて値をビンに配置し、クロス集計が実行されます。これにより、データのセグメンテーションや集計が行いやすくなります。


# 年齢を区間に分けて、新しいカラムage_groupを作成する
df['age_group'] = pd.cut(df['age'],
                          bins=[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60,
                                65, 70, 75, 80, 85, 90, 95, 100, 105],
                          labels=['10-14', '15-19', '20-24', '25-29', '30-34',
                                  '35-39', '40-44', '45-49', '50-54', '55-59',
                                  '60-64', '65-69', '70-74', '75-79', '80-84',
                                  '85-89', '90-94', '95-99', '100-104'])

# このコードは、DataFrame df の 'age' カラムを区間に分け、新しい 'age_group' カラムを作成する方法を示しています。pd.cut 関数を使用して、'age' の値を指定した区間に分割し、それぞれの区間に対応するラベルを 'age_group' カラムに割り当てています。

# 具体的には、次の手順が行われています：
# pd.cut 関数を使用して、'age' カラムを指定した区間に分割します。bins パラメータには年齢の区間を指定し、labels パラメータには各区間に対応するラベルを指定しています。これにより、各行の年齢が対応する区間に分類されます。
# 結果として得られる区間に対応するラベルが、新しい 'age_group' カラムに割り当てられます。各行の 'age' に応じて、対応する 'age_group' ラベルが格納されます。
# このようにして、DataFrame 内の年齢データを区間ごとに分類し、新しい 'age_group' カラムを作成します。この 'age_group' カラムを使用することで、年齢に基づいた集計や可視化などの操作が簡単に行えるようになります。



# priceを区間に分けて、新しいカラムprice_groupを作成する
df['sales_group'] = pd.cut(df['sales'], 
                            bins=range(1, 20001, 2000), 
                            labels=['{}-{}'.format(i, i+1999) for i in range(1, 18001, 2000)])

# salesが16001以上の場合、sales_groupを"16001-18000"に設定する
df.loc[df['sales'] >= 16001, 'sales_group'] = '16001-18000'

# priceを区間に分けて、新しいカラムprice_groupを作成する
df['unit_price'] = pd.cut(df['price'], 
                            bins=range(1, 8001, 500), 
                            labels=['{}-{}'.format(i, i+499) for i in range(1, 7501, 500)])
# 下限の上書き
df.loc[df['price'] <= 2000, 'unit_price'] = '1501-2000'

# 上限の上書き
df.loc[df['price'] >= 7001, 'unit_price'] = '7001-7500'

print(df['unit_price'].isnull().sum())

no5 = df.groupby(['producttype','unit_price'])['target'].agg(["count","sum"])

# 不要な下限を削除するために一度ばらす
no5 = no5.reset_index()
no5 = no5[~no5['unit_price'].isin(['1-500', '501-1000', '1001-1500'])]
# 再度マルチインデックスにまとめる
no5 = no5.set_index(['producttype', 'unit_price'])



# 30 ずつ
# 上限 181-210　→　1 ~ 211　→　プラス 30 → 1 ~ 241
df['daysofsupply'] = pd.cut(df['use_days'], 
                            bins=range(1, 241, 30), 
                            labels=['{}-{}'.format(i, i+29) for i in range(1, 211, 30)])
# 150 ずつ
# 上限 2100-2250　→　1 ~ 2251　→　プラス 150 → 1 ~ 2401
df['coupon_discount_group'] = pd.cut(df['coupon_discount'], 
                            bins=range(1, 2401, 150), 
                            labels=['{}-{}'.format(i, i+149) for i in range(1, 2251, 150)])

# 下限の上書き
df.loc[df['coupon_discount'] <= 150, 'coupon_discount_group'] = '1-150'

# 上限の上書き
df.loc[df['coupon_discount'] >=2101, 'coupon_discount_group'] = '2101-2250'

# ★集計上の注意点
# 1 ~ 150 には 0 も含まれるようにしたので、エクセルでは 0 - 150 に上書きする
# Categorical 型の値を上書きするのは面倒なのでコードは修正しない



# パラメータ
columname = '予測確率'
start = 0
bin = 0.05
max = df[columname].max()

# bins の生成
bins = list(np.arange(start, max + bin, bin))

# ラベルの生成
labels = [f'{i:.2f}以上{i+bin:.2f}未満' for i in bins[:-1]]
labels[-1] = f'{bins[-2]:.2f}以上{bins[-1]:.2f}以下'  # 最後のラベルだけ別途設定

# ビン化とラベル付け
df[columname+'_bins'] = pd.cut(df[columname], bins=bins, labels=labels, include_lowest=True)

# このコードは、特定の列の値をビン化し、各ビンにラベルを付ける例です。以下はコードの詳細な説明です。
# columname、start、bin、maxのパラメータを設定します。これらのパラメータは、ビン化する対象の列名、ビンの開始値、ビンの幅、および最大値を表します。
# binsの生成: np.arangeを使用して、startからmaxまでの範囲でビンの境界値（bin edges）を生成します。ビンの幅はbinで指定された値です。生成されたビンの境界値はリストとしてbinsに格納されます。
# ラベルの生成: 各ビンに対するラベルを生成します。ビンの境界値をもとにして、各ビンに対するラベルを作成します。labelsリストにラベルを格納します。最後のビンのラベルは別途設定されており、それがlabels[-1]に格納されます。
# ビン化とラベル付け: pd.cut関数を使用して、対象の列（df[columname]）を指定したビンに分割します。binsパラメータにはビンの境界値が、labelsパラメータにはビンのラベルが指定されます。include_lowest=Trueは、最小値を含むことを意味します。この処理により、指定した列の各値が対応するビンに分類され、ラベルが付けられます。その結果、新しい列columname+'_bins'がDataFrameに追加されます。

# このコードを使用することで、指定した列の値をビン化し、各ビンに対するラベルを簡単に付けることができます。これは、データのグループ化やビンごとの集計など、さまざまなデータ処理タスクで役立ちます。
