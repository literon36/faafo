kata :tuple[int, ...] = (2019, 9, 25, 3, 30)

# make the numbers conform to two digits
year :str = str(kata[0]).zfill(4)
month :str = str(kata[1]).zfill(2)
day :str = str(kata[2]).zfill(2)
hour :str = str(kata[3]).zfill(2)
minute :str = str(kata[4]).zfill(2)

# print the date in the desired format
print(f"{month}/{day}/{year} {hour}:{minute}")