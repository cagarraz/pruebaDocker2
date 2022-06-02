from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print('se conectaron\n')
    f = open("log/log.log", "a")
    f.write("se conectaron\n")
    f.close()
    return "conexionholi!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
