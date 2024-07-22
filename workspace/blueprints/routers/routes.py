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
from workspace.models.model_session_information import ModelSessionInformation
# Importing Models

# Importing Entities
from workspace.models.entities.region import Region
from workspace.models.entities.site import Site
from workspace.models.entities.router import Router
from workspace.models.entities.session_information import SessionInformation


# Importing Entities


@routers_bp.route('/')
def routers():
    routers_list = ModelRouter.get_routers(workspace.db)
    return render_template('public/routers/routers.html', routers_list=routers_list, sites_functions=ModelSite,
                           db=workspace.db)


@routers_bp.route('/add', methods=['GET', 'POST'])
def add_router():
    if request.method == 'POST':
        try:
            router = Router(
                router_id="",
                router_name=request.form['router_name'],
                router_description="",
                router_brand="",
                router_model="",
                fk_site_id=int(request.form['fk_site_id']),
                fk_session_id=""
            )
            ModelRouter.add_router(workspace.db, router)
            return redirect(url_for('routers.routers'))
        except Exception as ex:
            flash('An error occurred while adding the router','danger')
            print(ex)
            return redirect(url_for('routers.routers'))

    sites_list = ModelSite.get_sites(workspace.db)
    return render_template('public/routers/forms_routers.html', sites_list=sites_list, router=None, router_session=None)




@routers_bp.route('/update/<router_id>', methods=['GET', 'POST'])
def update_router(router_id):
    sites_list = ModelSite.get_sites(workspace.db)
    router = ModelRouter.get_router_by_id(workspace.db, router_id)
    router_session = ModelSessionInformation.get_session_information_by_id(workspace.db, router.fk_session_id)
    if request.method == 'POST':
        router.router_name = request.form['router_name']
        router.fk_site_id = int(request.form['fk_site_id'])
        ModelRouter.update_router(workspace.db, router)
        flash('Router Updated Successfully', 'warning')
        return redirect(url_for('routers.routers'))
    return render_template('public/routers/forms_routers.html', sites_list=sites_list, router=router, router_session=router_session)


@routers_bp.route('/delete/<router_id>/', methods=['GET', 'POST'])
@routers_bp.route('/delete/<router_id>/<session_id>', methods=['GET', 'POST'])
def delete_router(router_id, session_id=None):
    if session_id is not None:
        ModelRouter.delete_router(workspace.db, router_id, session_id)
    else:
        ModelRouter.delete_router(workspace.db, router_id, None)
    flash('Router Deleted Successfully', 'danger')
    return redirect(url_for('routers.routers'))
