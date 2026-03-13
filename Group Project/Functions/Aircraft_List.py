import os
def clear_terminal() :
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()


#   LIst of 6 different aircraft

def calculate_deflection() :    # Gather variable choices
    # 1- Aircraft data (wingspan in meters, reference area in m^2)
    aircraft = {
        "Sailplane (High Performance)" : {"span" : 21.0, "area" : 13.2},
        "Cesna 172" : {"span" : 11.0, "area" : 16.2},
        "Gulfstream G500" : {"span" : 26.5, "area" : 88.0},
        "Boeing 737-800" : {"span" : 35.8, "area" : 124.6},
        "Boeing 787-10" : {"span" : 60.1, "area" : 361.0},
        "Lockheed C-5 Galaxy" : {"span" : 67.9, "area" : 576.0},
    }

    # 2- Material data (Young's Modulus in Pascals)
    materials = {
        "Carbon Fiber (CFRP)" : 150e9,
        "Aluminum (7075)" : 71.7e9,
        "Titanium Alloy" : 113e9,
        "Sitka Spruce (Wood)" : 11e9
    }

    print("-----Wing Deflection Calculator----")

    #  Select the airplane
    planes = list(aircraft.keys())
    for i, name in enumerate(planes, 1) :
        print(f"{i}. {name}")
    plane_choice = planes[int(input("\nSelect Aircraft (1-6): ")) - 1]

if __name__ == "__main__" :
    calculate_deflection()
