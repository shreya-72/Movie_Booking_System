from .abstract import AbstractClass
from .app_config import FlaskAppConfig
from flask import Flask, jsonify
from flask_mysqldb import MySQL



class entity_class(AbstractClass):
    def __init__(self): 
        config = FlaskAppConfig() 
        self.app = config.app      
        self.mysql = config.mysql  


    
    def update_entity(self,data, table_name):
        try:
            # data = request.get_json()
            keys = list(data.keys())

            id_column = keys[0]  # Get the first key
            id_value = data[id_column]  # Get the value corresponding to the first key

            updated_column = keys[1]
            updated_value = data[updated_column]

            # theater_id = data.get('Theater_ID')
            # location = data.get('Location')
            # ratings = data.get('Ratings')
            # no_of_screens = data.get('No_of_screens')

            cur = self.mysql.connection.cursor()

            query = f"""
            UPDATE {table_name}
            SET {updated_column} = %s
            WHERE {id_column} = %s
            """           
            cur.execute(query, (updated_value, id_value))
            self.mysql.connection.commit()

            cur.close()

            return jsonify({"message": f"{table_name} updated successfully!"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500



    def delete_entity(self,data, table_name):
        try:
 
            id_column = next(iter(data))  # Get the first key
            id_value = data[id_column]  # Get the value corresponding to the first key

            cur = self.mysql.connection.cursor()

            query = f"DELETE FROM {table_name} WHERE {id_column} = %s"

            cur.execute(query, (id_value,))
            self.mysql.connection.commit()

            cur.close()

            return jsonify({"message": f"{table_name} deleted successfully!"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500



    def display_entity(self, query_params, table_name):
        try:
            conditions = " AND ".join([f"{key} = %s" for key in query_params.keys()])
            values = tuple(query_params.values())

            cur = self.mysql.connection.cursor()

            # query = f"SELECT * FROM theater WHERE {conditions}"
            query = f"SELECT * FROM {table_name} WHERE {conditions}"
            cur.execute(query, values)
            results = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]

            cur.close()

            return jsonify([dict(zip(column_names, row)) for row in results]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500



    def insert_entity(self, data, table_name):
        try:
            columns = []
            values = []

            for key, value in data.items():
                columns.append(key)
                values.append(value)

            placeholders = ','.join(['%s'] * len(columns))
            query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"

            cur = self.mysql.connection.cursor()
            cur.execute(query, tuple(values))

            self.mysql.connection.commit()
            cur.close()

            return jsonify({"message": f"{table_name} added successfully!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500



