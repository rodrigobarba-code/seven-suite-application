# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import routers_bp
import workspace
import time, datetime
# Importing Required Libraries

# Importing Models
from workspace.models.model_region import ModelRegion
from workspace.models.model_site import ModelSite
from workspace.models.model_router import ModelRouter
# Importing Models

# Importing Entities
from workspace.models.entities.region import Region
from workspace.models.entities.site import Site
from workspace.models.entities.router import Router
# Importing Entities


@routers_bp.route('/')
def routers():
    routers_list = ModelRouter.get_routers(workspace.db)
    return render_template('public/routers/routers.html', routers_list=routers_list, sites_functions=ModelSite, db=workspace.db)

@routers_bp.route('/add', methods=['GET', 'POST'])
def add_router():
    sites_list = ModelSite.get_sites(workspace.db)
    if request.method == 'POST':
        router = Router(
            router_id=str(int(datetime.datetime.now().timestamp())),
            router_name=request.form['router_name'],
            fk_site_id=int(request.form['fk_site_id']),
            fk_session_id=None,
            fk_ip_address_id=None
        )
        ModelRouter.add_router(workspace.db, router)
        flash('Router Added Successfully', 'success')
        return redirect(url_for('routers.routers'))
    return render_template('public/routers/forms_routers.html', sites_list=sites_list, router=None)

@routers_bp.route('/update/<router_id>', methods=['GET', 'POST'])
def update_router(router_id):
    sites_list = ModelSite.get_sites(workspace.db)
    router = ModelRouter.get_router_by_id(workspace.db, router_id)
    if request.method == 'POST':
        router.router_name = request.form['router_name']
        router.fk_site_id = int(request.form['fk_site_id'])
        ModelRouter.update_router(workspace.db, router)
        flash('Router Updated Successfully', 'warning')
        return redirect(url_for('routers.routers'))
    return render_template('public/routers/forms_routers.html', sites_list=sites_list, router=router)

@routers_bp.route('/delete/<router_id>', methods=['GET', 'POST'])
def delete_router(router_id):
    ModelRouter.delete_router(workspace.db, router_id)
    flash('Router Deleted Successfully', 'danger')
    return redirect(url_for('routers.routers'))