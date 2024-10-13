#Name: Johnathan Sullivan
#Program Name: Planting Grapevines
#Program_Description: The following program calculates the number of vines that will fit in the row, /
#along with the trellis end-post assemblies that will need to be constructed at each end of the row.




#Input
R = int(input('Enter the length of the row in feet:'))
E = int(input('Enter the amount used by end assembly in feet:'))
S = int(input('Enter the amount of space used by vines in the row:'))

#The Formula is
V = (R - 2 * E) / S

#Output
number_of_grapevines = (R - 2 * E) / S
print(f'Number of Grapevines = {number_of_grapevines:.0f}')
