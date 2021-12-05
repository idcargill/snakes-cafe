from Order_Screen import Order_Screen
from food import food

screen = Order_Screen(38, food)

if __name__ == '__main__':
  screen.welcome_screen()
  screen.print_full_menu()
  screen.order_prompt()
  screen.place_order()
