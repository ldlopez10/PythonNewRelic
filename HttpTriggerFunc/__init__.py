import logging
import azure.functions as func
import requests
import random
import json

import newrelic.agent
newrelic.agent.initialize('./newrelic.ini')
newrelic.agent.register_application(name='Python-NewRelic-Local', timeout=1)


# @newrelic.agent.background_task()
@newrelic.agent.web_transaction(name="HttpTriggerFunc")
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        generate_random_error()
        cat_fact = get_cat_fact()
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully, so here is your cat fact: \n \n{cat_fact}")
    else:
        generate_random_error()
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
        

@newrelic.agent.external_trace('library', 'https://cat-fact.herokuapp.com/facts', 'get')
def get_cat_fact():
    # Replace 'YOUR_EXTERNAL_API_URL' with the actual URL of the external API you want to call.
    external_api_url = 'https://cat-fact.herokuapp.com/facts'

    try:
        # Call the external API
        logging.warning("Calling an External API for Cat-Facts...")
        response = requests.get(external_api_url)
        

        # Check if the API call was successful (status code 200)
        if response.status_code == 200:
            
            json_response = json.loads(response.content)
            
            random_index = generate_random_index(json_response)
            
            cat_fact = json_response[random_index]['text']
            
            logging.critical(f"We found a cat fact: {cat_fact}")
            return cat_fact
            
        else:
            # Log the error if the API call was not successful
            logging.error(f"Failed to fetch data from the external API. Status Code: {response.status_code} \n External URL: {external_api_url}")
            raise Exception(f"Failed to fetch data from the external API. status_code: {response.status_code}")
            # return f"Failed to fetch data from the external API. status_code: {response.status_code}"

    except requests.RequestException as e:
        # Log the exception if there was an error during the API call
        logging.exception("Error occurred while calling the external API: %s", str(e))
        raise Exception(f"Error occurred while calling the external API. status_code: {response.status_code}")

@newrelic.agent.function_trace(name="generate_random_index")
def generate_random_index(array):
    # Generate a random index within the range of the array's length
    random_index = random.randint(0, len(array) - 1)
    return random_index

@newrelic.agent.function_trace(name="generate_random_error")
def generate_random_error():
    # Simulate a 10% chance of generating an error
    if random.random() < 0.10:
        logging.error("Logging Randomly generated Error")
        raise Exception ("This is a random simulated error.")
