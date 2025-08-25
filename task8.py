from flask import Flask
app = Flask(__name__)

@app.route('/')

def ana_sehife():
    return """
    <html>
        <head>
            <title>Salam, Menim sehifeme xos geldiniz!</title>
                </head>
                    <body>
                <h1>Salam, menim sehifeme xos geldiniz!</h1>
                <p>Burada sizinle melumatlar paylasacagim</p>
            <p>Bu gun hava cox gozeldir</p>
            <ul>
                <li>Bu gun hava 25 derecedir</li>
                <li>Hava guneslidir</li>
                <li>Hava buludsuzdur</li>
                <li>Hava yagisli deyil</li>
            </ul>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1454)





