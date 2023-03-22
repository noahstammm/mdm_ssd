from flask import Flask, render_template, request
from deepmultilingualpunctuation import PunctuationModel


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/punctuate', methods=['POST'])
def punctuate():
    text = request.form['text']
    print(text)
    dmp = PunctuationModel()
    punctuated_text = dmp.restore_punctuation(text)
    return render_template('result.html', text=text, punctuated_text=punctuated_text)


if __name__ == '__main__':
    app.run(debug=True)
