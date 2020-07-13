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
		locholder = tracker.get_slot('location')
		loc = str(locholder).lower()

		print("loc is: " + str(loc))
		if((loc not in T1List) and (loc not in T2List)):
			print("checking location no srvice")
			return [SlotSet("isServicedCity", False)]	    
		else :
			dispatcher.utter_message("Serviced")
			print("checking location ok")
			return [SlotSet("isServicedCity", True)]


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		emailId = tracker.get_slot('email')
		loc = str(tracker.get_slot('location')).lower()
		cuisine = str(tracker.get_slot('cuisine')).lower()
		print("emailid is: " + str(emailId))
		send_email(emailId, "TestMail", "Your Top 10" + cuisine + "restaurants in " + loc );
		response ="mail sent"
		dispatcher.utter_message(response)


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"4cd00db93a47050dde023c45cc5f98ef"}
		zomato = zomatopy.initialize_app(config)
		loc = str(tracker.get_slot('location')).lower()
		cuisine = str(tracker.get_slot('cuisine')).lower()
		range = str(tracker.get_slot('pricerange')).lower()
		dispatcher.utter_message("range is: " + range)

		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

T1List = ["ahmedabad", "bangalore", "chennai", "delhi", "hyderabad", "kolkata" , "mumbai", "pune"]
T2List = ["agra","ajmer","aligarh","amravati","amritsar","asansol","aurangabad","bareilly","belgaum",
		  "bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bilaspur","bokarosteelcity","chandigarh",
		  "coimbatore","cuttack","dehradun","dhanbad","bhilai","durgapur","erode","faridabad","firozabad","ghaziabad"
		  "gorakhpur","gulbarga","guntur","gwalior","gurgaon","guwahati","hamirpur","hublidharwad","indore","jabalpur",
		  "jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kakinada","kannur","kanpur","kochi",
		  "kolhapur","kollam","kozhikode","kurnool","ludhiana","lucknow","madurai","malappuram","mathura","goa",
		  "mangalore","meerut","moradabad","mysore","nagpur","nanded","nashik","nellore","noida","patna","pondicherry",
		  "purulia","prayagraj","raipur","rajkot","rajahmundry","ranchi","rourkela","salem","sangli","shimla",
		  "siliguri","solapur","srinagar","surat","thiruvananthapuram","thrissur","tiruchirappalli","tiruppur","ujjain",
		  "bijapur","vadodara","varanasi","vasaivirarcity","vijayawada","visakhapatnam","vellore","warangal"]


def send_email(toAddress, mailSubject, mailText):
		import smtplib
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText

		sender_address = 'upgradchatbottest2020@gmail.com'
		sender_pass = 'upgrad2020'
		receiver_address = toAddress
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = mailSubject

		message.attach(MIMEText(mailText, 'plain'))
		session = smtplib.SMTP('smtp.gmail.com', 587) 
		session.starttls()
		session.login(sender_address, sender_pass) 
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		print('Mail Sent')