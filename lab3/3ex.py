class Unique:
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.items = iter(items)
    
    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.items)
            comparison_item = item.lower() if self.ignore_case and isinstance(item, str) else item
            
            if comparison_item not in self.seen:
                self.seen.add(comparison_item)
                return item
if __name__ == "__main__":
    data = [1, 1, 1, 2, 2, 2, 3, 3]
    for i in Unique(data):
        print(i) 
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data):
        print(i) 
    for i in Unique(data, ignore_case=True):
        print(i) 