from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    mylist = [1,2,3,4,5]
    return render_template('00-Basic-Template.html', mylist = mylist)

if __name__ == '__main__':
    app.run(debug=True)
