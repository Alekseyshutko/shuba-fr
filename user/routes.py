import requests
from config import Config
from flask import Blueprint, redirect, render_template, url_for, request, session
from user.utils import access, get_current_user, create_user, access_token_request
from user.form import RegisterUserForm, LoginForm
from order.routes import CREATE_ORDER
from user.models import RegisterUser
from user.permissions import login_required, profile_required


user_blueprint = Blueprint(
    "user",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/user",
)


@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterUserForm()
    if request.method == "POST":
        user = create_user(**form.data)
        print(user)

        return render_template("login.html", form=form)
    return render_template("register.html", form=form)


@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        auth = access(**form.data)
        print(auth)
        auth.store_in_session()
        user = get_current_user()
        user.store_in_session()
        tokens = access_token_request(
            email=form.email.data,
            password=form.password.data,
        )
        session["access"] = tokens["access"]
        session["refresh"] = tokens["refresh"]
        session.modified = True
        return redirect(url_for('index'))
    return render_template("login.html", form=form)


@user_blueprint.route("/logout", methods=["GET"])
def logout():
    print("LOGOUT")
    session.clear()
    return redirect(url_for("index"))


@user_blueprint.route('/me', methods=["GET", "POST"])
def user():
    user = session.get("user")
    order = requests.get(CREATE_ORDER).json()
    orderlist = []

    for i in range(len(order)):
        if order[i]['user'] == user['id']:
            orderlist.append(order[i])

    if user is None:
        user = get_current_user()
        user.store_in_session()
    return render_template('user.html', user=user, orderlist=orderlist)
