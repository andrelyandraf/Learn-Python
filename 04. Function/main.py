second_of_units = "seconds"
minute_of_units = "minutes"
calculate_to_second = 24 * 60 * 60
calculate_to_minute = 24 * 60


def convert_to_hours(num_of_days,message):
    print (f"{num_of_days} days are {num_of_days * calculate_to_second} {second_of_units}")
    print (f"{num_of_days} days are {num_of_days * calculate_to_minute} {minute_of_units}")
    print (message)

convert_to_hours(35, "good")
convert_to_hours(40, "good")