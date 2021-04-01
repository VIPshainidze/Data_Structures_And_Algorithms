from array import array


class Deque:

    def __init__(self, total_size):
        self.__total_size = total_size
        self.__count = 0
        self.__main_deque = array("i", [0 for _ in range(self.__total_size)])

    def right_shift_elements(self):  # დეკის ელემენტების ერთი ბიჯით ძვრა მარჯვნივ
        for index in range(self.__total_size - 1, 0, -1):
            self.__main_deque[index] = self.__main_deque[index - 1]

    def left_shift_elements(self):  # დეკის ელემენტების ერთი ბიჯით ძვრა მარცხვნივ
        for index in range(1, self.__count):
            self.__main_deque[index - 1] = self.__main_deque[index]
        self.__main_deque[self.__count - 1] = 0

    def front(self):  # მიმართვა დეკის სათავეზე
        if self.is_empty():
            return None
        return self.__main_deque[0]

    def back(self):  # მიმართვა დეკის ბოლოზე
        if self.is_empty():
            return None
        return self.__main_deque[self.__count - 1]
    
    def push_front(self, element):  # ელემენტის ჩამატება დეკის სათავეში
        if self.is_full():
            return None
        self.right_shift_elements()
        self.__main_deque[0] = element
        self.__count += 1

    def push_back(self, element):  # ელემენტის ჩამატება დეკის ბოლოში
        if self.is_full():
            return None
        self.__main_deque[self.__count] = element
        self.__count += 1

    def pop_front(self):  # ელემენტის წაშლა დეკის სათავეში
        if self.is_empty():
            return None
        target_element = self.__main_deque[0]
        self.left_shift_elements()
        self.__count -= 1
        return target_element

    def pop_back(self):  # ელემენტის წაშლა დეკის ბოლოში
        if self.is_empty():
            return None
        target_element = self.__main_deque[self.__count - 1]
        self.__main_deque[self.__count - 1] = 0
        self.__count -= 1
        return target_element

    def size(self):  # აბრუნებს დეკში არსებულ ელემენტთა რაოდენობას
        return self.__count

    def total_size(self):  # აბრუნებს დეკში შესაძლო არსებულ ელემენტთა მაქსიმალურ რაოდენობას
        return self.__total_size

    def is_empty(self):  # გვატყობინებს არის თუ არა დეკი ცარიელი: (True/False)
        return self.__count == 0

    def is_full(self):  # გვატყობინებს არის თუ არა დეკი სავსე: (True/False)
        return self.__count == self.__total_size

    def to_list(self):  # აბრუნებს დეკს ორმაგ ბმულ სიად
        if self.is_empty():
            return []
        return [self.__main_deque[index] for index in range(self.__count)]

    def print(self):  # პრინტავს დეკში დამატებულ ელემენტებს
        for index in range(self.__count):
            print(self.__main_deque[index], end=" ")
        print()


if __name__ == "__main__":
    deque = Deque(5)
    deque.push_front(1)
    deque.push_front(2)
    deque.push_back(3)
    deque.push_back(4)
    deque.push_front(5)
    deque.pop_front()
    deque.push_front(6)
    deque.print()
    print(deque.size())
    print(deque.pop_back())
    print(deque.pop_front())
    deque.print()
    deque.push_front(10)
    deque.print()
    print("-----------")
    print(deque.size())
    print(deque.is_full())
    print(deque.is_full())
    print(deque.total_size())
    deque_to_list = deque.to_list()
    print(deque_to_list)
    print(deque.front())
    print(deque.back())
