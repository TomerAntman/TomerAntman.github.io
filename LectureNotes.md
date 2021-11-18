**2/11/2021**
## JSON
We learned what **.JSON** files are used for: mainly it allows us to transfer data between platforms and programs. It works similarly to vocabulary in python.
  - JSON files can't have a comma after the last value
  - use _null_ rather than _none_
  - to add several values to each key create a list by putting square brackets
  
## GIT
The full description appears in the [README.md](https://github.com/Code-Maven/wis-advanced-python-2021-2022/blob/main/README.md) file on github.

- Turn a github directory into a website, based on a markdown file

## HTML
- small icons = "Favicon"
- how to change styles
- HTML vs CSS
- you can use docs directory instead of root
- use \<div> to have blocks
- use \<span> to change the styling **inline**

**9/11/2021**
## HTML/CSS frameworks
Use too build a website that looks much better
- Bulma
- Bootstrap

## Flask
A web framework written in python. See [slides](https://code-maven.com/slides/python/flask)
- need to install (pip install flask)
- a decorator in python (@) changes the behaviour of the function after it
- to run, write in the terminal of Pycharm:
  - set FLASK_APP=app</br>  set FLASK_DEBUG=1</br> flask run 
- We talked about testing the flask app
- by using "**request**" you can create an html page based on input (meaning you can also request data)
- [**client**](https://code-maven.com/slides/python/flask-echo-get-client): call the flask app code from other python code (program)
- GET method vs POST method: I think GET will change the URL to whatever you wrote. (relevant [slide](https://code-maven.com/slides/python/flask-get-and-post-in-two-functions))

**16/11/2021**
## Flask
work with \<form> to use html syntax in flask. within it, use action to move to another url

As for the function that you want to call, you need to import (import <_file name_>) it and call some function in it. (to run the function by itself, not in flask, you need if \_\_name__=="\_\_main__" condition)

slide to see for homework: flask-path-params

### Templating
**Jinja**: templating engine. Special placeholders in the template allow writing code similar to Python syntax
- it's called jinja2 when you call it

## CSS
There are 3 ways to approach an element:
- name of html
- class
- id

**remember to use code-maven skeletons!!!**

## Python Tk
- toolkit to draw application (GUI)
- There are good videos in the bootcamp series