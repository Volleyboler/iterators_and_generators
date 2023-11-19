class FlatIterator:

    def __init__(self, list_of_lists: list):
        self.list_of_lists = list_of_lists
        self.amount_lists = len(list_of_lists)

    def __iter__(self):
        self.list_count = 0
        self.element_list_count = -1
        return self

    def __next__(self):
        """
        Также добавил обработку пустых списков
        """
        self.element_list_count += 1
        if self.element_list_count >= len(self.list_of_lists[self.list_count]):
            self.element_list_count = 0
            self.list_count += 1
            for lst in self.list_of_lists[self.list_count:]:
                if len(lst) == 0:
                    self.list_count += 1
                    continue
                else:
                    break
            else:
                raise StopIteration
        item = self.list_of_lists[self.list_count][self.element_list_count]
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        [],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
