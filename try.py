# try ステートメントは、Pythonのプログラム内でエラーを処理するために使用されます。具体的には、try ブロック内のコードを実行し、エラーが発生する可能性がある場合、エラーをキャッチして適切に処理することができます。以下は、try ステートメントの具体的な例です。
# ゼロ除算の例外をキャッチする
try:
    num = 10 / 0  # 0で割り算を試みます
except ZeroDivisionError:
    print("ゼロ除算エラーが発生しました。")
  
# このコードでは、try ブロック内で 10 / 0 を試みていますが、これはゼロ除算エラー (ZeroDivisionError) を発生させます。
# しかし、except ブロックによってこのエラーがキャッチされ、メッセージ "ゼロ除算エラーが発生しました。" が表示されます。これにより、プログラムがクラッシュせずにエラーを処理できます。
# try ステートメントは、エラーが発生したときのプログラムの動作を制御し、エラーに対処するためのさまざまな方法を提供します。エラーが発生しない場合、except ブロックは実行されず、通常のプログラムの実行が続行されます。
