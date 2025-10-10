
def hotel_cost(nights):
    return 140*nights


def plane_ride_cost(city):
    if"Dubai" == city:
        return 183
    elif"Istanbul" == city:
        return 220
    elif"Karachi" == city:
        return 222
    elif"Mecca" == city:
        return 475
    

    def rental_car_cost(days):
        if days>=7 :
            return 40*days - 50
        elif days>=3 :
            return