# map は、Pythonのリストやイテラブル（反復可能なオブジェクト）の各要素に対して、指定した関数を適用して新しいリストやイテラブルを生成するための関数です。以下に具体的な例を示します。
# 例として、与えられたリストの各要素を2倍にする関数を定義し、それを map を使ってリストの各要素に適用して新しいリストを生成します。

# 関数を定義
def double(x):
    return x * 2

# リストを作成
numbers = [1, 2, 3, 4, 5]

# mapを使用して関数を適用し、新しいリストを生成
doubled_numbers = list(map(double, numbers))

# 結果を表示
print(doubled_numbers)

# このコードの説明：
# double 関数は、引数 x を受け取り、それを2倍にして返す関数を定義します。
# numbers リストは、整数を含むリストです。
# map(double, numbers) は、double 関数を numbers リストの各要素に適用します。map 関数は新しいイテレータを返します。
# list(map(double, numbers)) を使用して、新しいリスト doubled_numbers を生成します。このリストには、元のリスト numbers の各要素が2倍になった値が含まれます。
# 最後に print(doubled_numbers) を使用して、結果を表示します。結果は [2, 4, 6, 8, 10] となります。

# このように、map 関数を使用することで、イテラブル内の要素に対して簡単に関数を適用し、新しいリストやイテラブルを生成できます。