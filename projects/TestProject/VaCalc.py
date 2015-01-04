__author__ = 'dreiger'

def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        raise StandardError("Invalid City: " + city)

def rental_car_cost(days):
    cost = 40 * days

    if days >=7:
        cost-= 50
    elif days >=3:
        cost-= 20

    return cost

def trip_cost(city, days, spending_money):
    try:
        return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money
    except:
        print "Error"

print trip_cost("Los Angeles", 5, 600)