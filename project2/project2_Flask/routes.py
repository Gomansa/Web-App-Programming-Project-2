from project2_Flask import app, forms
from flask import request, render_template

@app.route('/', methods = ['GET','POST'])
def search():
    my_form = forms.MoviesForm(request.form)
    if request.method == "POST":

        format_ = request.form['format_'] #this variable is assigned to the option selected by the user
        """TO BE CONTINUED"""

        #get the values provided by the user
        #call the API
        #generate the requested data
        response = forms.generateDataFromAPI(format_)

        return render_template('results.html', response = response)

    return render_template('search.html', form = my_form)
