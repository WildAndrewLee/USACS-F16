Notes For: 10/2/2016

Last Updated: 10/7/2016

Next Meeting: 10/17/2016 5:30 PM (Location TBD)

# Ping Pong Tournament Creator

## Assignments

- For 10/17/2016
    - Start learning HTML, CSS, JavaScript, Python, Flask, and SQLAlchemy (no jQuery!)
    
- For 11/2/2016 (2:30 PM) College Ave Student Center
    - All of the above + put dummy data into the database and practice querying it.
    - Challenge make a form to put data into the database instead of doing it manually
    - Look into filters
    - Challenge: Joins

## Purpose

By the end of this mentorship mentees should be able to demonstrate basic to basic/intermediate knowledge of:
- Frontend development
- Backend development
- Solid design principles
- Collaborating as a Team

## Technologies Used

- HTML
- CSS
- JavaScript
- jQuery
- Python
- Flask
- SQLAlchemy
- Object Relation Mapping
- Git
- SQL

For the database server, you will connect to the following:
```
Host: reticent.io
Port: 3306
Database Name: usacs
Username: usacs
Password: usacs
```

You may need to manually specify the database if you are not using Heidi. You can issue the following SQL to specify the `usacs` database: `use usacs;`

To insert rows in Heidi, click the table desired, go to the `Data` tab, and press the insert key.

## Requirements

As a user, I want to be able to:
- Register as a player
- Register for a tournament as a player
- See tournaments in their current state
    - Player rankings, score, game wins, etc
- See player profiles for more detailed information
- Additional requirements pending completion of the above

## Recommended Tools

- HeidiSQL
- VIM / Visual Studio Code / Atom / Sublime Text

## Learning HTML and CSS

By Tim's suggestion, Codeacademy seems like a good place to start learning HTML and CSS. Remember to apply what you've learned so you don't forget!

### Other HTML Resources

- https://developer.mozilla.org/en-US/docs/Web/HTML/Element
- https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements
- https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements
- https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms
- https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes
- https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Obsolete_things_to_avoid

## Learning JavaScript

I highly recommend learning vanilla JavaScript before jumping into libraries such as jQuery. It will only make your life easier if you do it my way. Below are some links for you to get started:

### JavaScript

- https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript
- http://helephant.com/2008/08/19/functions-are-first-class-objects-in-javascript/
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#Function_declaration_hoisting
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Introduction_to_Object-Oriented_JavaScript
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures

If you would like a more in-depth look at particular things, you can check out: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide. I would advise against checking out the advanced section of this page unless you really have time. Likewise, things like the meta programming section, the indexed collections section, and details of the object model should be skipped. Iterators and generators are useful however you will probably not need them.

### JavaScript DOM Manipulation

- https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction
- https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors
- https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Events

The above links pertain to adding event handlers to specific DOM elements. You will be able to "make things happen" when things are clicked.

You will not be doing any DOM manipulation using vanilla JavaScript as learning the functions takes too much time.

### jQuery

jQuery resources will come after the next meeting.

## Learning Python

- https://learnpythonthehardway.org/book/ - Everything up to and excluding exercise 45.
- http://preshing.com/20110920/the-python-with-statement-by-example/

## Flask + Jinja

- http://flask.pocoo.org/docs/0.11/tutorial/
- https://realpython.com/blog/python/primer-on-jinja-templating/

### SQLAlchemy

- http://docs.sqlalchemy.org/en/latest/orm/tutorial.html

## Learning SQL

- https://www.khanacademy.org/computing/computer-programming/sql

## Examples Flask Applications

https://github.com/WildAndrewLee/Watch-My-Anime

A basic Flask application.

https://github.com/WildAndrewLee/SoMoe

A somewhat more advanced Flask application.