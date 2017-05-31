# #LettuceBeFriends

A web application that lets people create healthy meal events to meet interesting people in small groups

[Live Site @ https://lettuce-be-friends.herokuapp.com/](https://lettuce-be-friends.herokuapp.com/)

## Technical Specifications

* Flask application using SQLAlchemy for database management
	* Implmeneted CRUD on User and Event resources with RESTful routing
* Templates built with Jinja2 and HTML, with styling using Bootstrap and CSS
* Password encryption done with Bcrypt

## Development Timeline

#### Tuesday May 30

* Set up Flask app with Users and Events resources, two sets of RESTful routes 
* Set up initial database migration **_(done)_**
* Set up user log in & signup & log out
* Basic styling with logo, splash image, font pairing, and color scheme **_(done)_**
* Initial deploy to Heroku **_(done)_**
* Add to Rithm repo **_(done)_**

#### Wednesday May 31

* Attendees list on Events objects (1:M relationship)
* Create a way for attendees to sign up for each event and stop them once event is full
* Convert CSS to SCSS
* Make layout with Flexbox rather than just 12 col grid
* Add CSS animations & transitions for event display and buttons

#### Thursday June 1

* Beta test with some friends and fix any bugs in basic event creation, attendee addition
* Get pickier about security so that personal info (email, cell #) are not accessible to anyone outside of attendees leading up to each event
* Get pickier about validation of data so that forms are intuitive to fill out & data is what we want/expect -- try to have drop-downs that you can also type in (like facebook events) for date and time of events
* Try to create a photo cropper; display of images including zoom in/out to fit the UI -- things like cropping profile image into a square, having maximum upload size, cropping lettuce header image into a landscape rectangle (cover image style)

#### Friday June 2

* Try out Google Maps search for restaurant venues
* Try out way to send email reminder to all attendees and/or text message reminder to all attendees
* Most importantly, *don’t break the app before demos*
* Final deploy

********

## Development Timeline

* How to set up and run this app locally:
    * (writing this up later)

## Appendix

* [Project Guidelines](https://github.com/rithmschool/fullstack_project) - Rithm School Week 5

* Check out more details about plans for the app, questions, & progress [here](https://docs.google.com/document/d/1UcY4zTgfRUQolKyFGeEFAckOhiQEANiOMKMgdrafxm4/edit?usp=sharing)
