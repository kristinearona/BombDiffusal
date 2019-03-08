#input number of wires
#input colors in orde
#input last digit of serial number
#output number of wire to cut
#www.bombmanual.com

wires = int (input("How many wires?"))
if wires == 3:
    wire1 = input ("1st wire color")
    wire2 = input ("2nd wire color")
    wire3 = input ("3rd wire color")
    bluecount = 0
    if wire1=="blue": bluecount=bluecount+1
    if wire1 != "red" and wire2 != "red" and wire3 != "red":
        print ("cut the second")
    if wire3 == "white":
        print ("cut last wire")
    if bluecount > 1:
        print ("cut the last blue wire")
    else :
        print ("cut the second wire")
elif wires == 4:
    wire1 = input ("1st wire color")
    wire2 = input ("2nd wire color")
    wire3 = input ("3rd wire color")
    wire4 = input ("4th wire color")
    serial = int (input("Serial"))
    redcount = 0
    bluecount = 0
    yellowcount = 0
    if wire1 == "red" : redcount=redcount+1
    elif wire1 == "blue" : bluecount=bluecount + 1
    elif wire1 == "yellow" : yellowcount=yellowcount+1
    if redcount > 1 and serial %2 == 1:
        print ("cut the last red wire")
    if wire4 == "yellow" and wire1 != "red" and wire2 != "red" and wire3 != "red":
        print ("cut the first wire")
    if bluecount == 1:
        print ("cut the first wire")
    if yellowcount > 1:
        print ("cut the last wire")
    else :
        print ("cut the second wire")
elif wires == 5:
    wire1 = input ("1st wire color")
    wire2 = input ("2nd wire color")
    wire3 = input ("3rd wire color")
    wire4 = input ("4th wire color")
    wire5 = input ("5th wire color")
    serial = int (input("Serial"))
    redcount = 0
    yellowcount = 0
    if wire1 == "red" : redcount=redcount+1
    elif wire1 == "yellow" : yellowcount=yellowcount+1
    if wire5 == "black" and serial %2 == 1:
        print ("cut the fourth wire")
    if redcount == 1 and yellowcount > 1:
        print ("cut the first wire")
    if wire1 != "black" and wire2 != "black" and wire3 != " black" and wire4 != "black" and wire5 != "black":
        print ("cut the last wire")
    else :
        print ("cut the first wire")
elif wires == 6:
    wire1 = input ("1st wire color")
    wire2 = input ("2nd wire color")
    wire3 = input ("3rd wire color")
    wire4 = input ("4th wire color")
    wire5 = input ("5th wire color")
    wire6 = input ("6th wire color")
    serial = int (input("Serial"))
    yellowcount = 0
    whitecount = 0
    if wire1 == "yellow": yellowcount=yellowcount + 1
    elif wire1 == "white": whitecount=whitecount + 1
    if wire1 != "yellow" and wire2 != "yellow" and wire3 != "yellow" and wire4 != "yellow" and wire5 != "yellow" and wire6 != "yellow" and serial %2 == 1:
        print ("cut the third wire")
    if yellowcount == 1 and whitecount > 1 :
        print ("cut the fourth wire")
    if wire1 != "red" and wire2 != "red" and wire3 != "red" and wire4 != "red" and wire5 != "red" and wire6 != "red":
        print ("cut the last wire")
    else :
        print ("cut the fourth wire")
