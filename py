import time

print("Hello, how many excercises are you doing today?")
exercises = input()
message = "Okay, you are doing " + str(exercises) + " exercises today"
print(message)
print("Please, insert information about seconds of exercise and seconds of rest")
numb_exercises = int(exercises)
exercises_times = []
while numb_exercises > 0:
    numb_exercises -= 1
    exercise = []
    exercise.append(int(input("Seconds of exercise ")))
    exercise.append(int(input("Seconds of rest ")))
    exercises_times.append(exercise)
    if numb_exercises == 0:
        break
print("Get ready, your timer will start in 60 seconds")
#countdown to get ready
countdown = + 60
while countdown > 0:
    print ('CountDown = ', countdown)
    countdown = countdown - 1
    time.sleep(1)
print("Get ready!")

# start countdown for exercise
for exercise, rest in exercises_times:
    print("Exercise time:")
    count_e = exercise
    count_r = rest
    while count_e > 0:
        print(f"Countdown = {count_e}")
        count_e -= 1
        time.sleep(1)
    print("Rest time:")
    while count_r > 0:
        print(f"Countdown = {count_r}")
        count_r -= 1
        time.sleep(1)
print("You are all set, great job")
