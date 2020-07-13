## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- yupp

## intent:deny
- no
- nope
- not needed
- leave it
- nahi
- nope not required
- I dont need

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- Hi

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "pricerange", "value": "midrange"} price range with [british](cuisine) food 
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Delhi](location)
- [Bangalore](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- please find me table for 5 costing around rupees [900](pricerange)
- show me restraurants within [500](pricerange) Rs
- I am looking for some [cheap](pricerange) restaurants in [Delhi](location)
- I am looking for some [midrange](pricerange) restaurants in [Delhi](location)
- Please find me a [highclass](pricerange) restaurant
- please help me to find restaurants in [pune](location) below [900](pricerange) per head
- Please find me a restaurantin [bangalore](location) costing rupees [1000](pricerange) per head
- looking for something [cheap](pricerange)
- looking for something [highend](pricerange)
- looking for something [midrange](pricerange)
- I want a place to eat within [250](pricerange) rupees
- Looking out for some good [south indian](cuisine) restaurants costing about [600](pricerange) per head
- Find me a [chinese](cuisine) restaurant in [lucknow](location)

## intent:send_email
- send mail to [abc@xyz.com](email)
- send to [ssasjhad@xdasdsyz.net](email)
- [abasdasc@xydasdsaz.com](email)
- [sample@domain.com](email)
- [sample_somethingelse@domain.com](email)
- ok my email address is [add.dshjhdjhdjw@xyewez.com](email)
- [hemant@gmail.com](email)
- [hemant1.abc@gmail.com](email)
- ok please send to [testmail@gmail.com](email)

## synonym:delhi
- New Delhi
- NCR
- Dilli

## synonym:mumbai
- Bombay
- Bambai
- Mubai
- Mumbaai


## synonym:bangalore
- Bengaluru
- Banglore
- blr
- blore

## synonym:kolkata
- Calcutta

## synonym:chennai
- Madras

## synonym:pune
- Poona

## synonym:ahmedabad
- Amdabad
- Ahamadabad

## synonym:hyderabad
- Hyd
- Haidarabad

## synonym:bokarosteelcity
- Bokaro

## synonym:hublidharwad
- Hubli
- Dharwad

## synonym:vasaivirarcity
- Vasai
- Virar
- Virarcity

## synonym:visakhapatnam
- Vizag


## synonym:cheap
- budget
- low price
- economical
- inexpensive


## synonym:midrange
- VFM
- value for money
- not very costly
- moderate
- mid

## synonym:highend
- highclass
- classy
- costly
- posh
- pricy
- fancy
- hiend


## synonym:chinese
- chines
- Chinese
- Chines
- china food

## synonym:american
- america

## synonym:italian
- italy

## synonym:mexican
- mexico



## synonym:mysore
- mysuru

## synonym:north indian
- north

## synonym:south indian
- south

## regex:greet
- hey[^\s]*

## regex:cheap
- hey[^\s]*