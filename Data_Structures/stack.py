```
from array import array


class Stack:

    def __init__(self):
        self.__count = 0
        self.__size = 5
        self.__main_array = array("i", [0 for _ in range(self.__size)])

    def __str__(self):
        return str(self.__main_array[:self.__count])[11:-1]

    def common_actions(self, array_1):
        array_2 = array("i", [0 for _ in range(self.__size)])
        for index in range(self.__count):
            array_2[index] = array_1[index]
        return array_2

    def push(self, element):
        if self.__count < self.__size:
            self.__main_array[self.__count] = element
            self.__count += 1
        else:
            helper_array = self.common_actions(self.__main_array)
            self.__size += 5
            self.__main_array = self.common_actions(helper_array)
            self.__main_array[self.__count] = element
            self.__count += 1

    def pop(self):
        target_element = self.__main_array[self.__count - 1]
        self.__count -= 1
        self.__main_array = self.common_actions(self.__main_array)
        return target_element

    def peek(self):
        return self.__main_array[self.__count - 1]

    def to_list(self):
        return [self.__main_array[index] for index in range(self.__count)]  # აქ self.__main_array[self.__count - 1]-ის
        # დაბრუნებაც შეიძლებოდა, მაგრამ ვიზუალური კუთხით ესე რო მიუვიდეს იუზერს უკეთესია.

    def is_empty(self):
        return self.__count == 0

    def clear(self):
        self.__count = 0
        self.__size = 5
        self.__main_array = array("i", [0 for _ in range(self.__size)])

    def show(self):
        return self.__str__()


if __name__ == '__main__':
    stack = Stack()

    for number in range(12):
        stack.push(number)

    print(stack)
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
    print(stack.peek())
    print(stack)
    listed_stack = stack.to_list()
    print(listed_stack)
    listed_stack.append(123)
    print(listed_stack)
    
```
