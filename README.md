# Build an Item Catalog Web App

A web application based on the Flask framework that provides a list of Type of Food, Authenticated users have the ability to create, edit, and delete .

we will develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. You will then learn when to properly use the various HTTP methods available to you and how these methods relate to CRUD (create, read, update and delete) operations.


## The files we have  

main Python module `app.py` which runs the Flask application

A SQL database is created using the `database_setup.py` module 

A test data using `database_init.py`

The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application.

CSS/JS are stored in the static directory.


## How to Set up a Google auth application
To get the Google login working there are a few additional steps:

1-go to https://console.developers.google.com/project and login with Google.
2-Create a new project
3- Name the project
4- Select "API's and Auth-> Credentials-> Create a new OAuth client ID" from the project menu
5-Select Web Application
6- On the consent screen, type in a product name and save.Enter name 'Item-Catalog'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory that you cloned from here
14. Run application using `python /item-catalog/app.py`

### Dependencies to run the application 
make sure to have all the items before you run the application 
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm-master)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)


## How to run the application
- make sure you are at fullstack-nanodegree-vm-master/vagrant
- Launch the Vagrant VM (vagrant up)
- Log into Vagrant VM (vagrant ssh)
- Navigate to the shared folder cd /vagrant 
- Setup application database python /item-catalog/database_setup.py
- *Insert fake data python /item-catalog/database_init.py
- Run application using python /item-catalog/app.py
- Access the application locally using http://localhost:5000




