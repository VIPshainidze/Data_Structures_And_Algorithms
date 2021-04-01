
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
        for index in range(self.__count):
            print(self.__main_array[index], end=" ")
        print()

    def get_count(self):
        return self.__count

    def __getitem__(self, item):
        return self.__main_array[item]

    def __setitem__(self, key, value):
        self.__main_array[key] = value

    def decrement_count(self):
        self.__count -= 1


class Queue:

    def __init__(self):
        self.__count = 0
        self.__main_queue = Stack()

    def push(self, element):  # ელემენტის ჩამატება რიგის ბოლოში
        self.__main_queue.push(element)
        self.__count += 1

    def pop(self):
        target_element = self.__main_queue[0]
        for index in range(1, self.__count):
            self.__main_queue[index - 1] = self.__main_queue[index]
        self.__main_queue[self.__count - 1] = 0
        self.__count -= 1
        self.__main_queue.decrement_count()
        return target_element

    def front(self):
        if self.is_empty():
            return
        return self.__main_queue[0]

    def back(self):  # მიმართვა ბოლოში მყოფ ელემენტზე
        if self.is_empty():
            return
        return self.__main_queue[self.__count - 1]

    def size(self):  # ეს ფუნქცია აბრუნებს რიგში არსებულ ელემენტთა რაოდენობას
        return self.__count

    def is_empty(self):  # გვატყობინებს არის თუ არა დეკი ცარიელი: (True/False)
        return self.__main_queue.is_empty()

    def to_list(self):  # აბრუნებს დეკს ორმაგ ბმულ სიად
        return self.__main_queue.to_list()

    def print(self):  # პრინტავს დეკში დამატებულ ელემენტებს
        self.__main_queue.show()


if __name__ == '__main__':
    queue = Queue()
    for number in range(1, 1 + 12):
        queue.push(number)
    queue.print()
    print(queue.pop())
    queue.print()
    queue.push(20)
    queue.print()
    queue.pop()
    queue.print()
    queue.push(100)
    queue.print()
    print(queue.front())
    print(queue.back())
    print(queue.size())
    print(queue.is_empty())
    main_list = queue.to_list()
    print(main_list)
