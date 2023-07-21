from flask import render_template, request, redirect, url_for
from app import app
from models import Warehouse, Item


@app.route('/')
def index():
    warehouses = Warehouse.get_all()
    return render_template('index.html', warehouses=warehouses)


@app.route('/warehouse/<int:warehouse_id>')
def warehouse_detail(warehouse_id):
    warehouse = Warehouse.get_by_id(warehouse_id)
    items = Item.get_by_warehouse(warehouse_id=warehouse_id)
    return render_template('warehouse_detail.html', warehouse=warehouse, items=items)


@app.route('/warehouse/<int:warehouse_id>/add_item', methods=['GET', 'POST'])
def add_item(warehouse_id):
    warehouse = Warehouse.get_by_id(warehouse_id)
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        item = Item.create(name=name, quantity=quantity, warehouse_id=warehouse_id)
        return redirect(url_for('warehouse_detail', warehouse_id=warehouse_id))
    else:
        return render_template('add_item.html', warehouse=warehouse)


@app.route('/warehouse/<int:warehouse_id>/edit_item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(warehouse_id, item_id):
    warehouse = Warehouse.get_by_id(warehouse_id)
    item = Item.get_by_id(item_id)
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        Item.update(name=name, quantity=quantity, item_id=item_id)
        return redirect(url_for('warehouse_detail', warehouse_id=warehouse_id))
    else:
        return render_template('edit_item.html', warehouse=warehouse)


@app.route('/warehouse/<int:warehouse_id>/delete_item/<int:item_id>', methods=['POST'])
def delete_item(warehouse_id, item_id):
    Item.delete(item_id)
    return redirect(url_for('warehouse_detail', warehouse_id=warehouse_id))


@app.route('/create_warehouse', methods=['GET', 'POST'])
def create_warehouse():
    if request.method == 'POST':
        # Create a new warehouse using data from the form
        warehouse_name = request.form.get('name')
        warehouse_location = request.form.get('location')
        new_warehouse = Warehouse.create(name=warehouse_name, location=warehouse_location)
        # Redirect the user to the new warehouse page
        return redirect(url_for('warehouse_detail', warehouse_id=new_warehouse))
    else:
        # Show a form for creating a new warehouse
        return render_template('create_warehouse.html')


@app.route('/edit_warehouse/<int:warehouse_id>', methods=['GET', 'POST'])
def edit_warehouse(warehouse_id):
    warehouse = Warehouse.get_by_id(warehouse_id)
    if request.method == 'POST':
        # Update the warehouse using data from the form
        warehouse_name = request.form.get('name')
        warehouse_location = request.form.get('location')
        Warehouse.update(warehouse_id, name=warehouse_name, location=warehouse_location)
        # Redirect the user to the updated warehouse page
        return redirect(url_for('warehouse_detail', warehouse_id=warehouse_id))
    else:
        # Show a form for editing the warehouse
        return render_template('edit_warehouse.html', warehouse=warehouse)


@app.route('/delete_warehouse/<int:warehouse_id>', methods=['POST'])
def delete_warehouse(warehouse_id):
    Warehouse.delete(warehouse_id)
    warehouses = Warehouse.get_all()
    return render_template('index.html', warehouses=warehouses)


