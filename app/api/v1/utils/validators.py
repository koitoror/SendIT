import re


def validate_user_data(user):
    """ this funtion validates the user data """

    user['username'] = user['username'].lower()

    if user['username'] == '':
        return {'warning': 'username is a required field'}, 400

    # Check for empty email
    elif user['email'] == '':
        return {'warning': 'email is a required field'}, 400

    # Check for empty password
    elif user['password'] == '':
        return {'warning': 'password is a required field'}, 400

    elif user['password'] == 'password':
        return {'warning': "password cannot be 'password'"}, 400

    elif user['password'].strip(' ').isdigit():
        return {'warning': 'password should be alphanumeric'}, 400

    elif user['password'] != user['confirm']:
        return {'warning': 'password mismatch!'}, 400

    # Check for a valid user name
    if not re.match(r'^[a-zA-Z0-9_.+-]+$', user['username'].strip(' ')):
        return {'warning': 'Enter a valid username'}, 400

    if user['username'].strip(' ').isdigit():
        return {'warning': 'Enter a non digit username'}, 400

    # Check for a valid email
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                    user['email'].strip(' ')):
        return {'warning': 'Enter a valid email address'}, 400

    # check for a valid password
    if not user["password"].strip():
        return {"warning": "Enter a valid password"}, 400

    # Check for large/long inputs
    if len(user['username']) > 15:
        return {'warning': 'username is too long'}, 400

    elif len(user['email']) > 40:
        return {'warning': 'email is too long'}, 400

    elif len(user['password']) < 6:
        return {'warning': 'password requires atlest 6 characters'}, 400


def validate_parcel_data(parcel):
    """ this funtion validates the parcel data """

    # Check for empty parcel_name
    if parcel['parcel_name'] == ' ':
        return {'warning': 'parcel_name is a required field'}, 400

    # Check for empty pickup_location
    elif parcel['pickup_location'] == ' ':
        return {'warning': 'pickup_location is a required field'}, 400

    # Check for empty destination_location
    elif parcel['destination_location'] == ' ':
        return {'warning': 'destination_location is a required field'}, 400

    # check for a valid parcel_name
    if parcel['parcel_name'].strip(' ').isdigit():
        return {'warning': 'Enter a non digit parcel_name'}, 400

    if not parcel["parcel_name"].strip():
        return {"warning": "Enter a valid parcel_name"}, 400

    # check for valid pickup_location
    if parcel['pickup_location'].strip(' ').isdigit():
        return {'warning': 'Enter non digit pickup_location'}, 400

    if not parcel["pickup_location"].strip():
        return {"warning": "Enter valid pickup_location"}, 400

    # check for valid destination_location
    if parcel['destination_location'].strip(' ').isdigit():
        return {'warning': 'Enter non digit destination_location'}, 400

    if not parcel["destination_location"].strip():
        return {"warning": "Enter valid destination_location"}, 400

    # Check for large/long inputs
    if len(parcel['parcel_name']) > 40:
        return {'warning': 'parcel_name is too long'}, 400


def validate_update_parcel(parcel, data):
    """ this funtion validates the updated parcel data """

    # Check for empty cancel_order
    if data['cancel_order'] == '':
        data['cancel_order'] = parcel['cancel_order']

    # Check for empty destination_location
    if data['destination_location'] == '':
        data['destination_location'] = parcel['destination_location']

    # check for valid destination_location
    if data['destination_location'].strip(' ').isdigit():
        return {'warning': 'Enter non digit destination_location'}, 400

    if not data["destination_location"].strip():
        return {"warning": "Enter valid destination_location"}, 400

    # Check for large/long inputs
    if len(data['destination_location']) > 40:
        return {'warning': 'destination_location is too long'}, 400


def validate_update_parcel_admin(parcel, data):
    """ this funtion validates the updated parcel data for admin"""

    # Check for empty status
    if data['status'] == '':
        data['status'] = parcel['status']

    # Check for empty present_location
    if data['present_location'] == '':
        data['present_location'] = parcel['present_location']

    # check for a valid status
    if data['status'].strip(' ').isdigit():
        return {'warning': 'Enter a non digit status'}, 400

    if not data["status"].strip():
        return {"warning": "Enter a valid status"}, 400

    # check for valid present_location
    if data['present_location'].strip(' ').isdigit():
        return {'warning': 'Enter non digit present_location'}, 400

    if not data["present_location"].strip():
        return {"warning": "Enter valid present_location"}, 400

    # Check for large/long inputs
    if len(data['present_location']) > 40:
        return {'warning': 'present_location is too long'}, 400
