from flask import Flask

app = Flask(__name__)

@app.route('/')
def esas_sehife():
    return """
    <html>
        <head>
            <title>Movsumler Haqqinda</title>
        </head>
        <body>
            <h1>Movsumler ve Onlarin Xususiyyetleri</h1>
            <p>Ilin dord movsum var: yaz, yay, payiz ve qis.<//p>
            <ul>
                <li>Hava cox istidir</li.
                <li>Gunes parlayir</li>
                <li>Insanlar denize gedir>
                <li>Meyveler bol olur</li>
            </ul>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

        