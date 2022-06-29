from flask import *
app = Flask("myTestTerver")

users = [
  {
    "id": "hari",
    "pwd": "pass"
  },
  {
    "id": "laks",
    "pwd": "1234"
  },
]

def prepare_resp(status, msg):
  return {
    "status": "SUCCESS" if (status == True) else "FAILURE",
     "message": msg
    }


@app.route("/users")
def get_all_users():
  return prepare_resp(True, users)

@app.route("/user/add/<new_user>/<new_pwd>")
def add_user(user,pwd):
  for user in users:
    if (user["id"] != new_user):
      users.append({"id": new_user, "pwd": new_pwd})
      return prepare_resp(True, "added successfully")
  return prepare_resp(False, "user exists")

app.run
