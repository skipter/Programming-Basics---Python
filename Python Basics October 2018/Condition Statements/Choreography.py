import math
steps = float(input())
dancers = float(input())
days = float(input())

stepsPerDay = math.ceil(1 * 100 / days)
procent = stepsPerDay / dancers

if stepsPerDay <= 13:
    print(f"Yes, they will succeed in that goal! {procent:.2f}%.")
else:
    print(f"No, They will not succeed in that goal! Required {procent:.2f}% steps to be learned per day.")
