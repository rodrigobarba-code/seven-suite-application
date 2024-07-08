# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import sites_bp
import workspace
# Importing Required Libraries


# Importing Models
from workspace.models.model_region import ModelRegion
from workspace.models.model_site import ModelSite
# Importing Models


# Importing Entities
from workspace.models.entities.region import Region
from workspace.models.entities.site import Site
# Importing Entities


# Main Route
@sites_bp.route('/')
def sites():
    sites_list = ModelSite.get_sites(workspace.db)
    return render_template('public/sites/sites.html', db=workspace.db, region_functions=ModelRegion, sites_list=sites_list)
# Main Route


# Add Site Route
@sites_bp.route('/add', methods=['GET', 'POST'])
def add_site():
    regions_list = ModelRegion.get_regions(workspace.db)
    if request.method == 'POST':
        site = Site(
            site_id=0,
            fk_region_id=int(request.form['fk_region_id']),
            site_name=request.form['site_name'],
            site_segment=int(request.form['site_segment'])
        )
        ModelSite.add_site(workspace.db, site)
        flash('Site Added Successfully', 'success')
        return redirect(url_for('sites.sites'))
    return render_template('public/sites/form_sites.html', regions_list=regions_list, site=None)
# Add Site Route

# Update Site Route
@sites_bp.route('/update/<int:site_id>', methods=['GET', 'POST'])
def update_site(site_id):
    site = ModelSite.get_site_by_id(workspace.db, site_id)
    regions_list = ModelRegion.get_regions(workspace.db)
    if request.method == 'POST':
        site = Site(
            site_id=site_id,
            fk_region_id=int(request.form['fk_region_id']),
            site_name=request.form['site_name'],
            site_segment=int(request.form['site_segment'])
        )
        ModelSite.update_site(workspace.db, site)
        flash('Site Updated Successfully', 'success')
        return redirect(url_for('sites.sites'))
    return render_template('public/sites/form_sites.html', regions_list=regions_list, site=site)
# Update Site Route


# Delete Site Route
@sites_bp.route('/delete/<int:site_id>', methods=['GET', 'POST'])
def delete_site(site_id):
    ModelSite.delete_site(workspace.db, site_id)
    flash('Site Deleted Successfully', 'success')
    return redirect(url_for('sites.sites'))
# Delete Site Route