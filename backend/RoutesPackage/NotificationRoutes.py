from RoutesInterfaceIn import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import threading
import traceback
from sqlalchemy.event import listens_for

@app.route("/get_notifications", methods=['GET'])
@cross_origin()
@jwt_required()
def get_notifications():
    if request.method == 'GET':
        userId = get_jwt_identity()['userId']
        notifications = Notification.query.filter_by(userId=userId).filter_by(read=False)
        notifications = [notification.serialize() for notification in notifications]
        notifications.sort(key=lambda x: x['timestamp'], reverse=True)
        return jsonify(notifications)
    
@app.route("/add_notification/<int:userId>/<int:projectId>", methods=['POST'])
@cross_origin()
def add_notification(userId, projectId):
    if request.method == 'POST':
        user = User.query.get(userId)
        project = Project.query.get(projectId)

        if user and project:
            notification = Notification(userId=userId, projectId=projectId, message=request.json['message'])
            db.session.add(notification)
            db.session.commit()
            return jsonify(notification.serialize())
        return jsonify({"error": "Something went wrong"})
        
    
@app.route("/notification/<int:notificationId>", methods=['DELETE'])
@cross_origin()
@jwt_required()
def delete_notification(notificationId):
    if request.method == 'DELETE':
        user = User.query.get(get_jwt_identity()['userId'])
        notification = Notification.query.get(notificationId)
        notification.read = True
        if user.userId != notification.userId:
            return jsonify({"error": "You are not authorized to delete this notification"})
        db.session.add(notification)
        db.session.commit()
        return jsonify(notification.serialize())
    
@listens_for(Notification, 'after_insert')
def send_notification_email_listener(mapper, connection, target):
        send_notification_email_async(target)


def send_notification_email_async(target):
    thread = threading.Thread(target=send_notification_email, args=(target,))
    thread.start()


def send_notification_email(target):
    user_id = target.userId
    project_id = target.projectId
    message = target.message
    with app.app_context():
        user = User.query.get(user_id)
        project = Project.query.get(project_id)
        if user.email:
            try:
                # send email
                from_name = "4Bättringsarbete"
                from_email = "4Battringsarbete@gmail.com"
                email_password = "gxfgtphimmajzdcl"
                to_email = user.email

                with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()

                    smtp.login(from_email, email_password)

                    msg = MIMEMultipart()
                    msg['From'] = Header(f"{from_name}", 'utf-8')
                    msg['To'] = to_email
                    msg['Subject'] = Header(f"Notis " + project.title, 'utf-8')
                    msg.attach(MIMEText(message, 'html', 'utf-8'))

                    smtp.sendmail(from_email, to_email, msg.as_string())
            except Exception as e:
                # Log the exception instead of printing directly
                print(f"Error sending email: {e}")
                traceback.print_exc()