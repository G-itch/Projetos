from flask import Flask, render_template, request,redirect
import keyboard
from time import sleep
stop=""
stop_=""
play=""
play_=""
back=""
back_=""
forward=""
forward_=""
volumeup=""
volumeup_=""
volumedown=""
volumedown_=""
enter=""
enter_=""
tab=""
tab_=""
full=""
full_=""
minimize=""
minimize_=""
mute=""
mute_=""
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home',methods=['POST'])
def home():
    return render_template('index.html')
@app.route('/build',methods=['POST'])
def build():
    return render_template('build.html')
@app.route('/script',methods=['POST'])
def scriptpage():
    return render_template('script.html')
@app.route('/py',methods=['POST'])
def script():
    while True:
        if keyboard.is_pressed("-"):
            keyboard.press("4")
            sleep(0.2)
        if keyboard.is_pressed("i"):
            sleep(0.2)
            break
    return render_template('script.html')
@app.route("/tecla" , methods=["POST","GET"])
def hexkey():
    t1 = request.form.get("oi")
    scr = request.form.get("hoi")
    print(t1)
    print(scr)
    while keyboard.is_pressed("i") == False:
        sleep(0.001)
    return render_template('script.html',Code=str(t1),Choose=str(t1),scroll=scr,ei="1")
@app.route('/about',methods=['POST'])
def about():
    return render_template('about.html')   
if __name__ == '__main__':
    app.run(debug=True)