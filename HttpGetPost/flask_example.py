#!/usr/bin/env python

######################################################
#
# Test to understand Get and Post in a server
#
#######################################################
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
#######################################################

import flask

app = flask.Flask(__name__)

# By default, only responds to GET
@app.route('/hello1')
def hello1():
  return 'Hello Ariadna!'

# Responds to both GET and POST
@app.route('/hello2', methods=['GET', 'POST'])
def hello2():
  if flask.request.method == 'GET':
    return 'Hello %s! [GET!]' % flask.request.args['name']
  else:
    return 'Hello %s! [POST!]' % flask.request.form['name']

# Only responds to POST
@app.route('/hello3', methods=['POST'])
def hello3():
  return 'Hello Fabian!'


if __name__ == '__main__':
    app.run(debug=True)
