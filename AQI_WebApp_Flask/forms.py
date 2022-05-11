from AQI_WebApp_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField


class AQIParameters(FlaskForm):
    # Create selectfield with choices in the form value:label
    aqiparameter = SelectField(choices=[["coordinates", "coordinates"], ["temperatureC", "temperatureC"],
                                        ["pressure", "pressure"], ["humidity", "humidity"], ["aqius", "aqius"]])


def aqi_parameter():
    # Build IQAir API key
    url = "https://api.airvisual.com/v2/nearest_city?key="
    aqi_key = main_functions.read_from_file("AQI_WebApp_Flask/JSON_Files/aqi_key.json")
    aqi_key = aqi_key['aqi_key']
    url2 = url + aqi_key

    # Save API JSON response to system
    request_json = requests.get(url2).json()
    main_functions.save_to_file(request_json, "AQI_WebApp_Flask/JSON_Files/aqi.json")
    air_quality_index = main_functions.read_from_file("AQI_WebApp_Flask/JSON_Files/aqi.json")

    # From the json file, access and store each of the following properties,
    # and concatenate latitude and longitude to create a coordinate variable.
    latitude = air_quality_index['data']['location']['coordinates'][0]
    longitude = air_quality_index['data']['location']['coordinates'][1]
    coordinates = str(latitude) + ', ' + str(longitude)
    temperatureC = air_quality_index['data']['current']['weather']['tp']
    pressure = air_quality_index['data']['current']['weather']['pr']
    humidity = air_quality_index['data']['current']['weather']['hu']
    aqius = air_quality_index['data']['current']['pollution']['aqius']

    parameters = {'coordinates': coordinates,
                  'temperatureC': str(temperatureC),
                  'pressure': str(pressure),
                  'humidity': str(humidity),
                  'aqius': str(aqius)}
    return parameters
