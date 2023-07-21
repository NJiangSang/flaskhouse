from app import mysql


class Warehouse:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM warehouses")
        result = cur.fetchall()
        cur.close()
        return result

    @staticmethod
    def get_by_id(warehouse_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM warehouses WHERE id = %s", (warehouse_id,))
        result = cur.fetchone()
        cur.close()
        return result

    @staticmethod
    def get_by_name(name):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM warehouses WHERE name = %s", (name,))
        result = cur.fetchone()
        cur.close()
        return result

    @staticmethod
    def create(name, location):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO warehouses (name, location) VALUES (%s, %s)", (name, location))
        mysql.connection.commit()  # 提交事务
        cur.close()
        new_warehouse = Warehouse.get_by_name(name)  # 根据名字获取新建的仓库对象
        return new_warehouse['id']

    @staticmethod
    def update(warehouse_id, name, location):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE warehouses SET name = %s, location = %s WHERE id = %s", (name, location, warehouse_id))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete(warehouse_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM warehouses WHERE id = %s", (warehouse_id,))
        mysql.connection.commit()
        cur.execute("SELECT * FROM warehouses")
        result = cur.fetchall()
        cur.close()
        return result


class Item:
    def __init__(self, id, name, quantity, warehouse_id):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.warehouse_id = warehouse_id

    @staticmethod
    def get_by_warehouse(warehouse_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM items WHERE warehouse_id = %s", (warehouse_id,))
        result = cur.fetchall()
        cur.close()
        return result

    @staticmethod
    def get_by_id(item_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM items WHERE id = %s", (item_id,))
        result = cur.fetchone()
        cur.close()
        return result

    @staticmethod
    def create(name, quantity, warehouse_id):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO items (name, quantity, warehouse_id) VALUES (%s, %s, %s)",
                    (name, quantity, warehouse_id))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def update(item_id, name, quantity):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE items SET name = %s, quantity = %s WHERE id = %s", (name, quantity, item_id))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete(item_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM items WHERE id = %s", (item_id,))
        mysql.connection.commit()
        cur.close()
