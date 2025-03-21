from flask import Flask, render_template, redirect, url_for
from github_api import fetch_github_user_data

app = Flask(__name__, template_folder='templates')
cached_user_data = None

@app.route('/')
def resume():
    global cached_user_data
    if cached_user_data is None:
        cached_user_data = fetch_github_user_data()
    return render_template('resume_template.html', user=cached_user_data)

@app.route('/refresh')
def refresh():
    global cached_user_data
    cached_user_data = fetch_github_user_data()
    return redirect(url_for('resume'))

if __name__ == '__main__':
    app.run(debug=True)
