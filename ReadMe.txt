
Introduction:
This is a restaurant chatbot which helps user get details about restaurants based on location, cusine and budget.
Features :
	- Maintains Dialog.
	- Presents user with options , users can also type additionally.
	- Option to receive email with details of restaurant.

How To Train:
In base folder :
rasa train -vv -dump-stories --force

How To Run:
"rasa shell"
In another terminal "rasa run actions"