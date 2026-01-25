input_rain = input("Is it raining? (yes/no): ")
input_tierd = input("Are you tierd? (yes/no): ")

raining = input_rain == "yes"
tierd = input_tierd == "yes"
if raining or tierd:
    print("Relax Indoors!")
elif not raining and not tierd:
    print ("Go for a hike!")