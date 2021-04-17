
COLOURS_AND_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "beige": "#f5f5dc",
                     "black": "#000000", "BlueViolet": "#8a2be2", "brown": "#a52a2a", "CadetBlue":
                         "#5f9ea0", "chocolate": "#d2691e", "coral": "#ff7f50", "DarkGreen": "#006400"}
print(COLOURS_AND_CODES)

color_input = input("Enter a color name: ")
while color_input != "":
    print("color code for {} is {}".format(color_input, COLOURS_AND_CODES.get(color_input)))
    color_input = input("Enter a color name: ")

