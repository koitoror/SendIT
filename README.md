[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# SendIT
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories. .

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

- Install node dependecies to run tests `npm install`
- Run tests `npm test`

Run `index.html` file in your browser

# UI link for GH-PAGES

```
https://koitoror.github.io/SendIT/UI/
```

**How should this be manually tested?**
The tests are written in jest testing framework and assetion library. To test

- `git clone https://github.com/koitoror/SendIT.git`
- `cd SendIT`
- Install node dependecies to run tests `npm install`
- Run tests `npm test`
