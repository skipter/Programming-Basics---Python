examHour = int(input())
examMinutes = int(input())
hourArrive = int(input())
minuteArrive = int(input())

minutesExam = examMinutes + examHour * 60
minutesStudent = minuteArrive + hourArrive * 60

diff = minutesExam - minutesStudent

mins = abs(diff) % 60
if abs(diff) >= 60 and mins < 10:
    mins = f"0{mins}"

hours = abs(diff) // 60

if 0 <= diff and diff <= 30:
    print("On time")
    if diff != 0:
        print(f"{mins} minutes before the start")
elif 30 < diff and diff < 60:
    print("Early")
    print(f"{mins} minutes before the start")
elif 60 <= diff:
    print("Early")
    print(f"{hours}:{mins} hours before the start")
elif 0 > diff > -60:
    print("Late")
    print(f"{mins} minutes after the start")
elif -60 >= diff:
    print("Late")
    print(f"{hours}:{mins} hours after the start")