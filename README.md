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
* Create event cards **_(done)_**
* Set up second resource Events with initial RESTful routes (GET & POST - index, new, & edit) **_(done)_**

#### Thursday June 1

* Complete second resource Events with remaining RESTful routes (PATCH & DELETE) **_(done)_**
* Event Card Styling **_(done)_**
    * Space out event cards using 12-col grid and gutters **_(done)_**
    * Add box shadow with hover effect **_(done)_**
    * Convert date like “06/02” to “June 2” **_(done)_**
* Mobile - change sandwich menu color to match color scheme **_(done)_**
* Attendees list on Events objects (1:M relationship) **_(done)_**

#### Friday June 2
 
* Create a way for attendees to sign up for each event and stop them once event is full
* Date & Time display 
    * add am/pm 
    * automatically display end time 
    * add bootstrap datepicker to new & edit forms
* Mobile UI Styling
    * increase font size and button size so they are clickable on small screen
* Add alert before deleting; “Are you sure you want to delete this event/user?” 

#### Extras

* Security; make sure personal info (email, cell #) is not accessible to anyone outside of attendees leading up to each event
* Add Google Maps search for restaurant venues & maps API to display location
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
