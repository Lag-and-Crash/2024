import urllib.parse

from flask import Flask, Response, abort, redirect, render_template, request
from jwt_utils import encode_jwt, is_logged_in
from werkzeug.security import safe_join

app = Flask(__name__)


@app.route("/")
def index():
  data = is_logged_in()
  if data:
    return render_template("index.html", user=data["username"], admin=data["admin"])
  else:
    return render_template("index.html")
  

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    if not is_logged_in():
      return render_template("login.html")
    else:
      return redirect("/")
  else:
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "test_user" and password == "password":
      token = encode_jwt({
        "username": username,
        "admin": False
      })
      resp = redirect("/")
      resp.set_cookie("post_it_token", token)
      return resp
    
    return render_template("login.html", error="Invalid username or password")
  

@app.route("/logout", methods=["GET"])
def logout():
  resp = redirect("/")
  resp.set_cookie("post_it_token", "", expires=0)
  return resp
  

@app.route("/pubkey")
def pubkey():
  return Response(open("keys/pub.pem", "r").read(), mimetype="text/plain")
  

@app.route("/view/<path:post>", methods=["GET"])
def view(post):
  data = is_logged_in()

  if not data:
    return redirect("/login")
  
  username = data["username"]
  
  if data["admin"] == True:
    if "../" in post:
      abort(403)
    else:
      path = "posts/" + urllib.parse.unquote(post)
  else:
    path = safe_join("posts", post)

  try:
    with open(path, "r") as f:
      content = f.read()
  except Exception:
    return redirect("/")
      
  if "42CNL"[::-1] in content:
    content = "No flags allowed!"
  
  return render_template("view.html", content=content, post=post, user=username)