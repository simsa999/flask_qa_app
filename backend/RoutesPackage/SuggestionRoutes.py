from RoutesInterfaceIn import *

##################################### AppRoute for Suggestions #############################################################
@app.route("/add_new_suggestion", methods=["POST"])
@cross_origin()
@jwt_required()
def add_new_suggestion():
    user_id = get_jwt_identity()['userId']
    User.query.get_or_404(user_id)  # only to get 404 if the user do not exist
    if request.method == "POST":
        data = request.get_json()
        print(data)
        newSuggestion = Suggestion(name=data["title"], descriptionImportance=data["descriptionImportance"], creator=user_id)
        keys_list = data.keys()
        if 'descriptionImpact' in keys_list:
            newSuggestion.descriptionImpact = data["descriptionImpact"]
        if 'descriptionRequirements' in keys_list:
            newSuggestion.descriptionRequirements = data["descriptionRequirements"]
        if 'status' in keys_list:
            if data["status"] == 'Draft':
                newSuggestion.status = statusSuggestion.draft
            if data["status"] == 'Published':
                newSuggestion.status = statusSuggestion.published
            if data["status"] == 'Archived':
                newSuggestion.status = statusSuggestion.archived
        db.session.add(newSuggestion)
        if 'categories' in keys_list:
            for category in data["categories"]:
                newSuggestion.categories.append(Category.query.get_or_404(category))
        db.session.commit()
        return jsonify({"suggestionId": newSuggestion.suggestionId})



@app.route("/get_all_suggestions", methods=['GET'])
@cross_origin()
def get_all_suggestions():
    if request.method == 'GET':
        suggestion = []
        suggestions = Suggestion.query.all()
        for s in suggestions:
            suggestion.append(Suggestion.serialize(s))
        return jsonify(suggestion)


@app.route("/suggestion/<int:id>", methods=['PUT', 'GET', 'DELETE'])
@cross_origin()
def edit_delete_get_suggestion(id):
    suggestion = Suggestion.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify([Suggestion.serialize(suggestion)])
    elif request.method == 'PUT':
        data = request.get_json()
        sugg = Suggestion.query.get_or_404(id)
        return jsonify([Suggestion.serialize(put_suggestion(data, sugg, None))])
    elif request.method == 'DELETE':
        db.session.delete(suggestion)
        db.session.commit()
        return jsonify("DELETE COMPLETE")
    
    
@app.route("/get_all_utkast_by_user", methods=["GET"])
@cross_origin()
@jwt_required()
def get_all_utkast():
    if request.method == 'GET':
        user = get_jwt_identity()
        user = user['userId']
        suggestionsQuery = Suggestion.query.filter(Suggestion.creator == user, Suggestion.status == statusSuggestion.draft)
        suggestions = []
        for s in suggestionsQuery:
            suggestions.append(Suggestion.serialize(s))
        return jsonify(suggestions)

@app.route("/get_all_published_suggestions", methods=["GET"])
@cross_origin()
def get_all_published():
    if request.method == 'GET':
        suggestionsQuery = Suggestion.query.filter(Suggestion.status == statusSuggestion.published)
        suggestions = []
        for s in suggestionsQuery:
            suggestions.append(Suggestion.serialize(s))
        return jsonify(suggestions)

def put_suggestion(data, suggestion, stat):
    
    keys_list = data.keys()
    if 'title' in keys_list:
        suggestion.name = data["title"]
    if 'descriptionImportance' in keys_list:
        suggestion.descriptionImportance = data["descriptionImportance"]
    if 'descriptionImpact' in keys_list:
        suggestion.descriptionImpact = data["descriptionImpact"]
    if 'descriptionRequirements' in keys_list:  
        suggestion.descriptionRequirements = data["descriptionRequirements"]
    if 'status' in keys_list:
        if data["status"] == 'Draft':
            suggestion.status = statusSuggestion.draft
        if data["status"] == 'Published':
            suggestion.status = statusSuggestion.published
        if data["status"] == 'Archived':
            suggestion.status = statusSuggestion.archived
    if 'categories' in keys_list:
        #Get all ids of the categories in keyslist
        new_category_ids = []  
        for category in data["categories"]:
            new_category_ids.append(category.get("categoryId"))       
        print(new_category_ids)
        # Create a copy of the current categories list
        current_categories = list(suggestion.categories)

        # Remove categories that are not in the new list
        for category in current_categories:
            if category.categoryId not in new_category_ids:
                suggestion.categories.remove(category)

        # Add categories that are not already there
        for category_id in new_category_ids:
            if category_id not in [c.categoryId for c in suggestion.categories]:
                category = Category.query.get_or_404(category_id)
                suggestion.categories.append(category)
    if stat:
        suggestion.status = stat
    db.session.commit()
    return suggestion

def create_project_from_suggestion(suggestion):
    newProject = Project(title=suggestion.name, creator_id=suggestion.creator, importance=suggestion.descriptionImportance,
                             difference=suggestion.descriptionImpact, requirements=suggestion.descriptionRequirements, measurements=suggestion.descriptionRequirements,
                             outcome=suggestion.descriptionRequirements, unit='N/A',
                             how_often='N/A', status=statusProject.utkast, categories = suggestion.categories)
    return newProject

@app.route("/start_project_from_suggestion", methods=['POST', 'PUT'])
@cross_origin()
@jwt_required()
def start_project_from_suggestion():
    user_id = get_jwt_identity()['userId']
    User.query.get_or_404(user_id)
    data = request.get_json()
    print(data)
    if request.method == 'PUT':
        sugg = Suggestion.query.get_or_404(data["suggestionId"])
        suggestion = put_suggestion(data, sugg, statusSuggestion.archived)
        newProject = create_project_from_suggestion(suggestion)
        db.session.add(newProject)
        db.session.add(suggestion)
        db.session.commit() 
    elif request.method == 'POST':
        suggestion = Suggestion(name=data["title"], descriptionImportance=data["descriptionImportance"], descriptionImpact = data["descriptionImpact"], descriptionRequirements = data["descriptionRequirements"], creator=user_id, status = statusSuggestion.archived)
        if data['categories']:
            for category in data["categories"]:
                suggestion.categories.append(Category.query.get_or_404(category.get("categoryId")))
        newProject = create_project_from_suggestion(suggestion)
        db.session.add(newProject)
        db.session.add(suggestion)
        db.session.commit()
    notification = Notification(userId=user_id, projectId=newProject.projectId, message="Ditt förslag \"" + suggestion.name + "\" har blivit ett förbättringsarbete")
    db.session.add(notification)
    db.session.commit()

    return jsonify({"projectId": newProject.projectId})