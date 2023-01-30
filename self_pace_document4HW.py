#Excersise #1


basket = {}
class Cart():
    """A simple grocery list."""


    def __init__(self, milk, eggs, butter):
        
        while True:
            y = input("Please choose: Add/Show/Delete or quit ")
            if y.lower() == 'add':
                product = input("What you want? ")
                items = input("How many? ")
                basket[product] = items
            elif y.lower() == 'delete':
                y = input("What to remove? ")
                del basket[y]
                print(f'okay {y} was removed')
            elif y.lower == 'show':
                print(f'here is your grocery list{basket}')
            elif y.lower() == 'quit':
                print("come back soon")
            break
            
        else:
            print("try again")

        self.milk = milk
        self.eggs = eggs
        self.butter = butter
        self.new_items = 0
    

    def grocery_list(self):
    #I get an error when I run this code, it says "can only concatenate str (not "int") to str", but I do not see why.
        first_items = str(self.milk) + "" + self.eggs + " " + self.butter
        return first_items.title()

    def show_items(self):

        print("This list has " + str(self.new_items) + " new items added. ")


    def update_list(self, items):
    
        self.new_items = items


my_current_list = Cart(10,5,6)
print(my_current_list.grocery_list()) 
my_current_list.new_items = 3
my_current_list.show_items()
my_current_list.update_list(0)
my_current_list.show_items()


#I think this is correct. I used the book as a refernce and guide. 
#Code does not run after the number of items is entered, cant figure out why, need help
