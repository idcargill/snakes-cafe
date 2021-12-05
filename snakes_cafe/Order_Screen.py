from sys import exit
from message import msg

class Order_Screen:
  def __init__(self, width, menu):
    self.width = width
    self.menu = menu
    self.stars = ('*' * self.width)
    self.dashes = '-' * 10
    self.dishes = self.__get_all_dishes()
    self.ordered = {}

  def welcome_screen(self):
    w1 = '**   Welcome to the Snakes Cafe!    **'
    w2 = '**   Please see our menu below.     **'
    w3 = '** To quit at any time, type "quit" **'
    space = (' ' * (self.width - 4))

    print(self.stars)
    print(w1)
    print(w2)
    print(f'**{space}**')
    print(w3)
    print(self.stars, '\n')

  def order_prompt(self):
    prompt = '** What would you like to order? **'
    print(self.stars)
    print(prompt)
    print(self.stars, '\n')

  def print_full_menu(self):
    for title in self.menu:
      print(title)
      print(self.dashes)
      for dish in self.menu[title]:
        print(dish)
      print('\n')

  def __get_all_dishes(self):
    all_items = []
    for i in self.menu.values():
      all_items += i
    return all_items

  def print_dishes(self):
    print(self.dishes)
  
  def place_order(self):
    item = input('> ')
    ordered_item = item.lower()

    if ordered_item == 'quit':
      exit()
    elif ordered_item == '':
      self.show_order()
      self.place_order()
    elif ordered_item.title() in self.dishes:
      self.store(ordered_item)
    else: 
      print(msg)
      self.place_order()

  def store(self, item):
    food = item.title()

    if food in self.ordered:
      self.ordered[food] += 1
      print(f'** {self.ordered[food]} orders of {item.title()} have been added to your meal **')
      self.show_order()
      self.place_order()
    else:
      self.ordered[food] = 1
      print(f'** 1 order of {item.title()} has been added to your meal **')
      self.show_order()
      self.place_order()

  def show_order(self):
      print('Your current order:')
      for i in self.ordered.keys():
        print(f'{self.ordered[i]} orders of {i}')
