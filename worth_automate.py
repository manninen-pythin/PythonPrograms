def convert_min(time):
    hours, mins = time
    hours *= 60
    mins += hours
    return mins

def worth_automate(times_done, time_to_perform, time_to_automate):
    t1 = convert_min(time_to_automate)
    t2 = convert_min(time_to_perform)
    total = t2 * times_done
    w = 0
    while t1 >= total:
        t1 -= t2
        w += 1
    return(str(w))

i1 = int(input("How many times is the task performed per week: " ))
i2 = int(input("How many hours does the task take: " ))
i3 = int(input("How many minutes does the task take: " ))
i4 = int(input("How many hours would it take to automate: " ))
i5 = int(input("How many minutes would it take to automate: " ))
print("It will take " + worth_automate(i1, (i2, i3), (i4, i5)) + " weeks to save time.")


