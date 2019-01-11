from flask import Flask,render_template,flash,redirect,url_for
from flaskblog import app
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User,Post


posts = [
    {
        'authour':'Derrick',
        'title':'Drew',
        'Content':'vast id',
        'date':'2018-12-4'

    },
    {
        'authour':'Alfred',
        'title':'alps',
        'Content':'vast id',
        'date':'2018-12-5'

    }
]

@app.route('/')
def index():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/home')
def home():
    return render_template('home.html',title='Home')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm() 
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login")
def login():
    form= LoginForm()
    return render_template('login.html',title='Login',form=form)
