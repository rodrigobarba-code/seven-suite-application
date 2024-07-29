# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request, jsonify
from . import regions_bp
from app.decorators import RequirementsDecorators as restriction

# Importing Required Libraries

# Importing Required Entities
from app.blueprints.regions.entities import RegionEntity
# Importing Required Entities

# Importing Required Models
from app.blueprints.regions.models import Region


# Importing Required Models

# Regions Main Route
@regions_bp.route('/', methods=['GET'])
@restriction.login_required
def regions():
    region_list = Region.get_regions()  # Get all regions
    return render_template(
        'regions/regions.html',  # Render the regions template
        region_list=region_list, region=None  # Pass the region list and None to the template
    )


# Regions Main Route

# Regions Add Route
@regions_bp.route('/add', methods=['GET', 'POST'])
@restriction.login_required
def add_region():
    if request.method == 'POST':  # If the request method is POST
        try:  # Try to add the region
            region = RegionEntity(  # Create a RegionEntity object
                region_id=None,
                region_name=request.form['region_name']
            )
            Region.add_region(region)  # Add the region
            flash('Region added successfully!', 'success')  # Flash a success message
        except Exception as e:  # If an exception occurs
            flash(str(e), 'danger')  # Flash an error message
        return redirect(url_for('regions.regions'))  # Redirect to the regions route
    return render_template(
        'regions/form_regions.html',  # Render the form_regions template
        region=None  # Pass None to the template
    )


# Regions Add Route

# Regions Update Route
@regions_bp.route('/update/<int:region_id>', methods=['GET', 'POST'])
@restriction.login_required
def update_region(region_id):
    if request.method == 'POST':  # If the request method is POST
        try:  # Try to update the region
            region = RegionEntity(  # Create a RegionEntity object
                region_id=region_id,
                region_name=request.form['region_name']
            )
            Region.update_region(region)  # Update the region
            flash('Region updated successfully!', 'success')  # Flash a success message
        except Exception as e:  # If an exception occurs
            flash(str(e), 'danger')  # Flash an error message
        return redirect(url_for('regions.regions'))  # Redirect to the regions route
    region = Region.get_region(region_id)
    return render_template(
        'regions/form_regions.html',  # Render the form_regions template
        region=region  # Pass the region to the template
    )


# Regions Update Route

# Regions Delete Route
@regions_bp.route('/delete/<int:region_id>', methods=['GET'])
@restriction.login_required
def delete_region(region_id):
    try:  # Try to delete the region
        Region.delete_region(region_id)  # Delete the region
        flash('Region deleted successfully!', 'success')  # Flash a success message
    except Exception as e:  # If an exception occurs
        flash(str(e), 'danger')  # Flash an error message
    return redirect(url_for('regions.regions'))  # Redirect to the regions route
# Regions Delete Route
