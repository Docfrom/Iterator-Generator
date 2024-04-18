nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

nested_list_2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]
class FlatIterator:

    def __init__(self, nested_list):
        self.list = nested_list
        self.flatten_list = []
        self._flat_list(self.list)


    def __iter__(self):
        self.start = 0
        self.end = len(self.flatten_list)
        return self

    def __next__(self):
        if self.start < self.end:
            self.start +=1
            return self.flatten_list[self.start-1]
        else:
            raise StopIteration

    def _flat_list(self, element):
        if (type(element) == list):
            for elem in element:
                self._flat_list(elem)
        else:
            self.flatten_list.append(element)
            return element

def flat_generator(nested_list: list):
    flatten_list: list = []
    def _flat_list(elem):
        if(type(elem) == list):
            for e in elem:
                _flat_list(e)
        else:
            flatten_list.append(elem)
            return elem
    _flat_list(nested_list)
    for elem in flatten_list:
        yield elem


test_list = FlatIterator(nested_list)
for item in test_list:
    print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

test_list = FlatIterator(nested_list_2)
for item in test_list:
    print(item)
flat_list = [item for item in FlatIterator(nested_list_2)]
print(flat_list)