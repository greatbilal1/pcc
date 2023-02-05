def make_car(manufacturer, model, average, oil_capacity, color="", **car_details):
    car_details["manufacturer"] = manufacturer
    car_details["model"] = model
    car_details["average"] = average
    car_details["oil_capacity"] = oil_capacity

    if color:
        car_details["color"] = color
    return car_details


car = make_car(
    manufacturer="toyota",
    model="forturner",
    average=50,
    oil_capacity=100,
    assembler="suzuki",
    location="japan",
)

print(car)
