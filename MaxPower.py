import sys
import math


# Calculates the most suitable link station for a device at point[x,y]


def max_power_calculation():

    # takes input from user for device's location
    def input_point_value():
        try:
            x = float(input("Enter x coordinate: "))
            y = float(input("Enter y coordinate: "))
            return x, y
        except ValueError:  # handles exception for entering alphabet value
            print("Please enter a number value")
            sys.exit(1)

    point = input_point_value()  # stores device location values in a variable
    link_station = [
        [0, 0, 10],
        [20, 20, 5],
        [10, 0, 12]
    ]   # defines link station locations

    # calculates device's distance from all link stations
    # calculates power for each link station and returns the value
    def calculate_power(device):
        power_of_link_stations = []         # initializing a list
        for i in range(len(link_station)):
            for j in range(len(link_station[i])):
                distance = math.sqrt(
                    ((device[0] - link_station[i][j]) ** 2)
                    + ((device[1] - link_station[i][j + 1]) ** 2)
                )     # calculating distance between device and link stations
                if distance < link_station[i][j + 2]:
                    # power = (reach - device's distance from link station)^2
                    power = round((link_station[i][j + 2] - distance) ** 2, 3)  # calculating power of each link station

                else:
                    power = 0     # if distance >reach, power=0
                power_of_link_stations.append(power)
                break
        return power_of_link_stations  # returns power of link stations

    link_station_power = calculate_power(point)  # stores power values in a variable

    # Calculates most suitable(with most power) link station for a user-input point

    def calculate_max_power(power_of_link_station):
        if (
                power_of_link_station[0]
                == power_of_link_station[1]
                == power_of_link_station[2]
                == 0
        ):
            print("No link station within reach")

        elif (power_of_link_station[0] > power_of_link_station[1]) and (
                power_of_link_station[0] > power_of_link_station[2]
        ):

            print("Best Link station for point "
                  + str(point) +
                  " is "
                  + str(link_station[0]) +
                  " with power "
                  + str(power_of_link_station[0])
                  )

        elif (power_of_link_station[1] > power_of_link_station[2]) and (
                power_of_link_station[1] > power_of_link_station[0]
        ):

            print("Best Link station for point " +
                  str(point) +
                  " is "
                  + str(link_station[1]) +
                  " with power "
                  + str(power_of_link_station[1]))
        else:

            print("Best Link station for point "
                  + str(point) +
                  " is "
                  + str(link_station[2]) +
                  " with power "
                  + str([2]))

    # calls calculate_max_power method

    calculate_max_power(link_station_power)


# Calls the function block


max_power_calculation()
