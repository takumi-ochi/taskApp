import sys
import os
import threading

# srcディレクトリをPythonパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import tkinter as tk
from tkinter import messagebox, ttk
from src.backend.backend import get_all_issues, get_jira_issue
from src.config.Const import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_X, WINDOW_Y
from src.gui.issue_details import (
    display_issues,
    on_issue_double_click,
    display_issue_details,
)
from src.gui.search_conditions import setup_search_conditions
from src.gui.detail import setup_tree


def on_get_issue(event=None):  # イベント引数を追加
    # インジケーターを表示
    progress_bar.pack(pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)
    progress_bar.start()

    # 検索処理を別スレッドで実行
    threading.Thread(target=perform_search).start()


def perform_search():
    ticket_id = ticket_id_entry.get()
    pj = pj_entry.get()
    summary = summary_entry.get()
    status = status_var.get()

    # ここで検索条件を使用してフィルタリングを行う
    issues, error = get_all_issues()

    # メインスレッドでUIを更新
    root.after(0, lambda: update_ui(issues, error, ticket_id, pj, summary, status))


def update_ui(issues, error, ticket_id, pj, summary, status):
    # インジケーターを停止して非表示
    progress_bar.stop()
    progress_bar.pack_forget()

    if error:
        messagebox.showerror("エラー", f"エラーが発生しました: {error}")
    else:
        # フィルタリング処理を追加
        filtered_issues = [
            issue
            for issue in issues
            if (not ticket_id or extract_issue_id(ticket_id) == issue["key"])
            and (not pj or pj in issue["fields"]["project"]["name"])
            and (not summary or summary in issue["fields"]["summary"])
            and (not status or status == issue["fields"]["status"]["name"])
        ]
        display_issues(tree, filtered_issues)


def extract_issue_id(input_text):
    import re

    match = re.search(r"/browse/([A-Z]+-\d+)", input_text)
    if match:
        return match.group(1)
    elif re.match(r"^[A-Z]+-\d+$", input_text):
        return input_text
    return None


def on_get_issue(event=None):  # イベント引数を追加
    # インジケーターを表示
    progress_bar.pack(pady=5, fill=tk.X)  # プログレスバーを検索ボタンの直後に配置
    progress_bar.start()

    # 検索処理を別スレッドで実行
    threading.Thread(target=perform_search).start()


def update_ui(issues, error, ticket_id, pj, summary, status):
    # インジケーターを停止して非表示
    progress_bar.stop()
    progress_bar.pack_forget()  # プログレスバーを非表示

    if error:
        messagebox.showerror("エラー", f"エラーが発生しました: {error}")
    else:
        # フィルタリング処理を追加
        filtered_issues = [
            issue
            for issue in issues
            if (not ticket_id or extract_issue_id(ticket_id) == issue["key"])
            and (not pj or pj in issue["fields"]["project"]["name"])
            and (not summary or summary in issue["fields"]["summary"])
            and (not status or status == issue["fields"]["status"]["name"])
        ]
        display_issues(tree, filtered_issues)


def run_app():
    global root, progress_bar, ticket_id_entry, pj_entry, summary_entry, status_var, tree, search_button
    root = tk.Tk()
    root.title("Jiraチケット取得アプリ")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}")

    # 検索条件のセットアップ
    ticket_id_entry, pj_entry, summary_entry, status_var = setup_search_conditions(root)

    # 検索ボタン
    search_button = tk.Button(root, text="検索", command=on_get_issue)
    search_button.pack(pady=10)

    # Enterキーで検索を実行
    root.bind("<Return>", on_get_issue)

    # Treeviewのセットアップ
    tree = setup_tree(root)
    tree.pack(pady=(30, 0))  # Treeviewの位置を少し下げる

    # ダブルクリックイベントのバインド
    tree.bind("<Double-1>", lambda event: on_issue_double_click(event, tree, root))

    # プログレスバー
    progress_bar = ttk.Progressbar(root, mode="indeterminate")

    root.mainloop()