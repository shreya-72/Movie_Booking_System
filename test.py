import requests

# Define the base URL for the Flask app
url = 'http://127.0.0.1:3306'


def test_insert_theaters():
  data_list = [
  {
    "Theater_ID": "116",
    "Location": "Hinjewadi",
    "Ratings": 4,
    "No_of_screens": 14
  },
  {
    "Theater_ID": "117",
    "Location": "Shivajinagar",
    "Ratings": 5,
    "No_of_screens": 11
  }
  ]

  
  for data in data_list:
    response = requests.post(url, json=data)
    response = requests.post(f"{url}/entity", json = data)
    
    # Print the status code and response for each request
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Data: {response.json()}")



def test_update_theaters():
    theater_data = {
        "Theater_ID": 112,
        "Location": "Updated Aundh_1",
        "Ratings": 5,
        "No_of_screens": 12
    }

    try:
        response = requests.put(f"{url}/entity", json=theater_data)
        
        # Check if the response status is successful
        if response.status_code == 200:
            print("Request successful!")
            print(response.json())  # Print the response data
        else:
            print(f"Request failed with status code {response.status_code}")
            print(response.json())  # Print the error details

    except Exception as e:
        print(f"An error occurred: {e}")


def test_delete_theaters():
  data_list = [
  {
    "Theater_ID": "116",
    "Location": "Hinjewadi",
    "Ratings": 4,
    "No_of_screens": 14
  }
  # ,
  # {
  #   "Theater_ID": "117",
  #   "Location": "Shivajinagar",
  #   "Ratings": 5,
  #   "No_of_screens": 11
  # }
  ]

  for data in data_list:
    response = requests.delete(f"{url}/entity", json = data)
    
    # Print the status code and response for each request
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Data: {response.json()}")


def test_display_theaters():
    # Hardcoded query parameters to test the endpoint
    query_params = {
        "Location": "Pune",
        "Ratings": 5
    }

    try:
        # Send a GET request to the endpoint with query parameters
        response = requests.get(f"{url}/entity", params=query_params)
        
        # Check if the response status is successful
        if response.status_code == 200:
            print("Request successful! Theaters matching the criteria:")
            print(response.json())  # Print the response data
        else:
            print(f"Request failed with status code {response.status_code}")
            print(response.json())  # Print the error details

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    test_update_theaters()
    # test_delete_theaters()
    # test_insert_theaters()
    # test_display_theaters()
