from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World!"

@app.route("/andsomething")
def main1():
    return '''
     <form action="/andsomething/echo" method="GET">
         <input name="text">
         <input type="submit" value="echo">
     </form>
     '''

@app.route("/andsomething/echo")
def echo():
    return "You said: " + request.args.get('text', '')