# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request, jsonify
from . import regions_bp

# Importing Required Entities
from app.blueprints.region.entities import RegionEntity
# Importing Required Entities

# Importing Required Models
from app.blueprints.region.models import Region
# Importing Required Models

# Regions Main Route
@regions_bp.route('/', methods=['GET'])
def regions():
    region_list = Region.get_regions()
    return render_template('regions/regions.html', region_list=region_list)
# Regions Main Route
