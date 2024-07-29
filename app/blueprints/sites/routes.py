# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request, jsonify
from . import sites_bp
from app.decorators import RequirementsDecorators as restriction
# Importing Required Libraries

# Importing Required Entities
from app.blueprints.sites.entities import SiteEntity
from app.blueprints.regions.entities import RegionEntity
# Importing Required Entities

# Importing Required Models
from app.blueprints.sites.models import Site
from app.blueprints.regions.models import Region


# Importing Required Models

# Sites Main Route
@sites_bp.route('/', methods=['GET'])
@restriction.login_required
def sites():
    site_list = Site.get_sites()  # Get the site list
    region_functions = Region()  # Create a Region object
    return render_template(
        'sites/sites.html',  # Render the sites template
        region_functions=region_functions,  # Pass the region object to the template
        site_list=site_list,  # Pass the site list to the template
        site=None  # Pass None to the template
    )


# Sites Main Route

# Sites Add Route
@sites_bp.route('/add', methods=['GET', 'POST'])
@restriction.login_required
def add_site():
    if request.method == 'POST':  # If the request method is POST
        try:  # Try to add the site
            site = SiteEntity(  # Create a SitesEntity object
                site_id=None,
                site_name=request.form['site_name'],
                fk_region_id=request.form['fk_region_id'],
                site_segment=request.form['site_segment']
            )
            Site.add_site(site)  # Add the site
            flash('Site added successfully!', 'success')  # Flash a success message
        except Exception as e:  # If an exception occurs
            flash(str(e), 'danger')  # Flash an error message
        return redirect(url_for('sites.sites'))  # Redirect to the sites route
    region_list = Region.get_regions()  # Get the region list
    return render_template(
        'sites/form_sites.html',  # Render the form_sites template
        region_list=region_list,  # Pass the region list to the template
        site=None  # Pass None to the template
    )


# Sites Add Route

# Sites Update Route
@sites_bp.route('/update/<int:site_id>', methods=['GET', 'POST'])
@restriction.login_required
def update_site(site_id):
    if request.method == 'POST':  # If the request method is POST
        try:  # Try to update the site
            site = SiteEntity(  # Create a SitesEntity object
                site_id=site_id,
                site_name=request.form['site_name'],
                fk_region_id=request.form['fk_region_id'],
                site_segment=request.form['site_segment']
            )
            Site.update_site(site)  # Update the site
            flash('Site updated successfully!', 'success')  # Flash a success message
        except Exception as e:  # If an exception occurs
            flash(str(e), 'danger')  # Flash an error message
        return redirect(url_for('sites.sites'))  # Redirect to the sites route
    site = Site.get_site(site_id)
    region_list = Region.get_regions()
    return render_template(
        'sites/form_sites.html',  # Render the form_sites template
        region_list=region_list,  # Pass the region list to the template
        site=site  # Pass the site to the template
    )


# Sites Update Route

# Sites Delete Route
@sites_bp.route('/delete/<int:site_id>', methods=['GET'])
@restriction.login_required
def delete_site(site_id):
    try:  # Try to delete the site
        Site.delete_site(site_id)  # Delete the site
        flash('Site deleted successfully!', 'success')  # Flash a success message
    except Exception as e:  # If an exception occurs
        flash(str(e), 'danger')  # Flash an error message
    return redirect(url_for('sites.sites'))  # Redirect to the sites route
# Sites Delete Route
