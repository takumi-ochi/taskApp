import tkinter as tk
from tkinter import messagebox
from src.backend.backend import get_jira_issue
from src.config.Const import DETAIL_WINDOW_WIDTH, DETAIL_WINDOW_HEIGHT, DETAIL_WINDOW_X, DETAIL_WINDOW_Y

def display_issues(tree, issues):
    for row in tree.get_children():
        tree.delete(row)
    for issue in issues:
        issue_key = issue['key']
        project_name = issue['fields']['project']['name']
        issue_summary = issue['fields']['summary']
        issue_type = issue['fields']['issuetype']['name']
        issue_status = issue['fields']['status']['name']
        tree.insert("", "end", values=(issue_key, project_name, issue_summary, issue_type, issue_status))

def on_issue_double_click(event, tree, root):
    selected_item = tree.selection()
    if selected_item:
        issue_key = tree.item(selected_item, 'values')[0]
        issue_data, error = get_jira_issue(issue_key)
        if error:
            messagebox.showerror("エラー", f"エラーが発生しました: {error}")
        else:
            display_issue_details(issue_data, root)

def display_issue_details(issue_data, root):
    # 説明を取得し、存在しない場合はデフォルトメッセージを設定
    issue_description = issue_data['fields'].get('description', None)
    
    if not issue_description:
        issue_description = "説明がありません。"
    elif isinstance(issue_description, dict):
        issue_description = extract_text_from_json(issue_description)

    # 新しいウィンドウを作成して説明を表示
    detail_window = tk.Toplevel(root)
    detail_window.title("チケット詳細")
    detail_window.geometry(f"{DETAIL_WINDOW_WIDTH}x{DETAIL_WINDOW_HEIGHT}+{DETAIL_WINDOW_X}+{DETAIL_WINDOW_Y}")
    
    text_widget = tk.Text(detail_window, wrap='word')
    text_widget.insert(tk.END, issue_description)
    text_widget.config(state=tk.DISABLED)  # 読み取り専用に設定
    text_widget.pack(expand=True, fill='both')

def extract_text_from_json(json_data):
    text = ""
    if 'content' in json_data:
        for content in json_data['content']:
            if 'content' in content:
                for item in content['content']:
                    if item['type'] == 'text':
                        text += item['text']
    return text