try:
    import _pickle as pickle
except ImportError:
    import pickle


def load_data():
    with open('resources/maps_data/maps.pkl', 'rb') as f:
        data = pickle.load(f)
    return data


def save_data(*data):
    with open('resources/maps_data/maps.pkl', 'wb') as f:
        for sub_data in data:
            pickle.dump(sub_data, f)


