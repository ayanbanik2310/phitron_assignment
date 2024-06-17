class Star_Cinema:
    def __init__(self):
        self.hall_list = []
    
    def enter_hall(self, hall):
        self.hall_list.append(hall)
    
    def hall_by_no(self, hallno):
        for hall in self.hall_list:
            if hall.hallno == hallno:
                return hall
        return None


class Hall:
    def __init__(self, hallno, row, col):
        self.seats = {}
        self.showList = []
        self.row = row
        self.col = col
        self.hallno = hallno
        self.seat = [[0 for i in range(col)] for j in range(row)]

    
    def entry_show (self, id, moviename):
        show = (id, moviename)
        self.showList.append(show)
        self.seats [id] = [[0 for i in range(self.col)] for j in range(self.row)]
    
    
    def bookseats(self, id, seatno):
        if id in self.seats:
            seats = self.seats[id]
            # if 0<=row<self.row and 0<=col<self.col:
            for row, col in seatno:
                if seats[row][col] == 0:
                    seats[row][col] = 1
                else:
                    print(f'{row}-{col} this seats already booked')
            # else:
            #     print(f'invalid seat no {row}-{col}')
        else:
            print(f'invalid show no {id}')
    
    def view_show_list(self):
        for show in self.showList:
            print('\t', end='')
            print(show)
    
    def view_available_seats(self, id):
        for show in self.showList:
            if show[0] == id:
                seats = self.seats[id]
                for row in seats:
                    print(" ".join(map(str, row)))
                    
                return
            else:
                print(f'invalid show id {id}')

    def get_show_id(self):  
        return [show[0] for show in self.showList] 


    

star_cinema = Star_Cinema()
hall1 = Hall(100, 10, 10)

hall1.entry_show(1001, 'Kantara')
hall1.entry_show(1002, 'Forensic')
hall1.entry_show(1003, 'U Turn')

star_cinema.enter_hall(hall1)

run = True
while run:
    print('options : ')
    print('1. All shows')
    print('2. All seats')
    print('3. Book tickets')
    print('4. Log-out')

    choice = int(input('select an options : '))

    if choice == 1:
        for hall in star_cinema.hall_list:
            print(f'\thall no - {hall.hallno} : ')
            hall.view_show_list()
        print()
    
    elif choice == 2:
        show_id = int(input('enter show id : '))
        hall = None
        for i in star_cinema.hall_list:
            if show_id in i.get_show_id():
                hall = i
                break
        if hall == None:
            print(f'\t{show_id} show is not found')
        else:
            hall.view_available_seats(show_id)
    
    elif choice == 3:
        show_id = int(input('enter show id : '))
        seat_count = int(input('how many seats you wanna booked : '))
        booked_seat = []

        for _ in range(seat_count):
            seat_no = input(f'\tenter Seat {_ + 1} (e.g., 0-0 to 9-9) : ')
            seat = tuple(map(int, seat_no.split('-')))
            booked_seat.append(seat)
        hall = None

        for i in star_cinema.hall_list:
            if show_id in i.get_show_id():
                hall = i
                break

        if hall:
            hall.bookseats(show_id, booked_seat)
            print("\tbooking successfully")

        else:
            print("\tshow Not Found!")

    elif choice == 4:
        print(f'\tthank you for visiting us')
        run = False
    else:
        print(f'\tinvalid input! try again')