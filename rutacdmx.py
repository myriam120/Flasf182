def findItinerary(tickets):
    def get_start_point(tickets):
        destinations = set(tickets.values())
        for k in tickets.keys():
            if k not in destinations:
                return k

    def find_min_itinerary(src):
        itinerary = []
        while src:
            dest = tickets.get(src)
            if not dest:
                break
            itinerary.append(src)
            src = dest
        return itinerary

    start_point = get_start_point(tickets)
    min_itinerary = find_min_itinerary(start_point)

    if min_itinerary:
        print(" -> ".join(min_itinerary))

if __name__ == '__main__':
    tickets = {
        'Constitucion': 'Isabel la Catolica',
        'La paz': 'Penon viejo',
        'Pantitlan': 'La paz',
        'Puerto aereo': 'Pantitlan',
        'Perto aereo': 'T.autobuses',
        'T.autobuses': 'Camarones',
        'Camarones': 'Instituto del petroleo',
        'Instituto del petroleo': 'Chabacano',
        'Chabacano': 'Garibaldi',
        'Garibaldi': 'Salto del agua',
        'Salto del agua': 'La paz',
        'Taxquena': 'Chabacano'
    }
    
    findItinerary(tickets)
