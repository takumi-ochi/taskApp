import sys
import os

# srcディレクトリをPythonパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.gui.taskApp import run_app

if __name__ == "__main__":
    run_app()