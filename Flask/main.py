"""This module serves the flask html environment"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    """
    Displays the home page.
        Parameters:

        Returns:
            rendering of 'index.html'
    """
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_submit():
    """
    Collects the latex code from the input box
        Parameters:
            request.form.['text']
        Returns:
            rendering of 'index.html'
    """
    print("submit")
    text = request.form['text']
    processed_text = text.upper()
    print(processed_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
