try:
    import _pickle as pickle
except ImportError:
    import pickle


class Example:
    int = 35
    str = 'Itay'
    list = [1, 2, 3]
    set = {a for a in range(3, 6)}


obj = Example()

pickle_obj = pickle.dumps(obj)

print(f"My obj:\n{pickle_obj}\n")

obj.int = 36

un_pickle = pickle.loads(pickle_obj)

print(
    f"int of unpickle is:\n{un_pickle.int}"
)