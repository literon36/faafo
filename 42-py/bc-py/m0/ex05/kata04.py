kata :tuple[int, int, float, int, float] = (0, 4, 132.42222, 10000, 12345.67)

modnum :str = str(kata[0]).zfill(2)
exnum :str = str(kata[1]).zfill(2)
roundnum :str = str(round(kata[2], 2))
#make scientific notation
sci1 :str = "{:.2e}".format(kata[3])
sci2 :str = "{:.2e}".format(kata[4])

print(f"module_{modnum}, ex_{exnum} : {roundnum}, {sci1}, {sci2}")

