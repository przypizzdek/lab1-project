import requests
import json

def Wczytywanie_danych(typ, brend, model, year,battery_capacity,charge_power,engine_size,power):

    typ_dla_zaprosu = ""
    if typ == "Zwykle_samochody":
        typ_dla_zaprosu = "cars"
    elif typ == "Motory":
        typ_dla_zaprosu = "motorcycles"
    elif typ == "Ciezarowki": ####ELEKTROCARY
        typ_dla_zaprosu = "electricvehicle" ###ИЗМЕНИТЬ КЛАСС С ФУРЫ НА ЭЛЕТТРОМОБИЛИ

    API_KEY = "GCr9Zf6m0UH6MHF30d3EmWiEJJQEjH31j0blqCgi"
    API_URL_OGOLNY = "https://api.api-ninjas.com/v1"
    API_URL = f"{API_URL_OGOLNY}/{typ_dla_zaprosu}"

    params = {
        "make": {brend},
        "limit": 20
    }

    if model == "":
        print("model == """)
    else:
        params["model"] = {model}

    if year == "":
        print("year == """)
    else:
        params["year"] = {year}

    if typ == "Ciezarowki":  ####ELEKTROCARY
        if battery_capacity == "":
            print("battery_capacity == """)
        else:
            params["battery_kwh"] = {battery_capacity}
        if charge_power == "":
            print("charge_power == """)
        else:
            params["charge_power"] = {charge_power}
    elif typ == "Motory":
        if engine_size =="":
            print("engine_size ==""")
        else:
            params["engine"] = {engine_size}
        if power == "":
            print("power == """)
        else:
            params["power"] = {power}

    headers = {
        "X-Api-Key": API_KEY
    }

    try:

        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()

        cars_data = response.json()
        print(f"Получено {len(cars_data)} записей от API.")

        transformed_data = []
        for car in cars_data:
            transformed_car = {
                # "cena": car.get("price", 0),
                "brend": car.get("make", "").capitalize(),
                "typ": {typ},
                "model": car.get("model", ""),
                "year": car.get("year", 0)
            }

            if typ == "Ciezarowki": ####ELEKTROCARY
                transformed_car["battery_kwh"] = car.get("battery_capacity", "")
                transformed_car["charge_power"] = car.get("charge_power", "")
            elif typ == "Motory":
                transformed_car["engine"] = car.get("engine_size", "")
                transformed_car["power"] = car.get("power", "")

            transformed_data.append(transformed_car)

        output_filename = typ + "_data.json"
        with open(output_filename, "w", encoding="utf-8") as f:

            json.dump(transformed_data, f, indent=4, ensure_ascii=False)
    except requests.exceptions.RequestException as e:
        print(f"Blad przy zapytaniu API: {e}")
    except json.JSONDecodeError as e:
        print(f"Blad JSON: {e}")



