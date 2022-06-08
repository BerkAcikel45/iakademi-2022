import psycopg2
import random


days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
connection = psycopg2.connect(
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5432",
    database="nutritionist_app"
)
cursor = connection.cursor()

def user_creation():
    get_user_name = input("Welcome, please enter your name: ").capitalize()
    get_user_last_name = input("Welcome, please enter your last name: ").capitalize()
    get_user_weight = int(input("Welcome, please enter weight (kg): "))
    get_user_height = input("Welcome, please enter height (m/cm): ")

    # integer values will lead to miscalculations this solves such problems by conversion
    decimal_point = "."
    if decimal_point not in get_user_height:
        get_user_height = "".join([get_user_height[:1], decimal_point, get_user_height[1:]])

    user_bmi = get_user_weight / (eval(get_user_height) * eval(get_user_height))
    
    cursor.execute(f"INSERT INTO users values ('{get_user_name}', '{get_user_last_name}', '{get_user_weight}',  '{get_user_height}', '{round(user_bmi, 1)}' )")
    connection.commit()

    cursor.execute(f"SELECT user_ids FROM users WHERE user_name = '{get_user_name}'")
    the_id = cursor.fetchall()
    print(f"{get_user_name} successfully created. Your ID is: {the_id[0][0]}")


# diets for per body type
def daily_diet(base, max, day, id):
    cursor.execute(f"SELECT * FROM nutritions")
    connection.commit()
    nutritions = cursor.fetchall()

    intake_list = []
    intake = 0

    while not (base < intake < max):
        random_for_quantity = random.randint(1, 3)
        random_for_name = random.randint(0, 9) # to able to move around indexes
        
        if nutritions[random_for_name][0] not in intake_list:
            intake += nutritions[random_for_name][1] * random_for_quantity
            intake_list.append(nutritions[random_for_name][0])
            intake_list.append(" x " + str(random_for_quantity) + ", ")

        # adding then removing a placeholding element is necessary as SQL doesn't iterate through the last item of 'days'
        if intake > base and intake < max:
            intake_list.append("")       
            print("----------------------------------------------\nYou can take", intake, f"calories for {day.capitalize()}.")
            print("".join(intake_list))
            intake_list.remove("")

            empty_str = ""            
            cursor.execute(f"INSERT INTO menu values ('{empty_str.join(intake_list[0:len(intake_list)])}', '{day.capitalize()}', {id})")
            
        elif intake > max:
            intake = 0
            intake_list.clear()
                
                        
def view_user_details():
    try:
        get_user_id = int(input("Please enter your id to reach user details: "))

        cursor.execute(f"SELECT * FROM users WHERE user_ids = '{get_user_id}'")
        the_details = cursor.fetchall()

        print(f"Showing details for user '{get_user_id}'\n----------------------------------------------")
        print(f"Name: {the_details[0][0] + ' ' + the_details[0][1]}")
        print(f"Weight: {the_details[0][2]} Height: {the_details[0][3]}")
        print(f"Their Body Mass Index is: {the_details[0][4]}")

        # show their weekly menu based on their body type
        # normal type
        if 18.5 <= the_details[0][4] <= 24.9:
            print("You're in normal shape, keep up the good work!")
            
            get_preference = input("Do you want to create a weekly menu? If you say yes this will overwrite the existing data if such data exists. (y/n): ")
            if get_preference == "y":
                for day in days:
                    daily_diet(900, 2100, day, get_user_id)

            elif get_preference == "n":
                print("Not creating a menu, just enjoy the user's data!\n----------------------------------------------")
            else:
                print("Did you not see me saying (y/n)? Give me something valid.\n----------------------------------------------")           
        # a bit above normal
        elif 25 <= the_details[0][4] <= 29.9:
            print("You have a few extra kilos, but we'll fix that!")

            get_preference = input("Do you want to create a weekly menu? If you say yes this will overwrite the existing data if such data exists. (y/n): ")
            if get_preference == "y":
                for day in days:
                    daily_diet(700, 1900, day, get_user_id)
                    
            elif get_preference == "n":
                print("Not creating a menu, just enjoy the user's data!\n----------------------------------------------")
            else:
                print("Did you not see me saying (y/n)? Give me something valid.\n----------------------------------------------")
        # obese
        elif the_details[0][4] > 29.9:
            print("I hate to break it to you but you're obese...\n----------------------------------------------")

            get_preference = input("Do you want to create a weekly menu? If you say yes this will overwrite the existing data if such data exists. (y/n): ")
            if get_preference == "y":
                for day in days:
                    daily_diet(500, 1700, day, get_user_id)

            elif get_preference == "n":
                print("Not creating a menu, just enjoy the user's data!\n----------------------------------------------")
            else:
                print("Did you not see me saying (y/n)? Give me something valid.\n----------------------------------------------")
        else:
            print("You're an underweight")

    except ValueError:
        print("ID values must be integer values!")    
    except IndexError:
        print("Oops! User not found")


def display_menus():
    get_user_id = input("Please enter your id to reach user details: ")
    cursor.execute(f"SELECT daily_menu, days FROM menu WHERE menu_ids = {eval(get_user_id)}")
    result = cursor.fetchall()

    for i in result:
        print("----------------------------------------------")
        print(i[1])
        print(i[0])
        

while True:
    print("----------------------------------------------\n1 will create a user.\n2 will make a weekly diet list for them or reach their data\n3 will show you the created menus for a user\n'q' will stop the execution")
    get_operation = input("Choose an operation: ")
    if get_operation == "1":
        user_creation()
    elif get_operation == "2":
        view_user_details()
    elif get_operation == "3":
        display_menus()    
    elif get_operation == "q":
        break