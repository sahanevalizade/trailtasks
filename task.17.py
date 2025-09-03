from flask import Flask

app = Flask(__name__)
 

@app.route('/')
def home():
    return 'MAIN PAGE' 

@app.route('/kody_az')
def data_test(data):
      
    return f'\Data: {escape(data)}!'




app.run(host='localhost', port=5151, debug=True)





