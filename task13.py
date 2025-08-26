from flask import Flask
app = Flask(__name__)


@app.route("/")
def tibbi_melumat():
    return """
    <html>
        <head> 
            <title>Insan Bedeninin Orqanlari</title>
        </head>
        <body>
            <h1>insan bedeninin esas orqanlari</h1>
            <p>Insan orqanlarinin esas orqanlari ve funksiyalari:</p>
            <ul>
               <li><b>Urek:</b> qani bedenne pompalayir</li>
                <li><b>Agciyerler:</b> Oksigen qebul edir ve karbon dioksidi xarici edir</li>
                <li><b>Boyrekler:</b> Qani temizleyir ve tulantillari sidik vasitesile xaric edir</li>
                <li><b>Mede:</b> Yemeyi hezm edir</li>
                 <li><b>Bas beyin:</b> Bedenin idareetme merkezdir</li>
            </ul>
            <hr>
            <p><i>Saglam heyat ucun orqanlarimizin qaygisina qalmaq vacibdir.</i></p>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1454)





