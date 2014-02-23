SafeDriveRaleigh
================  
  
Author: Jack Wang  
  
What is SafeDriveRaleigh  
---  
SafeDriveRaleigh is an HTML5 app helping safe driving in Raleigh area. It used the car crash open data from 09/01/2013 to 02/21/2014. The data is provided by Raleigh Police Department.  
  
Since all data provided are in PDF format, SafeDriveRaleigh mines car crashing geolocations from PDF files, and save them in MongoDB. It gathered 8875 number of data points. Then it uses K-means algorithm to find out the 500 crashing clusters, the result is generated to a JSON file.  
  
If you open SafeDriveRaleigh app on drive, it will remind you (through voice) when you are in an dangerous zone, and let you know when you are in the safe zoom again,
  
Tech Stack  
---  
JavaScript  
Python  
Leaflet  
MongoDB  
Heroku  

Top to-do list(No guarantee)  
---  
Use Cordova/PhoneGap to make this HTML5 app hybrid.  
  
Probably add a Choropleth map and a heat map for crashing location visualization (well we have 8000+ data points, right?).  
  
Add date range selection for map data visualization. We need to interact with MongoDB for that to happen (JSON data on client side is not good, because the computibility of a server is much more decent than a mobile phone; also downloading all data may also be unnecessary).  
  
Add script for auto updating crashing data daily.
