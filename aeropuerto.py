
def print_itinenary(dictionary, src):
    dest = dictionary.get(src)
    if not dest:
        return
    print(src + '->' + dest)
    print_itinenary(dictionary, dest)
    
def findItinerary(tickets):
    destinations = {*tickets.values()}
    for k, v in tickets.items():
        if k not in destinations:
            print_itinenary(tickets,k)
            return
if __name__== '__main__':
    tickets = {
        'LAX':'DXB',
        'DFW':'JFk',
        'LHR':'DFW',
        'JFK':'LAX'
    }
    findItinerary(tickets)
    