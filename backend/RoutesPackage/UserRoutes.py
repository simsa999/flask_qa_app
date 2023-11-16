from RoutesInterfaceIn import *

##################################### AppRoute for user #############################################################


# TODO: Now the route doesnt take password into account. Might not need route, since we have signup route. Incase of needing to use this route, add password to the route.
@app.route("/add_new_user", methods=["POST"])
@cross_origin()
def add_user():
    if request.method == "POST":
        data = request.get_json()
        keys_list = data.keys()
        if 'role' in keys_list:
            if data['role'] == Role.user.value:
                newUser = User(name=data["name"], email=data["email"],
                               role=Role.user, unit=data["unit"], jobTitle=data["jobTitle"])
            else:
                newUser = User(name=data["name"], email=data["email"],
                               role=Role.admin, unit=data["unit"], jobTitle=data["jobTitle"])
        else:
            newUser = User(name=data["name"], email=data["email"],
                           unit=data["unit"], jobTitle=data["jobTitle"])

        db.session.add(newUser)
        db.session.commit()
        return jsonify(User.serialize(newUser))

# GET ALL USERS


@app.route("/get_all_users", methods=["GET"])
@cross_origin()
def get_users():
    if request.method == 'GET':
        user = []
        users = User.query.all()
        for u in users:
            user.append(User.serialize(u))
        return jsonify(user)

# EDIT; DELETE OR GET a specific user


@app.route("/user/<int:user_id>", methods=["GET", "PUT", "DELETE"])
@cross_origin()
def edit_delete_get_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'GET':
        return jsonify([User.serialize(user)])
    elif request.method == 'PUT':
        data = request.get_json()
        keys_list = data.keys()
        if 'name' in keys_list:
            user.name = data["name"]
        if 'email' in keys_list:
            user.email = data["email"]
        if 'profileIcon' in keys_list:
            user.profileIcon = data["profileIcon"]
        if 'unit' in keys_list:
            user.unit = data['unit']
        if 'jobTitle' in keys_list:
            user.jobTitle = data["jobTitle"]
        if 'role' in keys_list:
            if data['role'] == 'User':
                user.role = Role.user
            else:
                user.role = Role.admin
        db.session.commit()
        return jsonify([User.serialize(user)])
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify("DELETE COMPLETE")

################################## AppRoute for Authentication #########################################################


@app.route("/signup", methods=["POST"])
def signup():
    if request.method == "POST":
        data = request.get_json()
        existing_user = User.query.filter_by(email=data["email"]).first()
        if existing_user:
            return jsonify({"message": "Email already in use"}), 400
        keys_list = data.keys()
        if 'role' in keys_list:
            if data['role'] == Role.admin.value:
                role = Role.admin
            else:
                role = Role.user

        new_user = User(
            name=data["name"],
            email=data["email"],
            role=role,
            unit=data["unit"],
            jobTitle=data["jobTitle"],

        )
        # new_user.set_password(data["password"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.serialize()), 200


@app.route("/login", methods=["POST"])
@cross_origin()
def login():
    if request.method == "POST":
        data = request.get_json()
        user = User.query.get(data["user_id"])
        if user:
            token = create_access_token(identity=user.serialize())
            return jsonify(dict(user.serialize(), token=token))
        else:
            return jsonify({"message": "Invalid credentials"}), 401