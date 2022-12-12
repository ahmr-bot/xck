from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/dYvFMYL8/h8A2xuUsHKoMz',  methods=['POST'])
def get_code():
    code = [
        {"status": "1", "code": "00", "errorDesc": "请求成功", "result": "短信发送中,请注意查收",
         "queryId": "7c954755b6ab8b4547ba844b19b91a45"}
    ]
    return jsonify(code)
@app.route('/PMfdZtmQM6PIu/jKDFMlURRsN6D9',  methods=['POST'])
def getcolor():


    data = request.json
    if data['y892342'] == '111111':
        color = {"status": "1", "code": "00", "errorDesc": "请求成功",
             "result":
                 {"color": "green",
                  "phone": "1145141919810",
                  "time": "2022.12.12 08:20:29",
                  "message": "xxx"},
             "queryId": "ff59252b4572f4480e48f5d44642c188"
             }
        return jsonify(color)
    else:
        code_error = {
                "status": "3",
                "code": "21",
                "errorDesc": "验证码错误",
                "result": "null",
                "queryId": "7c954755b6ab8b4547ba844b19b91a45"
            }
        return jsonify(code_error)
if __name__ == '__main__':
    app.run()
