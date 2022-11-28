def forecast(*data):
    result = []

    def add_locations(type_of_location):
        locations = list(filter(lambda x: x[1] == type_of_location, data))
        [result.append(f"{sl[0]} - {sl[1]}") for sl in sorted(locations, key=lambda x: x[0])]

    add_locations("Sunny")
    add_locations("Cloudy")
    add_locations("Rainy")

    return '\n'.join(result)

