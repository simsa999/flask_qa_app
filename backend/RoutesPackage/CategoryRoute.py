from RoutesInterfaceIn import *

##################################### AppRoute for adding category #############################################################
@app.route("/add_new_category", methods=["POST"])
@cross_origin()
def add_new_category():
    if request.method == "POST":
        data = request.get_json()
        if data["categoryName"] == ProjectCategory.option1.value:
            category = Category(categoryName=ProjectCategory.option1)
        if data["categoryName"] == ProjectCategory.option2.value:
            category = Category(categoryName=ProjectCategory.option2)
        if data["categoryName"] == ProjectCategory.option3.value:
            category = Category(categoryName=ProjectCategory.option3)
        if data["categoryName"] == ProjectCategory.option4.value:
            category = Category(categoryName=ProjectCategory.option4)
        db.session.add(category)
        db.session.commit()
        return jsonify(Category.serialize(category))


@app.route("/get_all_categories", methods=["GET"])
@cross_origin()
def add_newcategory():
    if request.method == "GET":
        category = []
        categories = Category.query.all()
        for c in categories:
            category.append(Category.serialize(c))
        return jsonify(category)
