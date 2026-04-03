from flask import Flask

'''
It creates an instance of the Flask class, which will act as the WSGI application. The Flask class takes the name of the module as an argument, which is typically __name__. However, in this case, we are using a simple string 'app' for demonstration purposes. 
'''
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Flask Introduction. This is the home page.'

@app.route('/about')
def about():
    return 'This is the about page. Here you can find information about our application.'

#this indicates that the application will be running from here only.
if __name__ == '__main__':
    app.run(debug=True) 
    #when we mention debug=True, server will automatically reload whenever 
    # we make changes to the code. This is very useful during development as i
    # t allows us to see the changes without having to manually restart the 
    # server each time.
