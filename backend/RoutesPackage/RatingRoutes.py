from RoutesInterfaceIn import *

##################################### AppRoute for rating #############################################################


@app.route("/add_new_rating", methods=["POST"])
@cross_origin()
@jwt_required()
def add_new_rating():
    if request.method == "POST":
        print("inside add new rating")
        user_id = get_jwt_identity()['userId']
        data = request.get_json()
        rating = Rating(rating=data["rating"],
                        comment=data["comment"], user=user_id)
        db.session.add(rating)
        db.session.commit()
        return jsonify(rating.serialize())