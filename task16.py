
from flask import Flask

  

app = Flask(__name__)




@app.route('/')
def start():
    return '''
    <h2>KODY.AZ & FLASK</h2>
    <a href='/about'>About page</a>
    '''


@app.route('/about')
def about():
    return '''                                      
    <h2>About page</h2>
    <a href='/'>Main page</a>
    '''





if __name__ == "__main__":
    app.run(debug=True)                                                                                                                                                                                                                                                               