# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import regions_bp
import workspace
# Importing Required Libraries

# Importing Models
from workspace.models.model_region import ModelRegion
# Importing Models

# Importing Entities
from workspace.models.entities.region import Region


# Importing


# Main Route
@regions_bp.route('/')
def regions():
    regions_list = ModelRegion.get_regions(workspace.db)
    return render_template('public/regions/regions.html', regions_list=regions_list)


# Main Route


# Add Region Route
@regions_bp.route('/add', methods=['GET', 'POST'])
def add_region():
    if request.method == 'POST':
        region = Region(
            region_id=0,
            region_name=request.form['region_name'],
        )
        ModelRegion.add_region(workspace.db, region)
        flash('Region Added Successfully', 'success')
        return redirect(url_for('regions.regions'))
    return render_template('public/regions/form_regions.html', region=None)
# Add Region Route

# Update Region Route
@regions_bp.route('/update/<int:region_id>', methods=['GET', 'POST'])
def update_region(region_id):
    region = ModelRegion.get_region_by_id(workspace.db, region_id)
    if request.method == 'POST':
        region.region_name = request.form['region_name']
        ModelRegion.update_region(workspace.db, region)
        flash('Region Updated Successfully', 'success')
        return redirect(url_for('regions.regions'))
    return render_template('public/regions/form_regions.html', region=region)
# Update Region Route

# Delete Region Route
@regions_bp.route('/delete/<int:region_id>', methods=['GET', 'POST'])
def delete_region(region_id):
    try:
        ModelRegion.delete_region(workspace.db, region_id)
        flash('Region Deleted Successfully', 'success')
    except Exception as e:
        if 'foreign key constraint' in str(e):
            flash('Error in deleting Region: Region is being used in Site', 'danger')
    return redirect(url_for('regions.regions'))
# Delete Region Route
