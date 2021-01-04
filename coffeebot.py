from time import sleep


def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print("I'm sorry, I didn't catch that.") 
        return get_size()
def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n ')
    if res == 'a':
        return 'Brewed Coffee'
    elif res == 'b':
        return 'Mocha'
    elif res == 'c':
        return order_latte()
    else:
        print("I'm sorry, I didn't catch that.") 
        return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy Milk \n")
  if res == 'a':
    return '2% milk'
  elif res == 'b':
    return 'Non-fat milk'
  elif res == 'c':
    return 'Soy'
  else:
    print("I'm sorry, I didn't catch that.") 
    return order_latte()

# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  sleep(2)
  size = get_size()
  sleep(1)
  # print(size)
  drink_type = get_drink_type()
  # print(drink_type)
  print("Alright, that\'s a {} {}!".format(size, drink_type))
  name = input("Can I get your name please?")
  print("Thanks, {}! Your drink will be ready shortly!".format(name))
  order_up = ("Order for,{}?".format(name))
  sleep(3)
  print(order_up)
  sleep(4)
  served = ("Oh there you are,{}! Here's your {} {}!".format(name, size, drink_type))
  print(served)
  sleep(3)
  print("Have a great day!")
  
  

# Call coffee_bot()!
coffeebot()  
  




