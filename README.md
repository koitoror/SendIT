[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Build Status](https://travis-ci.com/koitoror/SendIT.svg?branch=ft-parcels-endpoints-161738123)](https://travis-ci.com/koitoror/SendIT)
[![Coverage Status](https://coveralls.io/repos/github/koitoror/SendIT/badge.svg?branch=ft-parcels-endpoints-161738123)](https://coveralls.io/github/koitoror/SendIT?branch=ft-parcels-endpoints-161738123)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)

# SendIT
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories. .

![Home Image](https://raw.github.com/Koitoror/Parcels/SendIT.jpg)

### Required Features
1.	Users can create an account and log in. 
2.	Users can create a parcel delivery order. 
3.	Users can change the destination of a parcel delivery order. 
4.	Users can cancel a parcel delivery order. 
5.	Users can see the details of a delivery order. 
6.	Admin can change the status and present location of a parcel delivery order.

### Optional Features
1. The application should display a Google Map with Markers showing the pickup location
and the destination.
2. The application should display a Google Map with a line connecting both Markers (pickup
location and the destination).
3. The application should display a Google Map with computed travel distance and journey
duration between the pickup location and the destination.
4. The user gets real-time email notification when Admin changes the status of their parcel.
5. The user gets real-time email notification when Admin changes the present location their
parcel.


### NB: 
1.	The user can only cancel or change the destination of a parcel delivery when the parcel’s status is yet to be marked as delivered. 
2.	Only the user who created the parcel delivery order can cancel the order.  

## Installation
For the UI designs to work you need a working browser like Google Chrome or Mozilla Firefox

Clone the repository into your local environment

```
$ git clone https://github.com/koitoror/SendIT.git
```

Switch to the GH-PAGES branch
```
$ git checkout gh-pages
```

Change directory into SendIT
```
cd SendIT/UI
```

## Built With

* HTML5
* CSS3

Run `index.html` file in your browser

# UI link for GH-PAGES

```
https://koitoror.github.io/SendIT/UI/
```

## API Installation
To set up SendIT API, make sure that you have python3, postman and pip installed.

Use [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) for an isolated working environment.

Clone the Repo into a folder of your choice
```
git clone https://github.com/koitoror/SendIT.git
```

Create a virtual enviroment.
```
virtualenv venv --python=python3
```

Navigate to api folder.
```
cd SendIT
```

Install the packages.
```
pip3 install -r requirements.txt
```

Set environment variables for 

> `SECRET_KEY` is your secret key

> `FLASK_CONFIG` is the enviroment you are running on. Should be either `Production`, `Development` or `Testing`. NOTE: its case sensitive

> `PORT` the default port for postgresql service which 5432

> `HOST` which is localhost



## API Usage

To get the app running...

```bash
$ python run.py run
```

Open root path in your browser to test the endpoints. 
You can also use Postman or any other agent to test the endpoints

## Test

To run your tests use

```bash
$ python run.py test or 
$ pytest --cov
```

To test endpoints manually fire up postman and run the following endpoints


### Auth Endpoints
**EndPoint** | **Functionality**
--- | ---
POST  `/api/v1/auth/signup` | Register a user
POST  `/api/v1/auth/login` | Logs in a user


###  Endpoints
**EndPoint** | **Functionality**
--- | ---
GET  `/api/v1/parcels` | Fetch all parcel delivery orders
POST  `/api/v1/parcels` | Create a parcel delivery order
GET  `/api/v1/parcels/<parcelId>` | Fetch a single parcel delivery order 
DELETE  `/api/v1/parcels/<parcelId>` | Delete a parcel delivery order
PUT  `/api/v1/parcels/<parcelId>` | Update a parcel delivery order by admin
PUT  `/api/v1/parcels/<parcelId>/cancel` | Cancel a parcel delivery order by user
GET  `/api/v1/users/<userId>/parcels` | Fetch all parcel delivery orders


# API Documentation
Once app server is running you can view API documentation locally from
```
http://127.0.0.1:5000/
```

Once app server is running you can view * VERSION 1 * on HEROKU the [API documentation here](https://send-it-ke.herokuapp.com)
