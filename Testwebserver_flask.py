from flask import *

app = Flask("MyTestServer")

users = [
  {
    "id":"badrinath",
    "pwd":"password123"
  },
  {
    "id":"raghu",
    "pwd":"raghu123"
  },  
]

def prepare_resp(status, msg):
  return {
    "status": "SUCCESS" if(status == True) else "FAILED",
    "message": msg
  }
  

@app.route("/users")
def get_all_users():
  return prepare_resp(True,users)
  
  
@app.route("/user/add/<new_user>/<new_pwd>")
def add_user(new_user, new_pwd):
  for user in users:
    if(user["id"] == new_user):
      return prepare_resp(False,"User already exists")
  users.append({
   "id":new_user,
   "pwd":new_pwd
  })
  return prepare_resp(True,"Added successfully")
  
app.run(host="0.0.0.0", port=9999, debug=True)