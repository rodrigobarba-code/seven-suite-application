# Description: Regions Routes for the Region Blueprint

# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request, jsonify, session
# Importing Required Libraries

# Importing Required Decorators
from app.decorators import RequirementsDecorators as restriction
# Importing Required Decorators

# Importing Required Entities
from app.blueprints.regions.entities import RegionEntity
# Importing Required Entities

# Importing Required Models
from app.blueprints.regions.models import Region
# Importing Required Models

from . import regions_bp  # Import the regions Blueprint
from app.blueprints.users.functions import users_functions as functions  # Import the users functions object


# Regions Main Route
@regions_bp.route('/', methods=['GET'])
@restriction.login_required  # Need to be logged in
def regions():
    try:
        region_list = Region.get_regions()  # Get all regions on the database
        return render_template(
            'regions/regions.html',  # Render the regions template
            region_list=region_list, region=None  # Pass the region list and None to the template
        )
    except Exception as e:  # If an exception occurs
        flash(str(e), 'danger')  # Flash an error message
        return redirect(url_for('regions.regions'))  # Redirect to the regions route


# Regions Main Route

# Regions Add Route
@regions_bp.route('/add', methods=['GET', 'POST'])
@restriction.login_required  # Need to be logged in
@restriction.admin_required  # Need to be an admin
def add_region():
    if request.method == 'POST':  # If the request method is POST
        try:  # Try to add the region
            region = RegionEntity(  # Create a RegionEntity object
                region_id=int(),  # Set the region ID
                region_name=request.form['region_name']  # Set the region name
            )
            Region.add_region(region)  # Add the region
            functions.create_log(session['user_id'], 'Region added', 'INSERT', 'regions')  # Create a log
            flash('Region added successfully', 'success')  # Flash a success message
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
@restriction.login_required  # Need to be logged in
@restriction.admin_required  # Need to be an admin
def update_region(region_id):
    if request.method == 'POST':  # If the request method is POST
        try:  # Try to update the region
            region = RegionEntity(  # Create a RegionEntity object
                region_id=region_id,  # Set the region ID
                region_name=request.form['region_name']  # Set the region name
            )
            Region.update_region(region)  # Update the region
            functions.create_log(session['user_id'], 'Region Updated', 'UPDATE', 'regions')  # Create a log
            flash('Region was updated successfully', 'success')  # Flash a success message
        except Exception as e:  # If an exception occurs
            flash(str(e), 'danger')  # Flash an error message
        return redirect(url_for('regions.regions'))  # Redirect to the regions route
    try:  # Try to get the region
        region = Region.get_region(region_id)  # Get the region
        return render_template(
            'regions/form_regions.html',  # Render the form_regions template
            region=region  # Pass the region to the template
        )
    except Exception as e:  # If an exception occurs
        flash(str(e), 'danger')  # Flash an error message
        return redirect(url_for('regions.regions'))  # Redirect to the regions route


# Regions Update Route

# Regions Delete Route
@regions_bp.route('/delete/<int:region_id>', methods=['GET'])
@restriction.login_required  # Need to be logged in
@restriction.admin_required  # Need to be an admin
def delete_region(region_id):
    try:  # Try to delete the region
        Region.delete_region(region_id)  # Delete the region
        functions.create_log(session['user_id'], 'Region Deleted', 'DELETE', 'regions')  # Create a log
        flash('Region deleted successfully', 'success')  # Flash a success message
    except Exception as e:  # If an exception occurs
        flash(str(e), 'danger')  # Flash an error message
    return redirect(url_for('regions.regions'))  # Redirect to the regions route


# Regions Delete Route

# Regions Bulk Delete Route
@regions_bp.route('/delete/bulk', methods=['POST'])
@restriction.login_required  # Need to be logged in
@restriction.admin_required  # Need to be an admin
def bulk_delete_region():
    data = request.get_json()
    regions_ids = data.get('items_ids', [])
    try:
        flag = 0
        for region_id in regions_ids:
            Region.delete_region(region_id)
            flag += 1
        flash('Regions Deleted Successfully', 'success')
        functions.create_log(session['user_id'], 'Regions Deleted', 'DELETE', 'regions')
        return jsonify({'message': 'Users deleted successfully'}), 200
    except Exception as e:
        flash(str(e), 'danger')
        return jsonify({'message': 'Failed to delete users', 'error': str(e)}), 500


# Regions Bulk Delete Route

# Regions Delete All Route
@regions_bp.route('/delete/all', methods=['GET'])
@restriction.login_required  # Need to be logged in
@restriction.admin_required  # Need to be an admin
def delete_all_regions():
    try:  # Try to delete all regions
        Region.delete_all_regions()  # Delete all regions
        functions.create_log(session['user_id'], 'All Regions Deleted', 'DELETE', 'regions')  # Create a log
        flash('All Regions Deleted Successfully', 'success')  # Flash a success message
    except Exception as e:
        flash(str(e), 'danger')
    return redirect(url_for('regions.regions'))
# Regions Delete All Route
