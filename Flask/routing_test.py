from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route('/product/<name>')
def get_product(name):
  return "The product is " + str(name)


@app.route('/product/<fname>/<lname>')
def get_multiple_names(fname,lname):
  return "The product is " + str(fname)+' ......'+str(lname)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=81)

    
    
    