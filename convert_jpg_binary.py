import tkinter as tk
from tkinter import filedialog, messagebox
import os

def select_jpg_file():
    file_path = filedialog.askopenfilename(
        title = "画像を選択してください",
        filetypes = [("JPEG files", "*.jpg;*jpeg")]
    )
    if not file_path:
        return

    try:
        # ファイルをバイナリモードで読みこむ
        with open(file_path, "rb") as f:
            binary_data = f.read()

        # 16進数に変換
        hex_data = [f"0x{byte:02x}" for byte in binary_data]

        # 16バイトごとに改行
        formatted_hex = ""
        for i, byte in enumerate(hex_data):
            formatted_hex += byte + ", "
            if (i + 1) % 16 == 0:
                formatted_hex += "\n"

        # 出力ファイル名を設定
        output_file = os.path.splitext(file_path)[0] + "_output.txt"

        # テキストファイルに書き込む
        with open(output_file, "w") as out_f:
            out_f.write(formatted_hex.strip(", \n"))

        # 完了通知
        messagebox.showinfo("完了", f"データを出力しました. \n{output_file}")

    except Exception as e:
        messagebox.showerror("エラー", f"エラーが発生しました: {e}")

# GUIの構築
root = tk.Tk()
root.title("JPGバイナリ変換ツール")
root.geometry("300x150")

# 説明ラベル
label = tk.Label(root, text = "選択したJPG画像を解析・変換します", font = ("Arial", 12))
label.pack(pady = 10)

# 実行ボタン
select_button = tk.Button(root, text = "画像を選択", command = select_jpg_file)
select_button.pack(pady = 10)

# 終了ボタン
exit_button = tk.Button(root, text = "終了", command = root.quit)
exit_button.pack(pady = 5)

root.mainloop()