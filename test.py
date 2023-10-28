import main
import random

# Spin off of Parking Garage functionality
class Parking_Garage2(main.Parking_Garage):
    
    # No one in the garage, spaces are full at intialize
    def __init__(self, _max_space= 50, payrate = .05 ):
        self.payrate = payrate
        self.tickets_given = 0
        self.tickets_available = _max_space
        self.max_space = _max_space
        self.spaces_left = self.max_space
        self.current_tickets = {}
        self.tickets = []


    def take_ticket(self):
        print("Take ticket")
        if self.max_space > 0:
            self.spaces_left -= 1
            self.tickets_available -= 1
            self.tickets_given += 1

            # Creates a unique random ticket ID
            id_number = str(self.tickets_given)+"_"+str(random.randint(1,1000))+chr(random.randint(97,122)).upper()

            print(f"Your ticket ID number is {id_number}")

            ticket = main.Ticket(id_number)
            self.current_tickets[str(id_number)] = ticket
            self.tickets.append(ticket)
        else:
            print("The garage is full.")

        def pay_for_parking(self):
            print("Pay for parking")
            _time = float(time.time())/60

            ticket_id = input("enter the ticket number:   ").strip()

            if ticket_id in self.current_tickets:
                self.current_tickets[ticket_id].pay_for_ticket(_time)
            else:
                print("Invalid TIcket ID")

    def leave_garage(self):
        print("Enter ticket number to leave:")
        ticket_id = input("enter the ticket number:    ").strip()
        if ticket_id in self.current_tickets:
            ticket = self.current_tickets[ticket_id]
            if ticket.check_if_paid():
                print("Thank you have a nice day")
                del self.current_tickets[ticket_id]
                self.tickets_available += 1
                self.spaces_left += 1
            else:
                self.pay_for_parking()
                if ticket.check_if_paid():
                    print("Thank you have a nice day")
                    del self.current_tickets[ticket_id]
                    self.tickets_available += 1
                    self.spaces_left += 1
        else:
            print("invalid_ticket_number")


garage2 = Parking_Garage2()

garage2.take_ticket()
garage2.leave_garage()