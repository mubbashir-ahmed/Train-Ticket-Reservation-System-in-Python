# CLASSES
class MenuClass:
    def Panel_Selection():
        print("-----------------------------------")
        print("|                                 |")
        print("| Train Ticket Reservation System |")
        print("|                                 |")
        print("-----------------------------------")
        print("1. Admin Panel")
        print("2. Passenger Panel")
        print("3. Exit")
        opt = int(input("=> Enter your choice: "))
        if (opt == 1):
            AdminClass.Admin_Login()
        elif (opt == 2):
            PassengerClass.Passenger_Panel()
        elif (opt == 3):
            print("Thank you for using this app. Have a good day. Bye!")
            return
        else:
            print("Invalid option. Please try again")
            MenuClass.Panel_Selection()


class AdminClass:
    admin_login = {"username": "admin", "password": "admin123"}

    def Admin_Panel():
        print("\t\t\tADMIN PANEL")
        print("\t\t\t-----------")
        print("1. View Available Trains")
        print("2. Add New Train")
        print("3. Update Train Details")
        print("4. Remove Train")
        print("5. View Feedback")
        print("6. Logout")
        opt = int(input("=> Enter your choice: "))
        if (opt == 1):
            AdminClass.View_Trains()
        elif (opt == 2):
            AdminClass.Add_New_Train()
        elif (opt == 3):
            AdminClass.Update_Trains()
        elif (opt == 4):
            AdminClass.Delete_Trains()
        elif (opt == 5):
            AdminClass.View_Feedback()
        elif (opt == 6):
            MenuClass.Panel_Selection()
        else:
            print("Invalid option. Please try again")
            AdminClass.Admin_Panel()

    def Admin_Login():
        print("\t\t\tADMIN LOGIN")
        print("\t\t\t-----------")
        username = str(input("=> Enter your username: "))
        password = str(input("=> Enter your password: "))
        if (AdminClass.admin_login["username"] == username and AdminClass.admin_login["password"] == password):
            AdminClass.Admin_Panel()
        else:
            print("Invalid Credentials.")
            MenuClass.Panel_Selection()

    def View_Trains():
        print("\t\t\tVIEW TRAINS")
        print("\t\t\t-----------")
        for a, b, c, d, x, y, z in zip(TrainClass.t_id, TrainClass.t_name, TrainClass.t_seat, TrainClass.t_city, TrainClass.t_date, TrainClass.t_time, TrainClass.t_price):
            print("="*29)
            print("Train ID:", a)
            print("Train Name: " + b)
            print("Seats Available:", c)
            print("Departure City: Karachi")
            print("Arrival City: " + d)
            print("Departure Time: " + y)
            print("Departure Date: " + x)
            print("Ticket Price:", z)
            print("="*29)
        AdminClass.Admin_Panel()

    def Add_New_Train():
        print("\t\t\tADD NEW TRAIN")
        print("\t\t\t-------------")
        tid = int(input("=> Enter Train ID: "))
        if (not TrainClass.t_id.__contains__(tid)):
            tname = str(input("=> Enter Train Name: "))
            tseats = int(input("=> Enter Total Number of Seats Available: "))
            tcity = str(input("=> Enter Train Arrival City: "))
            ttime = str(input("=> Enter Train Departure Time: "))
            tdate = str(input("=> Enter Train Departure Date: "))
            tprice = int(input("=> Enter Train Ticket Price: "))
            TrainClass.t_id.append(tid)
            TrainClass.t_name.append(tname)
            TrainClass.t_seat.append(tseats)
            TrainClass.t_city.append(tcity)
            TrainClass.t_time.append(ttime)
            TrainClass.t_date.append(tdate)
            TrainClass.t_price.append(tprice)
            print("Record successfully added.")
        else:
            print("Train exists with train ID", tid)
            AdminClass.Add_New_Train()
        AdminClass.Admin_Panel()

    def Update_Trains():
        print("\t\t\tUPDATE TRAINS")
        print("\t\t\t-------------")
        tid = int(input("=> Enter train id to update train details: "))
        index = tid - 1
        if (TrainClass.t_id.__contains__(tid)):
            TrainClass.t_seat[index] = int(
                input("=> Enter updated number of seats available: "))
            TrainClass.t_time[index] = str(input("=> Enter updated time: "))
            TrainClass.t_date[index] = str(input("=> Enter updated date: "))
            TrainClass.t_price[index] = int(input("=> Enter updated price: "))
            print("Record successfully updated.")
        else:
            print("Train does not exists with Train ID", tid)
        AdminClass.Admin_Panel()

    def Delete_Trains():
        print("\t\t\tREMOVE TRAINS")
        print("\t\t\t-------------")
        tid = int(input("=> Enter train id to remove train: "))
        index = tid - 1
        if (TrainClass.t_id.__contains__(tid)):
            TrainClass.t_id.pop(index)
            TrainClass.t_name.pop(index)
            TrainClass.t_seat.pop(index)
            TrainClass.t_city.pop(index)
            TrainClass.t_time.pop(index)
            TrainClass.t_date.pop(index)
            TrainClass.t_price.pop(index)
            print("Record successfully deleted.")
        else:
            print("Train does not exists with Train ID", tid)
        AdminClass.Admin_Panel()

    def View_Feedback():
        print("\t\t\tPASSENGER FEEDBACKS")
        print("\t\t\t-------------------")
        feedback_file = open("feedback.txt", "r")
        for line in feedback_file.readlines():
            print(line.rstrip("\n"))
        feedback_file.close()
        AdminClass.Admin_Panel()


