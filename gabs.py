from flask import Flask, render_template, request

gabs = Flask(__name__)

@gabs.route('/',)
def index():
    return render_template('index.html')

@gabs.route('/sell')
def sell():
   return render_template('sell.html')

@gabs.route('/login')
def login():
    return render_template('login.html')

@gabs.route('/toyota')
def toyota():
    return render_template('toyota.html')

@gabs.route('/about')
def about():
    return render_template ('about.html')

@gabs.route('/account')
def account():
    return render_template('account.html')

@gabs.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    gabs.run(debug=True)
    
