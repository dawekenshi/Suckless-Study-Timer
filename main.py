from time import sleep
import winsound as sound

freq = 1000
dur = 2000

unity_times = ["hour", "min", "sec"]

unities = input("In which unities do you want to measure your study? (hour, min, sec): ")

if unities.lower() in unity_times:

    time = int(input(f"How many {unities} do you want to study? "))
    decision = input("Do you want to start studying now? (y/n): ")

    sleep_time = {"hour": 3600, "min": 60, "sec": 1}

    if decision.lower() == "y":
        while time > 0:
            print(time)
            time -= 1
            sleep(sleep_time[unities.lower()])
        print("Finished, hope u enjoyed your study!")
        sound.Beep(freq, dur)
    elif decision.lower() == "n":
        print("Okay, come back later :)")
    else:
        print("Please input using (Y/N).")
else:
    print("Please input a correct unity of time (hour, min, sec).")







