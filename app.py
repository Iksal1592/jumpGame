from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__, static_folder='.\\static', template_folder='.\\templates')

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
            return redirect(url_for('subpage'))
        else:
            error = "아이디 또는 비밀번호가 올바르지 않습니다."
    return render_template('index.html', error=error)



@app.route('/subpage')
def subpage():
    return render_template('subpage.html')

if __name__ == '__main__':
    app.run(debug=True)
