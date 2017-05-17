# Create a function
def minutes_to_hours(minutes):
    hours = minutes/int(60.0)
    return hours

print(int(minutes_to_hours(247)))

def time_conversion(minutes, seconds):
    hours = (minutes/60.0) + (seconds/3600)
    return hours

print(time_conversion(20, 40))
