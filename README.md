This project is the first step towards building my first full web application.

Here we wre building a console or command interpreter using the Cmd class of the cmd module.

This console allows users to create, display, update and destroy objects.

It  also includes a file storage engine.
We use JSON serialization and deserializtion to store our objects.
Storage is persistent that is data still remains even after you quit a session.

HOW DO WE START IT:
--------------------
To start an interactive session
--------------------------------
	By running ./console.py

	A prompt "(hbnb) " is displayed awaiting user input.

HOW DO WE USE IT
-----------------
Creating objects:

	create <ClassName> => returns the id of the created object
	For example:
	create Review
	User.create()

Displaying a particular class object using class_name and ID:

	For example:
	User.show(<id>)
	show Amenity <id>

You can also display all objects available for all classes:

	For example:
	all

Or you can display all objects of a specific class:

	For example:
	all Place
	State.all()

To update a particular instance, use update.

	For example:
	update User <id> "Attribute_Name" "Attribute_ Value"
	OR
	Amenity.update(<id>, "Attribute_Name", "Attribute_value")

	An object can also be updated by passing a dictionary.
	For example:
	Class_name.update(<id>, {"First_Name": "Alicia"}

To destroy an object, call destroy:

	For example:
	destroy Review <id>
	User.destroy(<id>)


------------To get the console running in non interactive mode---------------

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)



The Models Package
-------------------
This package contains these classes:

	1. BaseModel class in base_models => Attributes id, updated_at, created_at

	2. User class in user => User information like first_name and last_name

	3. Review class in review => Holds user reviews : Their id, the place id and the review

	4. Place class in place => Provides information like precise location(latitude, longitude), price per night, number of bathrooms, maximum number of guests..
	5. State class in state => Name of the state
	
	6. City class in city => Name of the city, state_id..

The Engine subpackage
----------------------
A subpackage of Models that contains the FileStorage class in file_storage module.

This manages JSON serialization and deserialization in this flow: <object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>

In the init file of this subpackage, we have the variable storage, an instance of FileStorage. We use storage to call reload() so that at initialization, storage is reloaded automatically, aiding in recovery of our data.

TESTS
-------
The tests folder contains tests for all classes and the console.
I used the unittest module to test my code.

