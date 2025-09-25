
# 10. Create a class Reverse that implements the iterator protocol to iterate over a list in reverse 
# order using the __iter__() and __next__() methods.
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    reverse_iter = Reverse(my_list)
    for item in reverse_iter:
        print(item)