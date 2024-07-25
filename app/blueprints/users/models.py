# Desc: Users Model for the Users Blueprint

# Importing Required Libraries
import bcrypt
from app.extensions import db
# Importing Required Libraries

# Importing Required Entities
from app.blueprints.users.entities import UserEntity
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
