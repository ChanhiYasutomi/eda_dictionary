# np.sin は、NumPyライブラリの関数であり、与えられた角度（ラジアン）の正弦（sine）を計算するのに使用されます。具体的な例を示します。
import numpy as np

# 角度をラジアンで指定
angle_in_radians = np.pi / 2  # 90度をラジアンに変換

# 正弦を計算
sine_value = np.sin(angle_in_radians)

# 結果を表示
print(f"sin({angle_in_radians}) = {sine_value}")

# このコードでは、np.sin 関数を使用して、90度（π/2 ラジアン）の正弦を計算しています。sine_value 変数にその結果を格納し、それを表示しています。
# 結果は次のようになります：
# sin(1.5707963267948966) = 1.0
# したがって、np.sin 関数は与えられた角度の正弦値を計算し、科学や工学、データ分析などのさまざまな分野で使用されます。
