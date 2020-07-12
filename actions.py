from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json


class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'
		
	def run(self, dispatcher, tracker, domain):
		print("checking location")
		response = "location fine"
		loc = tracker.get_slot('location')
		print("loc is: " + str(loc))
		if(loc == "churu"):
			dispatcher.utter_message("No Service")
			print("checking location no srvice")
			return [SlotSet("isServicedCity", False)]	    
		else :
			dispatcher.utter_message("Serviced")
			print("checking location ok")
			return [SlotSet("isServicedCity", True)]
			
		dispatcher.utter_message("-----"+response)


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		print("sent email")
		response = "email id ok"
		dispatcher.utter_message("-----"+response)


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"4cd00db93a47050dde023c45cc5f98ef"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

