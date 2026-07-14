from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about/<username>')
def about(username):
    return render_template('about.html', username = username)

@app.route('/myStory/<mystory_text>')
def my_story(mystory_text):
    return render_template('mystory.html', mystory_text = mystory_text)

@app.route('/contact')
def contact():
    return render_template('contact.html')


# LOGIN
USERNAME = "NewUser"
PASSWORD = "user1234"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username.lower() == USERNAME.lower():
            if password == PASSWORD:
                return render_template('login.html', success = f"Welcome: {username.capitalize()}")
            else:
                return render_template('login.html', error = "Incorrect Password")  
        else:
            return render_template('login.html', error = f"{username}: Incorrect Username")
        
    return render_template('login.html')
            

if __name__ == '__main__':
    app.run(debug=True)
