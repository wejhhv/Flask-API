#変換用の関数を書いたファイル
import convert

import os
from flask import Flask, jsonify, make_response
app = Flask(__name__)


#確認用
@app.route('/')
def index():
    return 'Hello World!'


@app.route('/v1/number2kanji/<Number>',methods=["GET"])  #GET
def ToKanji(Number):
    
    #判定結果と、変換結果を取得
    Bool,Res=convert.NumberToKanji(Number)
    
    if Bool==True:
        return Res
    
    #エラー時の処理
    else:
        error = make_response('error', 204)
        error.mimetype = app.config['JSONIFY_MIMETYPE']
        return error



@app.route('/v1/kanji2number/<Kanji>',methods=["GET"])  #GET
def ToNumber(Kanji):
    
    #判定結果と、変換結果を取得
    Bool,Res=convert.KanjiToNumber(Kanji)
    
    #int-> str
    Res=str(Res)

    if Bool==True:
        return Res
    

    #エラー時の処理
    else:
        error = make_response('', 204)
        error.mimetype = app.config['JSONIFY_MIMETYPE']
        return error


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))