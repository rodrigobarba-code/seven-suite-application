# Desc: Sites Model for the Sites Blueprint

# Importing Required Libraries
from app.extensions import db
# Importing Required Libraries

# Importing Required Entities
from app.blueprints.sites.entities import SiteEntity
# Importing Required Entities

# Sites Model
class Site(db.Model):
    # Table Name
    __tablename__ = 'sites'
    # Table Name

    # Columns
    site_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_region_id = db.Column(db.Integer, db.ForeignKey('regions.region_id'), nullable=False)
    site_name = db.Column(db.String(128), nullable=False)
    site_segment = db.Column(db.Integer, nullable=False)
    # Columns

    # Relationships
    region = db.relationship('Region', backref=db.backref('sites', lazy=True))
    # Relationships

    # Object Representation
    def __repr__(self):
        return f'<Site {self.site_id}>'
    # Object Representation

    # Dictionary Representation
    def to_dict(self):
        return {
            'site_id': self.site_id,
            'fk_region_id': self.fk_region_id,
            'site_name': self.site_name,
            'site_segment': self.site_segment
        }
    # Dictionary Representation

    # Static Methods
    # Add Site
    @staticmethod
    def add_site(site):
        try:
            db.session.add(
                Site(
                    fk_region_id=site.fk_region_id,
                    site_name=site.site_name,
                    site_segment=site.site_segment
                )
            )
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Add Site

    # Update Site
    @staticmethod
    def update_site(new_site):
        try:
            old_site = db.session.query(Site).get(new_site.site_id)
            old_site.fk_region_id = new_site.fk_region_id
            old_site.site_name = new_site.site_name
            old_site.site_segment = new_site.site_segment
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Update Site

    # Delete Site
    @staticmethod
    def delete_site(site_id):
        try:
            site = Site.query.get_or_404(site_id)
            db.session.delete(site)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Delete Site

    # Delete All Sites
    @staticmethod
    def delete_all_sites():
        try:
            Site.query.delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Delete All Sites

    # Get Site
    @staticmethod
    def get_site(site_id):
        try:
            tmp = Site.query.get_or_404(site_id).to_dict()
            return SiteEntity(
                tmp['site_id'],
                tmp['fk_region_id'],
                tmp['site_name'],
                tmp['site_segment']
            )
        except Exception as e:
            return str(e)
    # Get Site

    # Get Sites
    @staticmethod
    def get_sites():
        try:
            r_list = []
            sites = Site.query.all()
            for site in sites:
                tmp = site.to_dict()
                obj = SiteEntity(
                    tmp['site_id'],
                    tmp['fk_region_id'],
                    tmp['site_name'],
                    tmp['site_segment']
                )
                r_list.append(obj)
            return r_list
        except Exception as e:
            return str(e)
    # Get Sites
    # Static Methods
# Site Model
