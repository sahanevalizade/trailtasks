from flask import Flask
app = Flask(__name__)
@app.route("/")
def qafqaz():
    return """
    <html>
        <head>
            <title>Qafqaz Dağları</title>
        </head>
        <body>
            <h1>Qafqazın Möhtəşəm Təbiəti</h1>
            <p>Qafqaz dağları Avropa ilə Asiyanı ayıran bir sıra uca və möhtəşəm dağlardır.</p>
            <ul>
                <li>Bazardüzü dağı – Azərbaycanın ən hündür zirvəsi</li>
                <li>Elbrus dağı – Qafqazın və Avropanın ən yüksək zirvəsi</li>
                <li>Şahdağ – məşhur turizm məkanı</li>
            </ul>
            <hr>
            <p><i>Qafqaz dağları həm təbiət, həm də mədəni müxtəliflik baxımından zəngindir.</i></p>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1454)