from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, RadioField
import requests
from project2_Flask import main_functions

class MoviesForm(FlaskForm):
    format_ = StringField('Movie Title')

def generateDataFromAPI(option):
    my_key_dict = main_functions.read_from_file("project2_Flask/JSON_Documents/api_keys.json")
    my_key = my_key_dict["my_ny_key"]

    print(my_key)

    final_url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=" + option + "&api-key=" + my_key

    print(final_url)

    response = requests.get(final_url).json()

    print(response)

    main_functions.save_to_file(response,"project2_Flask/JSON_Documents/response.json")

    response_dict = main_functions.read_from_file("project2_Flask/JSON_Documents/response.json")
    """From the response dictionary, you need to filter the data requested by the user"""
    results = []

    for i in response_dict["results"]:
        results.append({
            "display_title": i["display_title"],
            "summary_short": i["summary_short"],
            "url_": i["link"]["url"]
        })

    return results
