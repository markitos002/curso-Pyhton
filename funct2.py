from datetime import datetime, timedelta

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main Tank: {main_tank}
    External Tank: {external_tank}
    Hydrogen Tank: {hydrogen_tank}
    """
    print(output)

generate_report(100, 200, 300)


#tiempo de llegada de la mision apollo que tomo 51 horas
def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Orbit", hours=0.13))
