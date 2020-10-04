
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


Sample Run after rasa shell:
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  Hi
Hi, How can I help you!
Your input ->  I need table for 2
please let me know the location.
Your input ->  bangalore
Serviced
? what kind of cuisine would you like?  6: North Indian (North Indian)
? what is the price range you are looking for ?  3: More than 700 ? (highend)
-----
B-hive in 43/A, 1st Main, Near Wipro Park, Jakkasandra Road, Koramangala 1st Block, Bangalore has been rated 4.4 Average Cost for 2 is : 1200
Kesariya in 55, Goenka Chambers, 1st Floor, Jeevan Griha Colony, 19th Main, Phase 2, JP Nagar, Bangalore has been rated 4.3 Average Cost for 2 is : 1200
Rasovara in Level 2, The Collection, UB City, Vithal Mallya Road, Lavelle Road, Bangalore has been rated 4.3 Average Cost for 2 is : 1400
Samarkand in Gem Plaza, Infantry Road, Bangalore has been rated 4.3 Average Cost for 2 is : 1600
Tandoori Taal in 3169-B, 12th Main, HAL 2nd Stage, Double Road, Indiranagar, Bangalore has been rated 4.2 Average Cost for 2 is : 900
-----
would you like details of top 10 restaurants in email ?
Your input ->  yes
please let me know your email adderess
Your input ->  h e m a n t @gmail.com
mail sent
Bye-bye
