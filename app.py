from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

from controllers.scrapper import Scrapper


app = Flask(__name__)

CORS(app)
@cross_origin()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        try:
            res = Scrapper(request.form['searchStr'], int(request.form['imageCount']),request.form['searchEngine']).imageScrap()
            return render_template('index.html', res=res)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    app.run(port=8000, debug=True)