# #LettuceBeFriends

A web application that lets people create healthy meal events to meet interesting people in small groups

[Live Site @ https://lettuce-be-friends.herokuapp.com/](https://lettuce-be-friends.herokuapp.com/)

********

## Technical Specifications

* Flask application using SQLAlchemy for database management
	* Implemented CRUD on User and Event resources with RESTful routing
* Templates built with Jinja2 and HTML, with styling using Bootstrap and CSS
* Password encryption done with Bcrypt

********

## Development Timeline

#### Tuesday May 30

* Set up Flask app with Users resource and RESTful routes **_(done)_**
* Set up initial database migration **_(done)_**
* Basic styling with logo, splash image, font pairing, and color scheme **_(done)_**
* Initial deploy to Heroku **_(done)_**
* Add to Rithm repo **_(done)_**

#### Wednesday May 31

* Set up user log in & signup & log out **_(done)_**
* Make favicon **_(done)_**
* Set up second resource Events with its RESTful routes 
* Attendees list on Events objects (1:M relationship)

#### Thursday June 1

* Add alert before deleting; “Are you sure you want to delete this event?” 
* Create a way for attendees to sign up for each event and stop them once event is full
* Security; make sure personal info (email, cell #) is not accessible to anyone outside of attendees leading up to each event

#### Friday June 2

* Validation of data; make forms more intuitive to fill out 
* Add drop-downs calendar that you can also type in (like facebook events) for date and time of events
* Try out Google Maps search for restaurant venues & maps API to display location
* Final deploy

#### Extras

* Create a photo cropper for profile pictures to be a square with a maximum upload size
* Convert CSS to SCSS
* Make layout with Flexbox rather than just 12 col grid
* Add CSS animations & transitions for event display and buttons
* Try out way to send email reminder to all attendees and/or text message reminder to all attendees

********

## How to set up and run this app locally:

* (writing this up later)

********

## Appendix

* [Project Guidelines](https://github.com/rithmschool/fullstack_project) - Rithm School Week 5

* Check out more details about plans for the app, questions, & progress [here](https://docs.google.com/document/d/1UcY4zTgfRUQolKyFGeEFAckOhiQEANiOMKMgdrafxm4/edit?usp=sharing)
