def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main Tank: {main_tank}
    External Tank: {external_tank}
    Hydrogen Tank: {hydrogen_tank}
    """
    print(output)

generate_report(100, 200, 300)
