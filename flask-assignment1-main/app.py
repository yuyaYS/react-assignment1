from flask import Flask
from flask import request
from flask import jsonify,make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'it will return the item based on the route!'



# @app.route('/users')
# def get_users():
#    search_username = request.args.get('name') #accessing the value of parameter 'name'
#    if search_username :
#       subdict = {'users_list' : []}
#       for user in users['users_list']:
#          if user['name'] == search_username:
#             subdict['users_list'].append(user)
#       return subdict
#    return users

# @app.route('/users/<id>')
# def get_user(id):
#    if id :
#       for user in users['users_list']:
#         if user['id'] == id:
#            return user
#       return ({})
#    return users

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         return filter_name_and_job(search_username,search_job)
      elif search_username:
         return filter_name(search_username)
      return users  

   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True),201
      #resp = jsonify({"201 response"}),201
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

    

@app.route("/users/<id>", methods=['GET','DELETE'])
def get_usersById(id):
   if id:
        for user in users['users_list']:
           if user['id']== id:
              if request.method =='GET':
                  return user
              elif request.method == 'DELETE':
                  users['users_list'].remove(user)
                  resp = jsonify(),204
                  return resp
        res = jsonify({"could not fund the item given id"}),404
        return res
   return users


def filter_name_and_job(name,job):
      subdict ={'users_list':[]}
      for user in users['users_list']:
         if user['name']== name and user['job']==job:
            subdict['users_list'].append(user)
      return subdict


def filter_name(name):
      subdict ={'users_list':[]}
      #search_username = request.args.get('name') #accessing the value of parameter 'name'
      for user in users['users_list']:
         if user['name']== name:
            subdict['users_list'].append(user)
      return subdict


users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}