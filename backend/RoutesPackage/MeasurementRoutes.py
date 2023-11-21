from RoutesInterfaceIn import *

##################################### AppRoute for adding Measurement #############################################################

@app.route("/add_new_measurement/<int:project_id>", methods=["POST"])
@cross_origin()
def add_new_measurement(project_id):

    if request.method == "POST":

        data = request.get_json()
        newMeasurement = Measurementparent(measurementParentName=data["name"], measurementParentUnit=data["unit"], measurementParentFrequencyAmount = data["frequencyAmount"], measurementParentFrequencyInterval = data["frequencyInterval"], project_id=project_id)
        project = Project.query.get_or_404(project_id)
        project.measurementsChildren.append(newMeasurement)
        db.session.add(newMeasurement)
        db.session.commit()
        return jsonify(Measurementparent.serialize(newMeasurement))
    
@app.route("/get_all_measurements/<int:project_id>", methods=['GET'])
@cross_origin()
def get_all_measurements(project_id):
    if request.method == 'GET':
        measurement = []
        project = Project.query.get_or_404(project_id)
        measurements = project.measurementsChildren
        for m in measurements:
            measurement.append(Measurementparent.serialize(m))
        return jsonify(measurement)
    
@app.route("/measurement/<int:measurement_id>", methods=["GET", "PUT", "DELETE"])
@cross_origin()
def edit_delete_get_measurement(measurement_id):
    measurement = Measurementparent.query.get_or_404(measurement_id)
    if request.method == 'GET':
        return jsonify(Measurementparent.serialize(measurement))
    elif request.method == 'PUT':
        data = request.get_json()
        keys_list = data.keys()
        if 'name' in keys_list:
            measurement.measurementParentName = data["name"]
        if 'unit' in keys_list:
            measurement.measurementParentUnit = data["unit"]
        if 'frequencyAmount' in keys_list:
            measurement.measurementParentFrequencyAmount = data["frequencyAmount"]
        if 'frequencyInterval' in keys_list:
            measurement.measurementParentFrequencyInterval = data["frequencyInterval"]
        if 'project' in keys_list:
            measurement.project = data["project"]
        db.session.commit()
        return jsonify(Measurementparent.serialize(measurement))
    elif request.method == 'DELETE':
        children = measurement.measurementChilds
        for child in children:
            db.session.delete(child)
        db.session.delete(measurement)
        db.session.commit()
        return jsonify(Measurementparent.serialize(measurement))
    
@app.route("/add_new_measurement_child/<int:measurement_id>", methods=["POST"])
@cross_origin()
def add_new_measurement_child(measurement_id):
    
        if request.method == "POST":
    
            data = request.get_json()
            newMeasurement = Measurementchild(measurementChildValue=data["value"], measurementParentId=measurement_id)
            measurement = Measurementparent.query.get_or_404(measurement_id)
            measurement.measurementChilds.append(newMeasurement)
            db.session.add(newMeasurement)
            db.session.commit()
            return jsonify(Measurementchild.serialize(newMeasurement))
        
@app.route("/get_all_measurements_child/<int:measurement_id>", methods=['GET'])
@cross_origin()
def get_all_measurements_child(measurement_id):
    if request.method == 'GET':
        measurement = []
        measurementParent = Measurementparent.query.get_or_404(measurement_id)
        measurements = measurementParent.measurementChilds
        for m in measurements:
            measurement.append(Measurementchild.serialize(m))
        return jsonify(measurement)