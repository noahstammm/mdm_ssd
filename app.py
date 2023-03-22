from flask import Flask, render_template, request
from deepmultilingualpunctuation import PunctuationModel


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/punctuate', methods=['POST'])
def punctuate():
    try:
        text = request.form['text']
        print(text)
        if len(text) > 0:
            dmp = PunctuationModel()
            punctuated_text = dmp.restore_punctuation(text)
            return render_template('result.html', text=text, punctuated_text=punctuated_text)

        else:
            return render_template('result.html', error="Kein Text eingegeben")

    except Exception as e:

        return print("An error has occured", e)


if __name__ == '__main__':
    app.run(debug=True)
