pencil = int(input())
pen = int(input())
liquid = float(input())
discount = int(input())

pencip_price = pencil * 5.80
pen_price = pen * 7.20
liquid_price = liquid * 1.20

materials = pencipPrice + penPrice + preparatPrice

total = materials - ((materials * discount) / 100)
print(f"{total:.3f}")
