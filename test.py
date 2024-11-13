# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def home_page():
#     return "<p>hello world</p>"




# if __name__=="__main__":
#     app.run(host="0.0.0.0")

from flask import Flask

app=Flask(__name__)

@app.route("/")
def home_page():
    return "<p>home page</p>"

if __name__=='__main__':
    app.run(host='0.0.0.0')