class NationalPark:

    def __init__(self, name):
        if isinstance (name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception

    @property
    def name(self):
        return self._name
        
    def trips(self):
        park_trips = []
        for trip in Trip.all:
            if (trip.national_park == self) and isinstance(trip, Trip):
                park_trips.append(trip)
        return park_trips
    
    def visitors(self):
        all_visitors = set()
        
        for trip in Trip.all:
            if (trip.national_park == self) and isinstance(trip.visitor, Visitor):
                all_visitors.add(trip.visitor)
        return list(all_visitors)
    
    def total_visits(self):
        park_visits = 0

        for trip in Trip.all:
            if trip.national_park == self:
                park_visits += 1
        return park_visits
    
    def best_visitor(self):
        visitor_visits = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor in visitor_visits:
                    visitor_visits[trip.visitor] += 1
                else:
                    visitor_visits[trip.visitor] = 1
        if visitor_visits:
            most_visits = max(visitor_visits, key=lambda visitor: visitor_visits[visitor])
            return most_visits
        return None

                
class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date (self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, new_start_date):
        if isinstance (new_start_date, str) and len(new_start_date) >= 7:
            self._start_date = new_start_date
        else:
            raise Exception
        
    @property
    def end_date (self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, new_end_date):
        if isinstance (new_end_date, str) and len(new_end_date) >= 7:
            self._end_date = new_end_date
        else:
            raise Exception
        
    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, new_visitor):
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
            return new_visitor
        else:
            raise Exception
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park (self, new_park):
        if isinstance(new_park, NationalPark):
            self._national_park = new_park
            return new_park
        else:
            raise Exception

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str) and (1 <= len(new_name) <= 15):
            self._name = new_name
        else:
            raise Exception
        
    def trips(self):
        all = []

        for trip in Trip.all:
            if trip.visitor == self and isinstance(trip, Trip):
                all.append(trip)
        return all
    
    def national_parks(self):
        all_parks = set()
        
        for trip in Trip.all:
            if (trip.visitor == self) and isinstance(trip.national_park, NationalPark):
                all_parks.add(trip.national_park)
        return list(all_parks)
    
    def total_visits_at_park(self, park):
        amt_visits = 0
        for trip in Trip.all:
            if (trip.visitor == self) and (trip.park == park):
                amt_visits += 1
        return amt_visits
