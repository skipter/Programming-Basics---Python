cinemaType = input()
r = int(input())
c = int(input())

seats = r * c

premiere = 12 * seats
normal = 7.50 * seats
discount = 5 * seats

if cinemaType == "Premiere":
    print("{0:.02f} leva".format(premiere))
elif cinemaType == "Normal":
    print("{0:.02f} leva".format(normal))
elif cinemaType == "Discount":
    print("{0:.02f} leva".format(discount))