import os
def clear_terminal() :
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()


#   LIst of 6 different aircraft

def calculate_deflection() :    # Gather variable choices  
    materials = {
        "Carbon Fiber (CFRP)" : 150e9,
        "Aluminum (7075)" : 71.7e9,
        "Titanium Alloy" : 113e9,
        "Sitka Spruce (Wood)" : 11e9,
        "Concrete" : 28e9
    }

    mats = list(materials.keys())
    for j, name in enumerate(mats, 1) :
        print(f"{j}. {name}")
    mat_choice = mats[int(input("\nSelect Wing Material (1-5): ")) - 1]





if __name__ == "__main__" :
    calculate_deflection()
