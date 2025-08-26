from flask import Flask
app = Flask(__name__)

@app.route("/")
def tibbi_melumat():
    return """
    <html>
        <head>
            <title>İnsan Bədəninin Orqanları</title>
        </head>
        <body>
            <h1>İnsan Bədəninin Əsas Orqanları</h1>
            <p>İnsan orqanizminin əsas orqanları və funksiyaları:</p>
            <ul>
                <li><b>Ürək:</b> Qanı bədənə pompalayır</li>
                <li><b>Ağciyər:</b> Oksigen qəbul edir və karbon dioksidi xaric edir</li>
                <li><b>Böyrəklər:</b> Qanı təmizləyir və tullantıları sidik vasitəsilə xaric edir</li>
                <li><b>Mədə:</b> Yeməyi həzm edir</li>
                <li><b>Baş beyin:</b> Bədənin idarəetmə mərkəzidir</li>
            </ul>
            <hr>
            <p><i>Sağlam həyat üçün orqanlarımızın qayğısına qalmaq vacibdir.</i></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
