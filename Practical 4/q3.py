hourly_rate = 40
OT_regular = hourly_rate * 1.5
OT_excess = hourly_rate * 2
hourly_limit = 35
hourly_ragular = 25

#read the hour input
hours = float(input('Enter working hours: '))

if hours <= 35:
    regular_pay = hours * hourly_rate
else:
    regular_pay = hourly_limit * hourly_rate
    hours -= hourly_limit

if hours <= 25:
    overtime_pay = hours * OT_regular
else:
    overtime_pay = hourly_ragular * OT_regular
    hours -= hourly_ragular

overtime_pay += hours * OT_excess

print("\n {:15s}:RM {:.2f}".format("Total salary",regular_pay + overtime_pay))

print("\n {:15s}:RM {:.2f}".format("->Regular pay",regular_pay))

print("\n {:15s}:RM {:.2f}".format("->Overtime Pay" ,overtime_pay))
print("Total Salary :" ,round (overtime_pay+regular_pay,2))


round(1,2)