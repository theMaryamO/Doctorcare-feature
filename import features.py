import requests
import json

# define your API endpoint for analytics tracking
API_ENDPOINT = 'https://myhospitalcloud.com/myhospital-cloud/'

# define your application's unique identifier
APP_ID = 'adm.myhospitalcloud.com'

# define function for tracking events
def track_event(event_name, event_data):
    # construct the data payload
    data = {
        'app_id': APP_ID,
        'event_name': event_name,
        'event_data': event_data
    }
    
    # make POST request for  API endpoint
    response = requests.post(API_ENDPOINT, json.dumps(data))
    
    # handle any errors
    if response.status_code != 200:
        raise Exception('Analytics tracking failed with status code: {}'.format(response.status_code))

# sample usage
track_event('login', {'user_id': 1234})
----------------------------------------------------------------



# Define the URL of the analytics endpoint
analytics_url = "https://myhospitalcloud.com/features/"

# Define the function to send analytics data to the endpoint
def send_analytics_data(data):
    headers = {"Content-Type": "application/json"}
    response = requests.post(analytics_url, json=data, headers=headers)
    if response.status_code != 200:
        print("Failed to send analytics data")

# Define a sample function that performs an action in the application
def perform_action():
    # Code to perform the action goes here
    print("Action performed")
    
    # Send analytics data to the endpoint
    data = {"action": "perform_action"}
    send_analytics_data(data)
