from AQI_WebApp_Flask import app, forms
from flask import request, render_template


@app.route('/', methods=['GET', 'POST'])
def search():
    searchForm = forms.AQIParameters(request.form)
    # If the user makes a post request, save the parameter selected by the user into a variable,
    # call the aqi_parameter function with all the results, then
    # render template parameter_result.html with only the parameter requested by the user.
    if request.method == "POST":
        # User option selected via form is saved here
        parameter_requested = request.form['aqiparameter']
        # User-selected API response snippet saved here
        result = forms.aqi_parameter().get(parameter_requested)
        return render_template('parameter_result.html', result=result, parameter_requested=parameter_requested)
    return render_template('parameter_search.html', form=searchForm)