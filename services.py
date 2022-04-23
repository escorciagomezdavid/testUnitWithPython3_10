import json


def __read_file():
    f = open('data.json')
    data = json.load(f)
    f.close()
    return data


def read():
    return __read_file()


def search(id):
    persons = __read_file()

    for person in persons:
        if person['id'] == id:
            return person

    return {}


def create(person):
    personas = __read_file()
    personas.append(person)
    f = open("data.json", "w")
    f.write(json.dumps(personas, indent=4))  # --- para pasarlo de json a str
    f.close()
    return True


def delete(id):
    person = search(id)
    persons = read()
    persons.remove(person)
    f = open("data.json", "w")
    f.write(json.dumps(persons, indent=4))
    f.close()


def update(id, data):
    person = search(id)
    persons = read()
    persons.remove(person)

    if data["name"]:
        person["name"] = data["name"]

    if data["email"]:
        person["email"] = data["email"]

    if data["phone"]:
        person["phone"] = data["phone"]

    if data["profile"]:
        person["profile"] = data["profile"]

    persons.append(person)
    f = open("data.json", "w")
    f.write(json.dumps(persons, indent=4))
    f.close()
