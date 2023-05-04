from app import create_app, db
from app.models import Employee

config_name = 'testing'
app = create_app(config_name)
with app.app_context():
    db.create_all()
    # create admin user
    admin = Employee(username="admin", password="heslo", is_admin=True)
    db.session.add(admin)
    db.session.commit()