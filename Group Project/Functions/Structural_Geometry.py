#  This is for determining the thickness profile for the wing depending on AC chosen

#  Structural Geometry (I value)

if "Sailplane" in plane_choice :
    thickness_factor = 0.03  #  very thin
else:
    thickness_factor = 0.12  #Standard airfoil thickness

span = aircraft[plane_choice]["span"]
area = aircraft[plane_choice]["area"]

#  Moment of Inertia (approximated for a wing box)
#  I = (width * height^3) / 12
avg_chord = area / span
I = (avg_chord * (height**3)) / 12


#  Let's calculate


lift = 0.5 * rho * (v**2) * area * cl
q = (lift / 2) / (span / 2)  #  Load per meter on one wing

#  Cantilever Deflection: (q * l^4) / (8 * E * I)
#  L is the length of one wing (half-span)
L_wing = span / 2
deflection = (q * (L_wing**4)) / (8 * E * I)

#  Time to print stuff

print(f"\n" + "*" * 40)
print(f"AIRCRAFT: {plane_choice}")
print(f"MATERIAL: {mat_choice}")
print(f"FORCE:  {lift:,.3f} N total lift")
print(f"Estimated Wingtip Deflection: {deflection * 100:.3f} cm")

#  Warnings
if deflection > (L_wing * 0.2) :
    print("Warning: Structural limits likely exceeded!")
elif "Concrete" in mat_choice :
    print("A plane with concrete wings isn't goint to get off the ground.")
    
