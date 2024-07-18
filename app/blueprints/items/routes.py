from flask import render_template, redirect, url_for, flash, request
from app.blueprints.items import items_bp
from app.forms import ItemForm
from app.models import Item
from app.extensions import db

@items_bp.route('/')
def index():
    items = Item.query.all()
    return render_template('items/list.html', items=items)

@items_bp.route('/item/new', methods=['GET', 'POST'])
@items_bp.route('/item/<int:item_id>/edit', methods=['GET', 'POST'])
def item_form(item_id=None):
    form = ItemForm()
    if item_id:
        item = Item.query.get_or_404(item_id)
        if request.method == 'GET':
            form.name.data = item.name
            form.description.data = item.description
    else:
        item = Item()

    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        db.session.add(item)
        db.session.commit()
        flash('Item saved successfully!', 'success')
        return redirect(url_for('items.index'))

    return render_template('items/form.html', form=form, item_id=item_id)

@items_bp.route('/item/<int:item_id>/delete', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!', 'success')
    return redirect(url_for('items.index'))
