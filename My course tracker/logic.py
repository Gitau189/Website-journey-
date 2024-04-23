from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def login():
   return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def log():
   user = request.form['nm']
   password = request.form['pw']
   if password == "Queenof12@": # replace with your logic
      return redirect(url_for('success', name = user))
   else:
      return "Incorrect password. Please try again."

if __name__ == '__main__':
   app.run(debug = True)
