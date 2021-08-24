from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from .forms import InputForm
from .geocode import Geocode


from flask import Blueprint

distance_finder = Blueprint('distance_finder', __name__)

log = open(".log", "w")

distance_finder = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
distance_finder.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(distance_finder)

api_key = '47ec0d7d-ea0a-4a20-bcee-66b897ea33bb'


@distance_finder.route('/', methods=['GET', 'POST'])
def index():  # default route
    form = InputForm()  # instantiate the inputform
    message = ""

    if form.validate_on_submit():  # validate the form
        input_address = form.input_address.data  # retrive the input address
        # initialize the geocode object
        origin_geocode = Geocode('Ring road, moscow', api_key)
        input_geocode = Geocode(input_address, api_key)
        if input_geocode.is_valid_address:  # check if the address is valid
            # check if the address inside MKAD
            if origin_geocode.is_located_inside(input_geocode):
                log.write(
                    f"{input_address} is located inside Ring road, Moscow")
                message = f"{input_address} is located inside Ring road, Moscow"
                # render template with message
                return render_template('index.html', form=form, message=message)
            else:
                distance = origin_geocode.get_distance(
                    input_geocode)  # calculate the distance
                log.write(
                    f'The distance between {input_address} and the Ring road, Moscow is {distance:.2f} KM')
                message = f'The distance between {input_address} and the Ring road, Moscow is {distance:.2f} KM'

                # 'form' is the variable name used in this template: index.html
                return render_template('index.html', form=form, message=message)
        else:
            message = f"You've entered invalid input address: {input_address}. Try again!"
            # render template with error message
            return render_template('index.html', form=form, message=message)

    else:
        # render default template
        return render_template('index.html', form=form, message=message)


distance_finder.run(debug=True)