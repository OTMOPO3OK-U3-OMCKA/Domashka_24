import os
from flask import Flask, request, jsonify
from data_reader import r_file
from utils import dict_cmd
from typing import *


from flask import Flask

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query/")
def perform_query():
    req = request.json
    try:
        cmd1 = dict_cmd[req["cmd1"]]
        cmd2 = dict_cmd[req["cmd2"]]
        result1 = cmd1(r_file(req["file_name"]), req["value1"])
        result2 = cmd2(result1, req["value2"])
        return jsonify(result2)
    except KeyError:
        return []

    # нужно взять код из предыдущего ДЗ
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py
    #return app.response_class('', content_type="text/plain")


if __name__ == "__main__":
    app.run()