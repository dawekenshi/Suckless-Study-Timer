from time import sleep
import winsound

freq = 1000
dur = 2000

unities = input("In which unities do you want to measure your study? (hours, minutes, seconds) ")

if unities == "hours" or unities == "minutes" or unities == "seconds":
    
    time = input("How many time in "+unities+" do you want to study? ")

    time = int(time)

    decision = input("Do you want to start studying now? Y/N ")

    if unities == "hours" or unities == "Hours" and  decision == "Y":
        while time > 0:
            print(time)
            time -= 1
            sleep(3600)
        print("Finished hope u enjoyed your study!")
        winsound.Beep(freq, dur)
    elif unities == "minutes" or unities == "Minutes" and  decision == "Y":
        while time > 0:
            print(time)
            time -= 1
            sleep(60)
        print("Finished hope u enjoyed your study!")
        winsound.Beep(freq, dur)
    elif unities == "seconds" or unities == "Seconds" and  decision == "Y":
        while time > 0:
            print(time)
            time -= 1
            sleep(1)
        print("Finished hope u enjoyed your study!")
        winsound.Beep(freq, dur)
    elif decision == "N" or decision == "n":
        print("Okay, come back later :)")
else:
    print("Please input a correct unity of time")
    






