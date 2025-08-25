from flask import Flask, jsonify, request

app = Flask(__name__)

# Sadə məlumat bazası kimi dictionary (sözlük) istifadə edirik
melumatlar = {
    1: {"ad": "Aylin", "yas": 30},
    2: {"ad": "Ramil", "yas": 25}
}

# GET metodu - istifadəçi məlumatını əldə etmək üçün
@app.route('/istifadeciler/<int:id>', methods=['GET'])
def istifadeci_alaq(id):
    istifadeci = melumatlar.get(id)
    if istifadeci:
        return jsonify(istifadeci)
    else:
        return jsonify({"xeta": "İstifadəçi tapılmadı"}), 404

# POST metodu - yeni istifadəçi əlavə etmək üçün
@app.route('/istifadeciler', methods=['POST'])
def yeni_istifadeci_elave_et():
    yeni_istifadeci = request.get_json()
    yeni_id = max(melumatlar.keys()) + 1
    melumatlar[yeni_id] = yeni_istifadeci
    return jsonify({"id": yeni_id}), 201

# PUT metodu - mövcud istifadəçi məlumatını yeniləmək üçün
@app.route('/istifadeciler/<int:id>', methods=['PUT'])
def istifadeci_yenile(id):
    if id not in melumatlar:
        return jsonify({"xeta": "İstifadəçi tapılmadı"}), 404
    yenilenmis_istifadeci = request.get_json()
    melumatlar[id] = yenilenmis_istifadeci
    return jsonify(yenilenmis_istifadeci)

# DELETE metodu - istifadəçini silmək üçün
@app.route('/istifadeciler/<int:id>', methods=['DELETE'])
def istifadeci_sil(id):
    if id not in melumatlar:
        return jsonify({"xeta": "İstifadəçi tapılmadı"}), 404
    del melumatlar[id]
    return jsonify({"mesaj": "İstifadəçi silindi"})

if __name__ == '__main__':
    app.run(debug=True)
