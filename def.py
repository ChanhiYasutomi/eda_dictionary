# Pythonの def キーワードは、新しい関数を定義するために使用されます。関数は、一連のコードステートメントをまとめて名前を付けたもので、再利用可能できます。以下に具体的な例を示します。
# 例えば、2つの数値を受け取り、それらの合計を計算する簡単な関数を定義することを考えてみましょう。
def add_numbers(a, b):
    result = a + b
    return result

# このコードでは、add_numbers という名前の関数を定義しています。この関数は2つの引数 a と b を受け取り、それらの合計を計算し、その結果を return キーワードを使用して返します。
# 関数を呼び出すには、次のようにします。
result = add_numbers(5, 3)
print(result)

# このコードを実行すると、add_numbers 関数が呼び出され、引数 5 と 3 が渡されます。関数内でこれらの引数が合計され、結果が result 変数に格納され、最後にその結果が表示されます。結果は 8 となります。
# こうして、def キーワードを使用して関数を定義し、再利用可能なコードブロックを作成できます。関数を呼び出すことで、同じ操作を何度も実行でき、コードの再利用性と可読性を向上させることができます。