class PassengerClass:
    def Passenger_Panel():
        print("\t\t\tPASSENGER PANEL")
        print("\t\t\t---------------")
        print("1. View Available Trains")
        print("2. Book/Reserve A Train Ticket")
        print("3. Give Your Feedback")
        print("4. Exit")
        opt = int(input("=> Enter your choice: "))
        if (opt == 1):
            PassengerClass.View_Available_Trains()
        elif (opt == 2):
            PassengerClass.Reserve_Train_Ticket()
        elif (opt == 3):
            PassengerClass.Give_Feedback()
        elif (opt == 4):
            MenuClass.Panel_Selection()
        else:
            print("Invalid option. Please try again")
            PassengerClass.Passenger_Panel()

    def View_Available_Trains():
        print("\t\t\tAVAILABLE TRAINS")
        print("\t\t\t----------------")
        for a, b, c, d, x, y, z in zip(TrainClass.t_id, TrainClass.t_name, TrainClass.t_seat, TrainClass.t_city, TrainClass.t_date, TrainClass.t_time, TrainClass.t_price):
            print("="*29)
            print("Train ID:", a)
            print("Train Name: " + b)
            print("Seats Available:", c)
            print("Departure City: Karachi")
            print("Arrival City: " + d)
            print("Departure Time: " + y)
            print("Departure Date: " + x)
            print("Ticket Price:", z)
            print("="*29)

        print("Do you want to book a train ticket? (Y/N)")
        opt = str(input("=> Enter your choice: "))
        if (opt == "Y" or opt == "y"):
            PassengerClass.Reserve_Train_Ticket()
        elif (opt == "N" or opt == "n"):
            PassengerClass.Passenger_Panel()
        else:
            print("Invalid option. Please try again")
            PassengerClass.Passenger_Panel()

    def Reserve_Train_Ticket():
        print("\t\t\tRESERVE A TICKET")
        print("\t\t\t----------------")

        book_id = int(input("=> Enter train ID: "))
        index = book_id - 1
        if (TrainClass.t_id.__contains__(book_id)):
            print("Seats Available:", TrainClass.t_seat[index])
            book_seat = int(input("=> How many seats you want? "))
            if (book_seat <= TrainClass.t_seat[index]):
                print("="*29)
                print("Train ID:", TrainClass.t_id[index])
                print("Train Name: " + TrainClass.t_name[index])
                print("Booked Seat Numbers:", book_seat)
                print("Departure City: Karachi")
                print("Arrival City: " + TrainClass.t_city[index])
                print("Departure Time: " + TrainClass.t_time[index])
                print("Departure Date: " + TrainClass.t_date[index])
                print("Ticket Price:", TrainClass.t_price[index])
                print("="*29)

                print("\t\t\tCONFIRM TICKET BOOKING DETAILS (Y/N)")
                print("\t\t\t------------------------------------")
                opt = str(input("=> Enter your choice: "))
                if (opt == "Y" or opt == "y"):
                    PassengerClass.Generate_Ticket(book_id, book_seat)
                elif (opt == "N" or opt == "n"):
                    PassengerClass.Passenger_Panel()
                else:
                    print("Invalid option. Please try again")
                    PassengerClass.Passenger_Panel()
            else:
                print(book_seat, "Seats not available!")
                PassengerClass.Passenger_Panel()
        else:
            print("No train found with ID", book_id)
            PassengerClass.Passenger_Panel()

    def Give_Feedback():
        print("\t\t\tGIVE YOUR FEEDBACK")
        print("\t\t\t------------------")
        name = str(input("=> Enter your name: "))
        print("From scale of 1 to 10, how would you rate us?")
        feedback = int(input("=> Enter your rating: "))
        print("Any Comments?")
        comment = str(input("=> Enter your comments: "))
        feedback_file = open("feedback.txt", "a")
        feedback_file.write("Passenger Name: " + name + "\n")
        feedback_file.write("Rating: " + str(feedback) + "\n")
        feedback_file.write("Comments: " + comment + "\n")
        feedback_file.close()
        PassengerClass.Passenger_Panel()

    def Generate_Ticket(book_id, book_seat):
        print("\t\t\tTICKET")
        print("\t\t\t------")
        index = book_id - 1
        total_seats = []
        for x in range(book_seat):
            total_seats.append(TrainClass.t_seat[index] - x)
        TrainClass.t_seat[index] = TrainClass.t_seat[index] - book_seat
        name = str(input("=> Enter your name: "))
        phone = str(input("=> Enter your phone number: "))
        print("=*"*25)
        print("|| Booking Person Name: " + name)
        print("|| Phone Number: " + phone)
        print("|| Train ID:", TrainClass.t_id[index])
        print("|| Train Name: " + TrainClass.t_name[index])
        print("|| Booked Seat Numbers:", total_seats)
        print("|| Departure City: Karachi")
        print("|| Arrival City: " + TrainClass.t_city[index])
        print("|| Departure Time: " + TrainClass.t_time[index])
        print("|| Departure Date: " + TrainClass.t_date[index])
        print("|| Ticket Price:", TrainClass.t_price[index])
        print("=*"*25)
        PassengerClass.Passenger_Panel()

class TrainClass:
    t_id = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]
    t_name = ["Allama Iqbal Express", "Karakoram Express", "Awam Express",
              "Pak Bussiness Express", "Akbar Express", "Karakoram Express",
              "Awam Express", "Pak Bussiness Express", "Akbar Express"]
    t_seat = [13, 14, 24, 32, 14, 23, 19, 8, 11]
    t_price = [3000, 3200, 2500,
               6000, 2200, 2500,
               2000, 6000, 3400]
    t_city = ["Lahore", "Peshawar", "Islamabad",
              "Sargodha", "Rawalpindi", "Quetta",
              "Sialkot", "Faisalabad", "Sukkur"]
    t_time = ["12:00 pm", "3:00 pm", "6:00 pm",
              "9:00 pm", "12:00 am", "3:00 am",
              "6:00 am", "9:00 am", "12:00 am"]
    t_date = ["24/6/2022", "25/6/2022", "23/6/2022",
              "28/6/2022", "27/6/2022", "29/6/2022",
              "8/7/2022", "9/7/2022", "7/7/2022"]

    # comments = ["Comment 1", "Comment 2", "Comment 3"]
    # feedback = []


# MAIN CODE
m = MenuClass
m.Panel_Selection()
