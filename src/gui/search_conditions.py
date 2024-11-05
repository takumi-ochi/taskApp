import tkinter as tk
from tkinter import ttk

def setup_search_conditions(root):
    # 検索条件を配置するフレーム
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10, fill=tk.X)

    # チケットID入力
    ticket_id_label = tk.Label(search_frame, text="チケットID:")
    ticket_id_label.pack(side=tk.LEFT, padx=5)
    ticket_id_entry = tk.Entry(search_frame)
    ticket_id_entry.pack(side=tk.LEFT, padx=5)

    # プロジェクト入力
    pj_label = tk.Label(search_frame, text="プロジェクト:")
    pj_label.pack(side=tk.LEFT, padx=5)
    pj_entry = tk.Entry(search_frame)
    pj_entry.pack(side=tk.LEFT, padx=5)

    # 要約入力
    summary_label = tk.Label(search_frame, text="要約:")
    summary_label.pack(side=tk.LEFT, padx=5)
    summary_entry = tk.Entry(search_frame)
    summary_entry.pack(side=tk.LEFT, padx=5)

    # ステータス選択
    status_label = tk.Label(search_frame, text="ステータス:")
    status_label.pack(side=tk.LEFT, padx=5)
    status_var = tk.StringVar()
    status_combobox = ttk.Combobox(search_frame, textvariable=status_var)
    status_combobox['values'] = ("", "ToDo", "進行中", "保留", "完了")
    status_combobox.pack(side=tk.LEFT, padx=5)

    return ticket_id_entry, pj_entry, summary_entry, status_var