from RedisCeleryConfig import app, celery
from db import db
from models import *
from datetime import datetime, timedelta

@celery.task
def check_for_new_child_measurement():
    with app.app_context():
        p = Measurementparent.query.all()
        for parent in p:
            c = Measurementchild.query.filter_by(measurementParentId=parent.measurementParentId).order_by(Measurementchild.measurementChildId.desc()).first()
            if c is None:
                continue
            if c.measurementChildTime + timedelta(seconds=(parent.measurementParentFrequencyInterval/parent.measurementParentFrequencyAmount)) < datetime.now():
                project_id = parent.project_id
                project = Project.query.get_or_404(project_id)
                users = project.users
                for user in users:
                    notification = Notification(userId = user.userId, projectId = project_id, message="Det var längesen ni mätte " + parent.measurementParentName + " I förbättringsarbetet \"" + project.title + "\". Snälla mät det snart igen!")
                    db.session.add(notification)
                    db.session.commit()



