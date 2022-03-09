import time, sys, os # modules that are useful

# Credit to @ollieg for the functions below

def write(string): # spells letters one by one
  for ch in string: # for loop; loops over each letter
    sys.stdout.write(ch) # writes each letter
    sys.stdout.flush() # https://stackoverflow.com/questions/10019456/usage-of-sys-stdout-flush-method
    time.sleep(0.1) # sleep function stops the program for some seconds
  print()

def wrfast(string): # faster spelling
  for ch in string:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.075)
  print()

def clear(): # this function clears the current screen
  os.system('clear')

wrfast("Welcome to the Python® CoffeeMachine™ 3.1.1!") # writes the text in quotes
time.sleep(1) # waits 1 second
wrfast("Please wait while we prepare the machine.") 
time.sleep(1)
print() # adds an extra empty line
wrfast("Booting up coffee machine...")
time.sleep(1)
wrfast("Checking credentials...")
time.sleep(1)
wrfast("Warming up...")
time.sleep(1)
wrfast("Getting ready to make drinks...")
time.sleep(1)
wrfast("Doing more preparation stuff...")
time.sleep(1)
write("Loading...")
time.sleep(2)
print("Ready!")
time.sleep(2)
print()
clear()

wa = 1500 # starting water amount
mi = 750 # starting milk amoung
cb = 125 # starting coffee beans amount
dc = 15 # starting disposable cups amount
cp = 75 # starting cocoa powder amount
sg = 75 # starting sugar amount
mo = 15 # starting money amount
action = None # defines the action variable
while action != exit:
    print("What would you like to do? (buy - buy a drink, fill - restock resources, take - take out money, remaining - remaining resources, exit - shut down the machine):") # user interface; asks them what they would like to do
    action = input() # user input
    if action == 'buy': # buy a drink
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - milk, 5 - hot cocoa, back - to main menu:") # menu select of drinks; user types a number to indicate which drink they would like
        answer = input() # user response to their choice of drink
        if answer == '1': # user chooses espresso
            if wa >= 250 and cb >= 16 and dc >= 1: # checks if there is enough resources to make an espresso; executes the code below if true
                write("Would you like milk in your coffee (yes/no)?")
                response = input()
                if response.lower() == "yes":
                  if mi >= 100:
                    print('I have enough resources, making you a coffee with some milk!')
                    print("Executing command")
                    time.sleep(1)
                    write("...")
                    time.sleep(1)
                    write("Grinding coffee beans...")
                    time.sleep(1)
                    write("Heating water...")
                    time.sleep(1)
                    write("Mixing coffee...")
                    time.sleep(1)
                    write("Adding milk...")
                    time.sleep(1)
                    print("Done!")
                    time.sleep(1)
                    print("Here is your espresso!")
                    mi -= 100
                  elif mi < 100:
                    print("Sorry, not enough milk.")
                elif response.lower() != "yes":
                  print('I have enough resources, making you a coffee!')
                  print("Executing command")
                  time.sleep(1)
                  write("...")
                  time.sleep(1)
                  write("Grinding coffee beans...")
                  time.sleep(1)
                  write("Heating water...")
                  time.sleep(1)
                  write("Mixing coffee...")
                  time.sleep(1)
                  print("Done!")
                  time.sleep(1)
                  print("Here is your espresso!")
                wa = wa - 250 # removes resources used to make an espresso
                cb = cb - 16
                dc = dc - 1
                mo = mo + 4
            elif wa < 250: 
                print('Sorry, not enough water.')
            elif cb < 16: 
                print('Sorry, not enough coffee beans.')
            elif dc < 1: 
                print('Sorry, not enough cups.')
        elif answer == '2': # user chooses latte
            if wa >= 350 and mi >= 75 and cb >= 20 and dc >= 1: # checks if resources are enought to make a latte; executes the code below if true
                print('I have enough resources, making you a latte!')
                print("Executing command")
                time.sleep(1)
                write("...")
                time.sleep(1)
                write("Grinding coffee beans...")
                time.sleep(1)
                write("Heating water...")
                time.sleep(1)
                write("Steaming some milk...")
                time.sleep(1)
                write("Foaming some milk...")
                time.sleep(1)
                write("Mixing a shot of espresso...")
                time.sleep(1)
                write("Adding steamed milk")
                time.sleep(1)
                write("Adding foamed milk...")
                time.sleep(1)
                print("Done!")
                time.sleep(1)
                print("Here is your latte!")
                wa = wa - 350 # removes resources used to make a latte
                mi = mi - 75
                cb = cb - 20
                dc = dc - 1
                mo = mo + 7
            elif wa < 350:
                print('Sorry, not enough water.')
            elif mi < 75:
                print('Sorry, not enough milk.')
            elif cb < 20:
                print('Sorry, not enough coffee beans.')
            elif dc < 1:
                print('Sorry, not enough cups.')
        elif answer == '3': # user chooses cappuccino
            if wa >= 200 and mi >= 100 and cb >= 12 and dc >= 1: # checks if there are enough resources for a cappuccino; executes the code below if true
                print('I have enough resources, making you a cappuccino!')
                print("Executing command")
                time.sleep(1)
                write("...")
                time.sleep(1)
                write("Grinding coffee beans...")
                time.sleep(1)
                write("Heating water...")
                time.sleep(1)
                write("Steaming some milk...")
                time.sleep(1)
                write("Foaming some milk...")
                time.sleep(1)
                write("Mixing a shot of espresso...")
                time.sleep(1)
                write("Adding steamed milk")
                time.sleep(1)
                write("Adding foamed milk...")
                time.sleep(1)
                print("Done!")
                time.sleep(1)
                print("Here is your cappuccino!")
                wa = wa - 200 # removes resources used to make a cappuccino
                mi = mi - 100
                cb = cb - 12
                dc = dc - 1
                mo = mo + 6
            elif wa < 200:
              print('Sorry, not enough water.')
            elif mi < 100:
                print('Sorry, not enough milk.')
            elif cb < 12:
                print('Sorry, not enough coffee beans.')
            elif dc < 1:
                print('Sorry, not enough cups.')
        elif answer == '4':
          if mi >= 200: # user chooses milk
            print('I have enough resources, here\'s your milk!')
            print("Executing command")
            time.sleep(1)
            write("...")
            time.sleep(1)
            write("Pouring milk...")
            time.sleep(1)
            print("Done!")
            time.sleep(1)
            print("Here is your milk!")
            mi -= 200 # removes resources to make a cup of milk
            dc -= 1 
            mo += 3
          elif mi < 200:
            print('Sorry, I don\'t have enough milk!')
          elif dc < 1:
            print("Sorry, not enough disposable cups!")
        elif answer == '5': # user chooses hot cocoa
          if mi >= 250 and cp >= 25 and sg >= 25:
            write("Would you like foamed milk on top (yes/no)?")
            reply = input()
            if reply.lower() == "yes":
              if mi >= 375:
                print("I have enough resources, making you some hot cocoa with a foamed top!")
                print("Executing command")
                time.sleep(1)
                write("...")
                time.sleep(1)
                write("Pouring milk...")
                time.sleep(1)
                write("Adding cocoa powder...")
                time.sleep(1)
                write("Adding sugar...")
                time.sleep(1)
                write("Mixing...")
                time.sleep(1)
                write("Foaming milk...")
                time.sleep(1)
                write("Adding foamed milk...")
                time.sleep(1)
                print("Done!")
                time.sleep(1)
                print("Here is your hot cocoa!")
                mi -= 375
              elif mi < 375:
                print("Sorry, not enough milk for the foam top!")
            elif reply.lower() != "yes":
              print("I have enough resources, making you some hot cocoa!")
              print("Executing command")
              time.sleep(1)
              write("...")
              time.sleep(1)
              write("Pouring milk...")
              time.sleep(1)
              write("Adding cocoa powder...")
              time.sleep(1)
              write("Adding sugar...")
              time.sleep(1)
              write("Mixing...")
              time.sleep(1)
              print("Done!")
              time.sleep(1)
              print("Here is your hot cocoa!")
              mi -= 250
            cp -= 25
            sg -= 25
            dc -= 1
            mo += 5
          elif mi < 250:
            print("Sorry, I don\'t have enough milk.")
          elif cp < 25:
            print('Sorry, I don\'t have enough cocoa powder!')
          elif sg < 25:
            print("Sorry, I don't have enough sugar!")
          elif dc < 1:
            print("Sorry, not enough disposable cups!")
        elif answer == 'back': # user decides to go back to the main interface
            clear()
            continue
        time.sleep(5)
        clear()
    elif action == 'fill': # restock resources
        print("Write how many ml of water do you want to add:")
        w = input()
        try:
          w = int(w)
          if wa + w <= 3000:
            if w > 0:
              wa += w
              wrfast("Adding requested amount...")
              print()
            elif w <= 0:
              wrfast("Sorry, we can't add \"negative\" or \"zero\"!")
              print()
          elif wa + w >= 3000:
            wrfast("Sorry, you can't add that amount; we can't hold more than 3000 mL of water!")
            print()
        except ValueError:
          wrfast("Sorry, that's not an numeric value!")
          print()
        time.sleep(1)
        print("Write how many ml of milk do you want to add:")
        m = input()
        try:
          m = int(m)
          if mi + m <= 1500:
            if m > 0:
              mi += m
              wrfast("Adding requested amount...")
              print()
            elif m <= 0:
              wrfast("Sorry, we can't add \"negative\" or \"zero\"!")
              print()
          elif mi + m >= 1500:
            wrfast("Sorry, you can't add that amount; we can't hold more than 1500 mL of milk!")
            print()
        except ValueError:
          wrfast("Sorry, that's not an numeric value!")
          print()
        time.sleep(1)
        print("Write how many grams of coffee beans do you want to add:")
        b = input()
        try:
          b = int(b)
          if cb + b <= 200:
            if b > 0:
              cb += b
              wrfast("Adding requested amount...")
              print()
            elif b <= 0:
              wrfast("Sorry, we can't add \"negative\" or \"zero\"!")
              print()
          elif cb + b >= 200:
            wrfast("Sorry, you can't add that amount; we can't hold more than 200 grams of coffee beans!")
            print()
        except ValueError:
          wrfast("Sorry, that's not an numeric value!")
          print()
        time.sleep(1)
        print("Write how many disposable cups do you want to add:")
        c = input()
        try:
          c = int(c)
          if dc + c <= 25:
            if c > 0:
              dc += c
              wrfast("Adding requested amount...")
              print()
            elif c <= 0:
              wrfast("Sorry, we can't add \"negative\" or \"zero\"!")
          elif dc + c >= 25:
            wrfast("Sorry, you can't add that amount; we can't hold more than 25 disposable cups!")
        except ValueError:
          wrfast("Sorry, that's not an numeric value!")
          print()
        time.sleep(1)
        print("Write how many grams of cocoa powder do you want to add:")
        s = input()
        try:
          s = int(s)
          if cp + s <= 150:
            if s > 0:
              cp += s
            elif s <= 0:
              wrfast("Sorry, we can't add \"negative\" or \"zero\"!")
          elif cp + s >= 150:
            wrfast("Sorry, you can't add that amount; we can't hold more than 150 grams of cocoa powder!")
        except ValueError:
          wrfast("Sorry, that's not an numeric value!")
        time.sleep(1)
        print("Write how many grams of sugar do you want to add:")
        p = input()
        try:
          p = int(p)
          if sg + p <= 110:
            if p > 0:
              sg += p
            elif sg <= 0:
              wrfast("Sorry, we can't add \"negative\" or \"zero\"!")
              print()
          elif sg + p >= 110:
            wrfast("Sorry, you can't add that amount; we can't hold more than 110 grams of sugar!")
            print()
        except ValueError:
          wrfast("Sorry, that's not an numeric value!")
        time.sleep(1.5)
        print()
        print("The coffee machine has:")
        print(wa, "of water")
        print(mi, "of milk")
        print(cb, "of coffee beans")
        print(dc, "of disposable cups")
        print(cp, "of cocoa powder")
        print(sg, "of sugar")
        print('$' + str(mo), "of money")
        print()
        time.sleep(5)
        clear()
    elif action == 'take': # take out the money from the machine
        print()
        print('I gave you', '$' + str(mo))
        mo = mo - mo
        print()
        time.sleep(5)
        clear()
    elif action == 'remaining': # check the remaining resources in the machine
        print()
        print("The coffee machine has:")
        print(wa, "of water")
        print(mi, "of milk")
        print(cb, "of coffee beans")
        print(dc, "of disposable cups")
        print(cp, "of cocoa powder")
        print(sg, "of sugar")
        print('$' + str(mo), "of money")
        print()
        time.sleep(5)
        clear()
    elif action == 'exit': # shuts down the machine
      write("Shutting down...")
      time.sleep(1.75)
      break
    else:
      clear()
      continue
