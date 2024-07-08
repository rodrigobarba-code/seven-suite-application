# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import routers_bp
import workspace
# Importing Required Libraries

# Importing Models
from workspace.models.model_region import ModelRegion
from workspace.models.model_site import ModelSite
# Importing Models

# Importing Entities
from workspace.models.entities.region import Region
from workspace.models.entities.site import Site
from workspace.models.entities.router import Router
# Importing Entities


@routers_bp.route('/')
def routers():
    return render_template('public/routers/routers.html')

@routers_bp.route('/add', methods=['GET', 'POST'])
def add_router():
    sites_list = ModelSite.get_sites(workspace.db)
    if request.method == 'POST':
        router = Router
    return render_template('public/routers/forms_routers.html', sites_list=sites_list, site=None)