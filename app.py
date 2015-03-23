# -*- coding: utf-8 -*
from flask import Flask, render_template, request, abort
from car import Car

app = Flask(__name__)

car = Car()

handle_map = {
    'forward': car.forward,
    'left': car.left,
    'right': car.right,
    'pause': car.stop,
    'backward': car.backward,
}


@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")


@app.route('/handle', methods=['GET'])
def handle():
    try:
        # 获取GET参数
        operation = request.args.get('type', '')
    except ValueError:
        abort(404)  # 返回 404
    else:
        if operation in handle_map.iterkeys():
            handle_map[operation]()
        else:
            abort(404)
    return 'ok'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=False)
