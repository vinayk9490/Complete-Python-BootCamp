#Building URLs Dynamically 
#Variable Rules in Flask Routes
#Jinja 2 Template Engine

#Jinja2 template engine various ways to use it.
'''
1. Using {{ }} to print variables and expressions
2. Using {% %} for control statements like loops and conditionals
3. Using {% include %} to include other templates
'''

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><H1>Welcome to Flask Introduction</H1></html>"

#by-default the HTTP method is GET
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if (request.method == 'POST'):
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit', methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


#Variable Rules in Flask Routes
# @app.route('/success/<int:score>')
# def success(score):
#     return "The marks you have scored are " + str(score)

#Building URLS Dynamically 
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score > 50:
        res = "PASSED"
    else:
        res = "FAILED"
    #passing the result to the result.html template and rendering it
    return render_template('result.html', results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score > 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {'score': score, 'result': res}
    return render_template('result1.html', results=exp)



#Jinja2 with If Condition
@app.route('/result_analysis/<int:score>')
def analysis(score):
    #passing the result to the result.html template and rendering it
    return render_template('result.html', results=score)



if __name__ == '__main__':
    app.run(debug=True)