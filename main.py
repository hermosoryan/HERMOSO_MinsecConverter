
# Enter an integer in seconds:500
# 500 seconds is 8 minutes and 20 seconds

print("Time Converter")
time = input("Enter an integer for seconds: ")
minute = int(time) // 60
second = int(time) % 60
print(time, "second is", minute, "minutes and", second, "seconds")