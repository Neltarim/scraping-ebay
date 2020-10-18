import json
from os import system as sc

def test():
    sc("rm data/test_res.json && touch data/test_res.json")
    with open("data/product.json", "r") as file:
        data = json.load(file)

    rejected, accepted = [], []

    for prod in data:
        if accurate("pins animators aurore", prod):
            accepted.append(prod['Name'])

        else:
            rejected.append(prod['Name'])

    data = {
        'accepted': accepted,
        'rejected': rejected,
        'total': {
            'accepted' : len(accepted),
            'rejected' : len(rejected)
            }
        }

    with open('data/test_res.json', 'w') as file:
        json.dump(data, file, indent=4, separators=(',', ': '))

def accurate(search_string, prod):

    if prod['Price'] == None:
        return False

    search_string = search_string.upper()
    keywords = search_string.split()
    name = prod['Name'].replace("\'", "")
    name = name.upper()
    name_sp = name.split()

    kc = len(keywords)
    max_tol = len(keywords) / 3

    for key in keywords:
        for word in name_sp:

            if word == key:
                kc -= 1

    if kc > max_tol:
        return False

    else:
        return True

def get_object(search_string):
    sc("rm data/product.json && touch data/product.json")
    sc("scrapy crawl ebay -o data/product.json -a search=\"" + search_string + "\"")

    with open("data/product.json", "r") as file:
        data = json.load(file)

    return data


def process(search_string):

    data = get_object(search_string)

    i, ipr = 0, 0

    for prod in data:
        i += 1
        if accurate(search_string, prod):
            ipr += 1
            print(prod['Name'] + ": " + prod['Price'])

    print(str(i) + ", " + str(ipr))

if __name__ == "__main__":
    #process("pins disney animators aurore")
    test()