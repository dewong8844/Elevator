import random
import bisect

class Elevator:
    """ Elevator class creates an elevator object,
    with a name and number of floors served.
    The elevator object is created with an empty list of requested stops,
    and a set of stops with all floors where this elevator stops.
    """
    def __init__(self, name, high=20, low=1):
        self.name = name
        if low < 1:
            self.low_limit = 1
        else:
            self.low_limit = low
        self.floors = self.high_limit = high
        self.requested = []
        self.stops = set(range(low,high))
        self.stops.add(1)               # Make sure 1 is in set of stops
        self.current_floor = 1          # Initial floor
        self.direction = "UP"           # Initial direction
        self.next_requests = []         # Use for reverse direction
        
        for i in range(self.floors):
            self.stops.add(i+1)

            
    def new_request(self, floor):
        """ insert a new floor in requested list
                in ascending sorted order, if direction == "UP"
                in descending sorted order, if direction == "DOWN"
            if new requested floor is already "passed" in current direction,
            insert into the next_requests list in reverse order
                
        """
        if floor in self.stops:
            if self.direction == "UP":
                if floor > self.current_floor:
                    # insert in ascending order
                    bisect.insort_left(self.requested, floor)
                elif floor < self.current_floor:
                    # figure out how to insert in descending order
                    bisect.insort_left(self.next_requests, floor)
                # drop the request if same as current floor
            else:  # direction == "DOWN"
                if floor < self.current_floor:
                    # figure out how to insert in descending order
                    bisect.insort_left(self.requested, floor)
                elif floor > self.current_floor:
                    # insert in ascending order
                    bisect.insort_left(self.next_requests, floor)
                # drop the request if same as current floor
        
    togdir = {'UP':'DOWN','DOWN':'UP'}
    def reverse_direction(self):
        """ toggle the direction between UP and DOWN
        also sets the requested list with the next_requests list,
        and sets the next_requests list with []
        """
        self.direction = Elevator.togdir[self.direction]
        print "New direction: ", self.direction
        self.requested = self.next_requests
        if self.direction == 'DOWN':
            #HACK, until i figure out how to insert easily in descending order
            self.requested.reverse()
        self.next_requests = []
        #print "[DEBUG] - reversing: ", self.requested, "len: ", len(self.requested)

    def goto_next(self):
        """ Go to the next floor, the next entry in requested list
        After going to a floor, remove it (i.e. remove the current_floor),
        if more than one requests are to same floor, remove all of them
        """
        self.requested = [x for x in self.requested if x != self.current_floor]
        if len(self.requested) > 0:
            self.current_floor = self.requested[0]
            return self.current_floor
        else:
            # reverse direction and check if needs to work on next_requests
            self.reverse_direction()
            if len(self.requested) > 0:
                self.current_floor = self.requested[0]
                return self.current_floor
            else:
                return -1

    def gen_random_request(self):
        """ generate a request in the range low to high floors
        """
        i = random.randint(self.low_limit, self.high_limit)
        self.new_request(i)
        return i

    def run_test(self):
        """ Simulate elevator object running using random requests
        for elevator stops
        """
        count = 0  # additional requests after elevator is running
        while len(self.requested) > 0:
            next_stop = self.goto_next()
            if next_stop != -1:
                print "stop at: ", next_stop
                # print "[DEBUG]:", self.requested, "len: ", len(self.requested)
            if count < n:
                new_floor = self.gen_random_request()
                # print "[DEBUG]: new request - floor: ", new_floor 
                count += 1
            # Force elevator to stop at floor 1 at end of test
            if count == 1:
                self.new_request(1)
    
if __name__ == '__main__':
    m = Elevator('Main', 40)
    print "Elevator name: ", m.name
    print "floors served: ", m.low_limit, " to ", m.high_limit
    for test in range(3):
        print "Test run ", test + 1
        n = 10
        for i in range(n):
           m.gen_random_request()
        print "Initial direction: ", m.direction
        m.run_test()

    print


    e = Elevator('Express', 80, 40)
    print "Elevator name: ", e.name
    print "floors served: ", e.low_limit, " to ", e.high_limit
    for test in range(3):
        print "Test run ", test + 1
        n = 10
        for i in range(n):
           e.gen_random_request()
        print "Initial direction: ", e.direction
        e.run_test()    
