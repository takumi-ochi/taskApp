import tkinter as tk
from tkinter import ttk
from src.config.Const import COLUMN_WIDTH_KEY, COLUMN_WIDTH_PJ, COLUMN_WIDTH_SUMMARY, COLUMN_WIDTH_TYPE, COLUMN_WIDTH_STATUS

def setup_tree(root):
    columns = ("キー", "PJ", "要約", "タイプ", "ステータス")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("キー", text="キー")
    tree.heading("PJ", text="PJ")
    tree.heading("要約", text="要約")
    tree.heading("タイプ", text="タイプ")
    tree.heading("ステータス", text="ステータス")

    tree.column("キー", width=COLUMN_WIDTH_KEY)
    tree.column("PJ", width=COLUMN_WIDTH_PJ)
    tree.column("要約", width=COLUMN_WIDTH_SUMMARY)
    tree.column("タイプ", width=COLUMN_WIDTH_TYPE)
    tree.column("ステータス", width=COLUMN_WIDTH_STATUS)

    # スクロールバーの追加
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scrollbar.pack(pady=(30, 0), side=tk.RIGHT, fill=tk.Y)  # スクロールバーを左側に配置

    # ツリービューをフレームに配置
    tree['yscrollcommand'] = scrollbar.set
    tree.pack(pady=(30, 0), side=tk.LEFT, fill=tk.BOTH, expand=True)

    return tree