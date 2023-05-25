# HBNB

This is the console /command interpreter for the ALX/Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects using either a MySQL database, or a JSON file.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start the console using JSON file storage, navigate to the project folder and enter `./console.py` in the shell.

To start the console using MySQL database as storage method, navigate to the project folder and enter:
`HBNB_MYSQL_USER=<username> HBNB_MYSQL_PWD=<password HBNB_MYSQL_HOST=<server hostname> HBNB_MYSQL_DB=<database name> HBNB_TYPE_STORAGE=db ./console.py`
