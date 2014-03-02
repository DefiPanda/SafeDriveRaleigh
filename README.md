SafeDriveRaleigh
================  
  
Author: Zhe Wang  
  
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
Flask  
Heroku
