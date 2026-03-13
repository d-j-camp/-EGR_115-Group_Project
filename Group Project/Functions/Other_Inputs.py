#   This is a list of inputs and calculations

    air_spd = float(input("\Enter Air Speed (kts): "))
    v = air_spd * 0.51444

    h = float(input("\nEnter Altitude (meters): "))
    L = 0.0065  #  Temperature lapse rate
    g = 9.81  #  Gravity, it's not just a good idea, it's the law.
    R = 287  #  Gas constant for air (J/kg K)


    rho0 = 1.225  # Air density at sea level
    T0 = 288.15
    rho = rho0 + (1 - (L * h) / T0) ** ((g / (R * L)) - 1)

    print("Air density at {h} meters is", round(rho, 3), "kg/m^3")

    cl = 0.6  #This is the lift constant (L) using a higher than typical Cl for general calculations
    E = materials[mat_choice]
