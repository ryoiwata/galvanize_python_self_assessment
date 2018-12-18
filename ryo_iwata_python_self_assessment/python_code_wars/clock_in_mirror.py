"""
codewars.com/kata/56548dad6dae7b8756000037

Returns the actual time from a horizontally mirrored clock
"""

def what_is_the_time(time_in_mirror):
    hour,min = time_in_mirror.split(":")
    if int(min) == 0:
        min = int(min)
    else:
        min = 60 - int(min) # the minutes of the two clocks must add to 60
        hour = int(hour) + 1 # one hour must be be added to make the total 24 hours
    hour = 12 - int(hour) % 12 # modular must be added for times that include 12 o' clock
    return(str(format(hour, "02")) + ":" + str(format(min, "02")))
print(what_is_the_time("11:05"))
print(what_is_the_time("12:30"))
