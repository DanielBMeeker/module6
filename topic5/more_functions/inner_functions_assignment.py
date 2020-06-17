def measurements(list_of_measurements):
    def area(a_list):
        return a_list[0]*a_list[1]

    def perimeter(a_list):
        return a_list[0]*2 + a_list[1]*2

    area_of_object = area(list_of_measurements)
    perimeter_of_object = perimeter(list_of_measurements)
    return "Perimeter = {} Area = {}".format(perimeter_of_object, area_of_object)
