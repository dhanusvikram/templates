from imp import source_from_cache
from flask import Flask, redirect, url_for, request,render_template
app=Flask(__name__,template_folder='template')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' %name 

@app.route('/travel', methods=['POST', 'GET'])
def travel():
    if request.method == 'POST':
        user = request.form['nm']

        return redirect(url_for('success', name = user))

    return render_template("travel.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        return redirect(url_for('travel'))

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)