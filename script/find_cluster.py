#this script find hotspot by applying kmeans; it also itserts the hotspot to mongodb database "crashes" with collection name "hotspot"
import numpy as np
from pymongo import MongoClient
import sklearn.cluster

def main():
  client = MongoClient()
  geolocation = client.crashes.geolocation
  hotspot = client.crashes.hotspot
  data = []
  for entry in geolocation.find():
  	lat = float(entry["lat"])
  	lng = float(entry["lng"])
  	data.append([lat, lng])
  data_array = np.array([x for x in data])
  model = sklearn.cluster.k_means(data_array, 530, max_iter=1000, n_init=50, tol=0.00001)
  valid_model = model[0][30:]
  #remove old hotspot
  hotspot.remove()
  for entry in valid_model:
    entry_list = entry.tolist()
    hotspot.insert({"lat": entry_list[0], "lng": entry_list[1]})

if __name__ == '__main__':
  main()