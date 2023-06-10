import csv


def load_data() -> list[list[str]]:
    data = []
    with open('resources/maps_data/maps.csv', 'r') as f:
        for line in csv.reader(f, delimiter=','):
            data.append(line)
    return data


def save_data(csv_data: list[list[str]]):
    with open('resources/maps_data/maps.csv', 'w') as f:
        csv_writer = csv.writer(f, delimiter=',')
        for data in csv_data:
            csv_writer.writerow(data)


