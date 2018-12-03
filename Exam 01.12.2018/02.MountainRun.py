import math
record_in_seconds = float(input())
distance_in_meters = float(input())
take_one_meter = float(input())

meters = distance_in_meters * take_one_meter
denivelation_slower = math.floor(distance_in_meters / 50)
denivelation_slower = denivelation_slower * 30
total_time = meters + denivelation_slower

var = total_time - record_in_seconds

if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {var:.2f} seconds slower.")
