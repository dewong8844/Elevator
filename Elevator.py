import random
import bisect

class Elevator:
    """ Elevator class creates an elevator object,
    with a name and number of floors served.
    The elevator object is created with an empty requested list
    and a set of stops with all floors where this elevator stops.
    """
    def __init__(self, name, high=20, low=2):
        self.name = name
        if low < 2:
            self.low_limit = 2
        else:
            self.low_limit = low
        self.floors = self.high_limit = high
        self.requested = [1]            # Floor 1 is always in requested list
        self.stops = set(range(low,high))
        self.current_floor = 1          # Initial floor
        # self.direction = "UP"           # Initial direction
        
        for i in range(self.floors):
            self.stops.add(i+1)

    def new_request(self, floor):
        """ insert a new floor in requested list in ascending sorted order
        """
        if floor in self.stops:
            bisect.insort_left(self.requested, floor)
        
    def gen_random_request(self):
        """ generate a request in the range 1 to floors
        """
        i = random.randint(self.low_limit, self.high_limit)
        self.new_request(i)

    def goto_next(self):
        """ Go to the next floor, the next entry in requested list
        Floor 1 always stays in the requested list, so don't delete it
        After going to a floor, remove it (i.e. remove the current_floor),
        if more than one requests are to same floor, remove all of them
        """
        if self.current_floor != 1:
            self.requested = [x for x in self.requested if x != self.current_floor]
        if len(self.requested) > 1:
            self.current_floor = self.requested[1]
            return self.current_floor
        else:
            return -1
    
if __name__ == '__main__':
    """ TODO: how to stop if multiple entries at end of list are same?
    Need better way to get next entry in list and better way to stop
    """
    m = Elevator('Main', 40)
    n = 10
    for i in range(n):
       m.gen_random_request()
    print "floors: ", m.floors
    print "requested size: ", len(m.requested)
    while len(m.requested) > 2:
        next_stop = m.goto_next()
        if next_stop != -1:
            print "stop at: ", next_stop
            print "[DEBUG]:", m.requested, "len: ", len(m.requested)

    e = Elevator('Express', 80, 40)
    n = 10
    for i in range(n):
       e.gen_random_request()
    print "floors: ", e.floors
    print "requested size: ", len(e.requested)
    while len(e.requested) > 2:
        next_stop = e.goto_next()
        if next_stop != -1:
            print "stop at: ", next_stop
            print "[DEBUG]:", e.requested, "len: ", len(e.requested)

    
