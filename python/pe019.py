# conversion of my f# code

num = 0
first = 2
regularYear = [3,0,3,2,3,2,3,3,2,3,2,3]
leapYear = [3,1,3,2,3,2,3,3,2,3,2,3]
def count_sundays_on_first(year):
    global first, num
    count = 0
    is_leap_year = lambda y: (regularYear, leapYear)[y % 4 == 0] 
    for i in is_leap_year(year):
        if first == 7:
            num += 1
        first += 1
        while first > 7:
            first -= 7
map(count_sundays_on_first, xrange(1901, 2000+1))
print num