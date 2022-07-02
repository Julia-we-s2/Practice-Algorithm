a, b = map(int, input().split())
required_min = int(input())

to_minutes = a * 60 + b + required_min

hour, minute = divmod(to_minutes, 60)

if hour >= 24:
    hour -= 24

print(hour, minute)
