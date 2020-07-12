## User Greets and Gives Location Cusine and Price one By One
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"isServicedCity" : "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_pricerange
* restaurant_search{"pricerange": "900"}
    - slot{"pricerange": "900"}
    - action_search_restaurants
    - utter_ask_ifemailneeded
* affirm
    - utter_ask_emailid
* send_email{"email": "abc@xyz.com"}
    - slot{"email": "abc@xyz.com"}
    - action_send_email
    - utter_goodbye


## User Greets Gives Location but Cusine and Price one By One
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"isServicedCity" : "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_pricerange
* restaurant_search{"pricerange": "highend"}
    - slot{"pricerange": "highend"}
    - action_search_restaurants
    - utter_ask_ifemailneeded
* affirm
    - utter_ask_emailid
* send_email{"email": "abcas@xyzsa.net"}
    - slot{"email": "abcas@xyzsa.net"}
    - action_send_email
    - utter_goodbye


## User Gives Location but Cusine and Price one By One, no email
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"isServicedCity" : "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_pricerange
* restaurant_search{"pricerange": "highend"}
    - slot{"pricerange": "highend"}
    - action_search_restaurants
    - utter_ask_ifemailneeded
* deny
    - utter_goodbye


## User Gives Location  Cusine and later Price one By One, no email
* restaurant_search{"location": "chennai", "cuisine": "italian" }
    - slot{"location": "chennai"}
    - slot{"cuisine": "italian"}
    - action_validate_location
    - slot{"isServicedCity" : "True"}
    - utter_ask_pricerange
* restaurant_search{"pricerange": "highend"}
    - slot{"pricerange": "highend"}
    - action_search_restaurants
    - utter_ask_ifemailneeded
* deny
    - utter_goodbye


## User gives Price , then location and cusine , denies email
* greet
    - utter_greet
* restaurant_search{"pricerange": "midrange"}
    - slot{"pricerange": "midrange"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"isServicedCity" : "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_ifemailneeded
* deny
    - utter_goodbye

## User gives Price  location and cusine , denies email
* restaurant_search{"location": "chennai", "cuisine": "italian","pricerange": "midrange"}
    - slot{"location": "chennai"}
    - slot{"cuisine": "italian"}
    - slot{"pricerange": "midrange"}
    - action_validate_location
    - slot{"isServicedCity" : "True"}
    - action_search_restaurants
    - utter_ask_ifemailneeded
* deny
    - utter_goodbye


## Location is tier3
## User Greets and Gives Location Cusine and Price one By One
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "abc"}
    - slot{"location": "abc"}
    - action_validate_location
    - slot{"isServicedCity" : "False"}
    - utter_no_operation
    - utter_goodbye


## Gives Location
* restaurant_search{"location": "xyz"}
    - slot{"location": "xyz"}
    - action_validate_location
    - slot{"isServicedCity" : "False"}
    - utter_no_operation
    - utter_goodbye

## User Gives Location  Cusine but T3
* restaurant_search{"location": "hhda", "cuisine": "italian" }
    - slot{"location": "adda"}
    - slot{"cuisine": "italian"}
    - action_validate_location
    - slot{"isServicedCity" : "False"}
    - utter_no_operation
    - utter_goodbye