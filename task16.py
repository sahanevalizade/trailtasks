
from flask import Flask

  

app = Flask(__name__)




@app.route('/')
def start():
    return '<h2>KODY.AZ</h2>'


app.run(host='localhost', port=5151, debug=True)


if __name__ == "__main__":
    app.run(debug=True)