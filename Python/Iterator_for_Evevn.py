class EvenNumbers:
    def __init__(self,limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 2
            return value
        else:
            raise StopIteration
        

limit = int(input("Enter limit: "))

even = EvenNumbers(limit)

print("Even numbers are: ")
for num in even:
    print(num)


    