# Desc: Routers Model for the Routers Blueprint

# Importing Required Libraries
from app.extensions import db
# Importing Required Libraries

# Importing Required Entities
from app.blueprints.routers.entities import RouterEntity
# Importing Required Entities

# Router Model
class Router(db.Model):
    # Table Name
    __tablename__ = 'routers'
    # Table Name

    # Columns
    router_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    router_name = db.Column(db.String(128), nullable=False)
    router_description = db.Column(db.String(256), nullable=False)
    router_brand = db.Column(db.String(128), nullable=False)
    router_model = db.Column(db.String(128), nullable=False)
    fk_site_id = db.Column(db.Integer, db.ForeignKey('sites.site_id'), nullable=False)
    router_ip = db.Column(db.String(16), nullable=False)
    router_mac = db.Column(db.String(32), nullable=False)
    router_username = db.Column(db.String(128), nullable=False)
    router_password = db.Column(db.String(128), nullable=False)
    allow_scan = db.Column(db.Integer, nullable=False, default=0)
    # Columns

    # Relationships
    site = db.relationship('Site', backref=db.backref('routers', lazy=True))
    # Relationships

    # Object Representation
    def __repr__(self):
        return f'<Router {self.router_id}>'
    # Object Representation

    # Dictionary Representation
    def to_dict(self):
        return {
            'router_id': self.router_id,
            'router_name': self.router_name,
            'router_description': self.router_description,
            'router_brand': self.router_brand,
            'router_model': self.router_model,
            'fk_site_id': self.fk_site_id,
            'router_ip': self.router_ip,
            'router_mac': self.router_mac,
            'router_username': self.router_username,
            'router_password': self.router_password,
            'allow_scan': self.allow_scan
        }
    # Dictionary Representation

    # Static Methods
    # Add Router
    @staticmethod
    def add_router(router: RouterEntity):
        try:
            router = Router(
                router_name=router.router_name,
                router_description=router.router_description,
                router_brand=router.router_brand,
                router_model=router.router_model,
                fk_site_id=router.fk_site_id,
                router_ip=router.router_ip,
                router_mac=router.router_mac,
                router_username=router.router_username,
                router_password=router.router_password,
                allow_scan=router.allow_scan
            )
            db.session.add(router)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Add Router

    # Update Router
    @staticmethod
    def update_router(new_router: RouterEntity):
        try:
            old_router = Router.query.get(new_router.router_id)
            old_router.router_name = new_router.router_name
            old_router.router_description = new_router.router_description
            old_router.router_brand = new_router.router_brand
            old_router.router_model = new_router.router_model
            old_router.fk_site_id = new_router.fk_site_id
            old_router.router_ip = new_router.router_ip
            old_router.router_mac = new_router.router_mac
            old_router.router_username = new_router.router_username
            old_router.router_password = new_router.router_password
            old_router.allow_scan = new_router.allow_scan
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Static Methods
    # Update Router

    # Delete Router
    @staticmethod
    def delete_router(router_id):
        try:
            router = Router.query.get(router_id)
            db.session.delete(router)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Delete Router

    # Get Router
    @staticmethod
    def get_router(router_id):
        tmp = Router.query.get(router_id)
        router = RouterEntity(
            router_id=tmp.router_id,
            router_name=tmp.router_name,
            router_description=tmp.router_description,
            router_brand=tmp.router_brand,
            router_model=tmp.router_model,
            fk_site_id=tmp.fk_site_id,
            router_ip=tmp.router_ip,
            router_mac=tmp.router_mac,
            router_username=tmp.router_username,
            router_password=tmp.router_password,
            allow_scan=tmp.allow_scan
        )
        return router
    # Get Router

    # Get All Routers
    @staticmethod
    def get_all_routers():
        r_list = []
        routers = Router.query.all()

        for router in routers:
            tmp = RouterEntity(
                router_id=router.router_id,
                router_name=router.router_name,
                router_description=router.router_description,
                router_brand=router.router_brand,
                router_model=router.router_model,
                fk_site_id=router.fk_site_id,
                router_ip=router.router_ip,
                router_mac=router.router_mac,
                router_username=router.router_username,
                router_password=router.router_password,
                allow_scan=router.allow_scan
            )
            r_list.append(tmp)
        return r_list
    # Get All Routers
# Router Model
