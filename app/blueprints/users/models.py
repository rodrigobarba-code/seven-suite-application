# Desc: Users Model for the Users Blueprint

# Importing Required Libraries
import bcrypt
from app.extensions import db
from datetime import datetime
# Importing Required Libraries

# Importing Required Entities
from app.blueprints.users.entities import UserEntity
from app.blueprints.users.entities import UserLogEntity
# Importing Required Entities

# Users Model
class User(db.Model):
    # Table Name
    __tablename__ = 'users'
    # Table Name

    # Columns
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_username = db.Column(db.String(128), nullable=False)
    user_password = db.Column(db.String(128), nullable=False)
    user_name = db.Column(db.String(128), nullable=False)
    user_lastname = db.Column(db.String(128), nullable=False)
    user_privileges = db.Column(db.String(128), nullable=False)
    user_state = db.Column(db.Integer, default=1, nullable=False)
    # Columns

    # Object Representation
    def __repr__(self):
        return f'<User {self.user_id}>'
    # Object Representation

    # Dictionary Representation
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_username': self.user_username,
            'user_password': self.user_password,
            'user_name': self.user_name,
            'user_lastname': self.user_lastname,
            'user_privileges': self.user_privileges,
            'user_state': self.user_state
        }
    # Dictionary Representation

    # Static Methods
    # Add User
    @staticmethod
    def add_user(user: UserEntity):
        try:
            # Encrypt the password
            hashed_password = bcrypt.hashpw(user.user_password.encode('utf-8'), bcrypt.gensalt())
            new_user = User(
                user_id=None,
                user_username=user.user_username,
                user_password=hashed_password,
                user_name=user.user_name,
                user_lastname=user.user_lastname,
                user_privileges=user.user_privileges,
                user_state=user.user_state
            )
            db.session.add(new_user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Add User

    # Update User
    @staticmethod
    def update_user(new_user: UserEntity):
        try:
            # Encrypt the password
            hashed_password = bcrypt.hashpw(new_user.user_password.encode('utf-8'), bcrypt.gensalt())
            old_user = User.query.get(new_user.user_id)
            old_user.user_username = new_user.user_username
            if new_user.user_password != old_user.user_password and new_user.user_password != '':
                old_user.user_password = hashed_password
            old_user.user_name = new_user.user_name
            old_user.user_lastname = new_user.user_lastname
            old_user.user_privileges = new_user.user_privileges
            old_user.user_state = new_user.user_state
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Update User

    # Delete User
    @staticmethod
    def delete_user(user_id: int):
        try:
            user = User.query.get(user_id)
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Delete User

    # Delete All Users
    @staticmethod
    def delete_all_users():
        try:
            User.query.delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Delete All Users

    # Get User
    @staticmethod
    def get_user(user_id: int):
        try:
            user = User.query.get(user_id)
            return UserEntity(
                user_id=user.user_id,
                user_username=user.user_username,
                # Decrypt Password
                user_password=bcrypt.hashpw(user.user_password, bcrypt.gensalt()).decode('utf-8'),
                user_name=user.user_name,
                user_lastname=user.user_lastname,
                user_privileges=user.user_privileges,
                user_state=user.user_state
            )
        except Exception as e:
            return str(e)
    # Get User

    # Get Users
    @staticmethod
    def get_users():
        try:
            users = User.query.all()
            return [UserEntity(
                user_id=user.user_id,
                user_username=user.user_username,
                # Decrypt Password
                user_password=bcrypt.hashpw(user.user_password, bcrypt.gensalt()).decode('utf-8'),
                user_name=user.user_name,
                user_lastname=user.user_lastname,
                user_privileges=user.user_privileges,
                user_state=user.user_state
            ) for user in users]
        except Exception as e:
            return str(e)
    # Get Users
    # Static Methods
# Users Model


# User Log Model
class UserLog(db.Model):
    # Table Name
    __tablename__ = 'users_log'
    # Table Name

    # Columns
    user_log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    user_log_description = db.Column(db.String(256), nullable=True)
    user_log_action = db.Column(db.String(128), nullable=False)
    user_log_table = db.Column(db.String(128), nullable=True)
    user_log_date = db.Column(db.String(128), nullable=False)
    user_log_public_ip = db.Column(db.String(32), nullable=False)
    user_log_local_ip = db.Column(db.String(32), nullable=False)
    # Columns

    # Object Representation
    def __repr__(self):
        return f'<UserLog {self.user_log_id}>'
    # Object Representation

    # Dictionary Representation
    def to_dict(self):
        return {
            'user_log_id': self.user_log_id,
            'fk_user_id': self.fk_user_id,
            'user_log_description': self.user_log_description,
            'user_log_action': self.user_log_action,
            'user_log_table': self.user_log_table,
            'user_log_date': self.user_log_date,
            'user_log_public_ip': self.user_log_public_ip,
            'user_log_local_ip': self.user_log_local_ip
        }
    # Dictionary Representation

    # Static Methods
    # Add User Log
    @staticmethod
    def add_user_log(user_log: UserLogEntity):
        try:
            new_user_log = UserLog(
                user_log_id=None,
                fk_user_id=user_log.fk_user_id,
                user_log_description=user_log.user_log_description,
                user_log_action=user_log.user_log_action,
                user_log_table=user_log.user_log_table,
                user_log_date=user_log.user_log_date,
                user_log_public_ip=user_log.user_log_public_ip,
                user_log_local_ip=user_log.user_log_local_ip
            )
            db.session.add(new_user_log)
            db.session.commit()
            return user_log
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Add User Log

    # Delete From Date Users Log Route
    from datetime import datetime

    # Delete From Date Users Log Route
    @staticmethod
    def delete_from_date_user_log(date_str):
        try:
            # Convert date_str to a date object
            from_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

            # Loop through all user logs and delete those older than from_date
            for user_log in UserLog.query.all():
                # Convert user_log.user_log_date from string to datetime
                user_log_date = datetime.strptime(user_log.user_log_date, '%d/%m/%Y %H:%M:%S')
                if user_log_date <= from_date:
                    db.session.delete(user_log)

            db.session.commit()  # Commit after deleting all the necessary logs
        except Exception as e:
            db.session.rollback()
            print(str(e))
    # Delete From Date Users Log Route

    # Delete All User Log
    @staticmethod
    def delete_all_user_log():
        try:
            UserLog.query.delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Delete All User Log

    # Get User Log
    @staticmethod
    def get_user_logs():
        try:
            user_logs = UserLog.query.order_by(UserLog.user_log_date.desc()).all()
            return [UserLogEntity(
                user_log_id=user_log.user_log_id,
                fk_user_id=user_log.fk_user_id,
                user_log_description=user_log.user_log_description,
                user_log_action=user_log.user_log_action,
                user_log_table=user_log.user_log_table,
                user_log_date=user_log.user_log_date.split(' '),
                user_log_public_ip=user_log.user_log_public_ip,
                user_log_local_ip=user_log.user_log_local_ip
            ) for user_log in user_logs]
        except Exception as e:
            return str(e)
    # Get User Log
    # Static Methods
# User Log Model
