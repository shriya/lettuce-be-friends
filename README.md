# #LettuceBeFriends

A web application that lets people create healthy meal events to meet interesting people in small groups

[Live Site @ https://lettuce-be-friends.herokuapp.com/](https://lettuce-be-friends.herokuapp.com/)

###
# DO NOT FORGET SETUP INSTRUCTIONS
###
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

#### Friday June 2

* Attendees list on Events objects (1:M relationship) **_(working on it)_**

********

## Challenges & Wins

#### Biggest Challenges

* Setting up the relationships between event hosts, events, and event attendees
* Minimizing duplication of CSS & templates & routes; I did not minimize it but I "tried"

#### Biggest Wins

* Learning more CSS techniques, including creating 12-col grid cards with semi-Material Design style, working favicon, parallax splash image
* Learning about Python datetime formatting
* Semi-figuring out how to make relationship tables in this schema

********

## Things I Want to Add / Change

* Data
    * Display events you're hosting vs. attending differently
    * Have maximum RSVP count per event and stop it when it hits that
* Date & Time display
    * sort cards in index pages by date (soonest first)
    * add am/pm
    * automatically display end time
    * add bootstrap datepicker to new & edit forms
* CSS
    * increase font size and button size on mobile so they are clickable on small screen
    * Convert CSS to SCSS
    * Make layout with Flexbox rather than just 12 col grid
    * Add CSS animations & transitions for event display and buttons
* Polish
    * Add alert before deleting; “Are you sure you want to delete?”
    * Security; make sure personal info (email, cell #) is not accessible to anyone outside of attendees leading up to each event
* Features
    * Add Google Maps search for restaurant venues & maps API to display location
    * Create a photo cropper for profile pictures to be a square with a maximum upload size
    * Try out way to send email reminder to all attendees and/or text message reminder to all attendees
    * Facebook login!!!!!

********

## Appendix

* [Project Guidelines](https://github.com/rithmschool/fullstack_project) - Rithm School Week 5

* Check out more details about plans for the app, questions, & progress [here](https://docs.google.com/document/d/1UcY4zTgfRUQolKyFGeEFAckOhiQEANiOMKMgdrafxm4/edit?usp=sharing)
