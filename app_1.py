from custom_class.app_config import FlaskAppConfig
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

from custom_class.theater import theater_class

config = FlaskAppConfig() 
app = config.app      
mysql = config.mysql 

@app.route('/theater', methods=['GET', 'POST', 'PUT', 'DELETE'])
def theater():
    obj = theater_class()
    table_name = "theater"

    if request.method == 'POST':
        # Insert theater record
        try: 
            data = request.get_json()

            return obj.insert_entity(data, table_name )


        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'PUT':
        # Update theater record
        try:
            data = request.get_json()

            return obj.update_entity(data, table_name)


        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'DELETE':
        # Delete theater record
        try:
            data = request.get_json()
            return obj.delete_entity(data, table_name)

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'GET':
        try:
            #display theater record
            query_params = request.args.to_dict()
            
            return obj.display_entity(query_params, table_name)
            
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3306)



# # Update a theater record
# @app.route('/update_theater', methods=['PUT'])
# def update_theater():
#     try:
#         data = request.get_json()
#         theater_id = data.get('Theater_ID')
#         location = data.get('Location')
#         ratings = data.get('Ratings')
#         no_of_screens = data.get('No_of_screens')

#         cur = mysql.connection.cursor()

#         query = """
#         UPDATE theater 
#         SET location = %s, ratings = %s, no_of_screens = %s 
#         WHERE theater_id = %s
#         """
#         cur.execute(query, (location, ratings, no_of_screens, theater_id))
#         mysql.connection.commit()

#         cur.close()

#         return jsonify({"message": "Theater updated successfully!"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# # Delete a theater record
# @app.route('/delete_theater', methods=['DELETE'])
# def delete_theater():
#     try:
#         data = request.get_json()
#         theater_id = data.get('Theater_ID')

#         cur = mysql.connection.cursor()

#         query = "DELETE FROM theater WHERE theater_id = %s"
#         cur.execute(query, (theater_id,))
#         mysql.connection.commit()

#         cur.close()

#         return jsonify({"message": "Theater deleted successfully!"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500



# # Display specific entries
# @app.route('/display_theater', methods=['GET'])
# def display_specific_entries():
#     try:
#         query_params = request.args.to_dict()
#         conditions = " AND ".join([f"{key} = %s" for key in query_params.keys()])
#         values = tuple(query_params.values())

#         cur = mysql.connection.cursor()

#         query = f"SELECT * FROM theater WHERE {conditions}"
#         cur.execute(query, values)
#         results = cur.fetchall()
#         column_names = [desc[0] for desc in cur.description]

#         cur.close()

#         return jsonify([dict(zip(column_names, row)) for row in results]), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# #to insert orders
# @app.route('/insert_theater', methods=['POST'])
# def insert_theater():
#     try:
#         data = request.get_json()
#         theater_id = data.get('Theater_ID')
#         location = data.get('Location')
#         ratings = data.get('Ratings')
#         no_of_screens = data.get('No_of_screens')

#         cur = mysql.connection.cursor()

#         query = "INSERT INTO theater (theater_id, location,ratings,no_of_screens) VALUES (%s, %s,%s, %s)"
#         cur.execute(query, (theater_id, location, ratings, no_of_screens))

#         mysql.connection.commit()

#         cur.close()

#         return jsonify({"message": "Order added successfully!"}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=3306)