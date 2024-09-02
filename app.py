from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__, static_folder='./static', template_folder='./templates')

users = {
    'smk1': '1234'
}

@app.route('/', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('mainpage'))
        else:
            error = "아이디 또는 비밀번호가 올바르지 않습니다."
    return render_template('index.html', error=error)



@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')

@app.route('/menu/game/jumpGame')
def jumpGame():
    return render_template('menu/game/jumpGame.html')



@app.route('/menu/game/tic_tac_toe')
def tic_tac_toe():
    return render_template('menu/game/tic_tac_toe.html')


@app.route('/menu/gpt/gpt')
def gpt():
    return render_template('menu/gpt/gpt.html')




@app.route('/menu/map/map')
def map():
    return render_template('menu/map/map.html')





if __name__ == '__main__':
    app.run(debug=True)
