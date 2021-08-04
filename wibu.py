import requests  

import bs4  

  
# Taking thecity name as an input from the user 

city = "palembang"

  
# Generating the url   

url = "https://google.com/search?q=weather+in+" + city 

  
# Sending HTTP request  

request_result = requests.get( url ) 

  
# Pulling HTTP data from internet  

soup = bs4.BeautifulSoup( request_result.text  

                         , "html.parser" ) 

  
# Finding temperature in Celsius. 
# The temperature is stored inside the class "BNeawe".  

temp = soup.find( "div" , class_='BNeawe' ).text  

    

print( temp )  
