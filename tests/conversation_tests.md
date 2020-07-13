#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## Basic TestCase
* greet: Hi
  - utter_greet
* restaurant_search: I want to find a restaurant
  - utter_ask_location
* restaurant_search: delhi
  - slot{"location": "delhi"}
  - action_validate_location
  - slot{"isServicedCity":true}
  - utter_ask_cuisine
* restaurant_search : chinese
  - slot{"cuisine": "chinese"}
  - utter_ask_pricerange
* restaurant_search : 900
  - slot{"pricerange": "900"}
  - action_search_restaurants
  - utter_ask_ifemailneeded
* affirm : yes
  - utter_ask_emailid
* send_email : "abc@xyz.com"
  - slot{"email": "abc@xyz.com"}
  - action_send_email
  - utter_goodbye
