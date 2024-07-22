# Desc: Region Model for the Region Blueprint

# Importing Required Libraries
from app.extensions import db
# Importing Required Libraries

# Importing Required Entities
from app.blueprints.regions.entities import RegionEntity
# Importing Required Entities

# Region Model
class Region(db.Model):
    # Table Name
    __tablename__ = 'regions'
    # Table Name

    # Columns
    region_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    region_name = db.Column(db.String(128), nullable=False)
    # Columns

    # Object Representation
    def __repr__(self):
        return f'<Region {self.region_id}>'
    # Object Representation

    # Dictionary Representation
    def to_dict(self):
        return {
            'region_id': self.region_id,
            'region_name': self.region_name
        }
    # Dictionary Representation

    # Static Methods
    # Add Region
    @staticmethod
    def add_region(region):
        try:
            db.session.add(
                Region(
                    region_name=region.region_name
                )
            )
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Add Region

    # Update Region
    @staticmethod
    def update_region(new_region):
        try:
            old_region = db.session.query(Region).get(new_region.region_id)
            old_region.region_name = new_region.region_name
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Update Region

    # Delete Region
    @staticmethod
    def delete_region(region_id):
        try:
            region = Region.query.get_or_404(region_id)
            db.session.delete(region)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Delete Region

    # Delete All Regions
    @staticmethod
    def delete_all_regions():
        try:
            Region.query.delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    # Delete All Regions

    # Get Region
    @staticmethod
    def get_region(region_id):
        try:
            tmp = Region.query.get_or_404(region_id).to_dict()
            return RegionEntity(
                tmp['region_id'],
                tmp['region_name']
            )
        except Exception as e:
            return str(e)
    # Get Region

    # Get Regions
    @staticmethod
    def get_regions():
        try:
            r_list = []
            regions = Region.query.all()
            for region in regions:
                tmp = region.to_dict()
                obj = RegionEntity(tmp['region_id'], tmp['region_name'])
                r_list.append(obj)
            return r_list
        except Exception as e:
            return str(e)
    # Get Regions
    # Static Methods
# Region Model
