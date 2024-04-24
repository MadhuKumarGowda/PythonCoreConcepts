import requests
# try:
#     response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=35.6762&lon=139.6503&appid=9ce90cebc5b4cded9f21c1fb7f197029")
#     print(response)
#     response_json = response.json()
#     temp =  response_json["main"]["temp"]
#     temp_min = response_json["main"]["temp_min"]
#     temp_max = response_json["main"]["temp_max"]

#     print(f"In Tokyo it is currently {temp}° C")
#     print(f"Today's Lowest Temp is {temp_min}° C")
#     print(f"Today's Highest Temp is {temp_max}° C")

# except:
#     print("No internet access")



class City:
    def __init__(self, name, lat,lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_Data()
    
    def get_Data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=9ce90cebc5b4cded9f21c1fb7f197029")            
            self.response_json = response.json()
            self.temp =   self.response_json["main"]["temp"]
            self.temp_min =  self.response_json["main"]["temp_min"]
            self.temp_max =  self.response_json["main"]["temp_max"]
           
        except:
            print("No internet access")
    
    def read_Data(self):
         units_sym = "C"
         if self.units == "imperial":
             units_sym = "F"
         print(f"In {self.name} it is currently {self.temp}° {units_sym}")
         print(f"Today's Lowest Temp is {self.temp_min}° {units_sym}")
         print(f"Today's Highest Temp is {self.temp_max}° {units_sym}")


my_city = City("Tokyo", "35.6762", "139.6503")
my_city.read_Data()
vacation_city =City("Portland", "45.523064","-122.676483",units="imperial")
vacation_city.read_Data()


