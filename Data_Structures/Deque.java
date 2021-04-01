import java.util.Arrays;
import java.util.NoSuchElementException;

public class Deque {

    private int totalSize;
    private int count;
    private int[] mainDeque;

    Deque() {}

    Deque(int total_size) {
        this.totalSize = total_size;
        this.count = 0;
        this.mainDeque = new int[this.totalSize];
    }

    private void rightShiftElements() { // დეკის ელემენტების ერთი ბიჯით ძვრა მარჯვნივ
        for (int index = this.totalSize - 1; index > 0; index --) {
            this.mainDeque[index] = this.mainDeque[index - 1];
        }
    }

    private void leftShiftElements() { // დეკის ელემენტების ერთი ბიჯით ძვრა მარცხვნივ
        for (int index = 1; index < this.count; index ++) {
            this.mainDeque[index - 1] = this.mainDeque[index];
        }
        this.mainDeque[this.count - 1] = 0;
    }

    private int front() throws NoSuchFieldException { // მიმართვა დეკის სათავეზე
        if (this.isEmpty()) {
            throw new NoSuchFieldException("The deque is empty");
        }
        else {
            return this.mainDeque[0];
        }
    }

    private int back() throws NoSuchFieldException { // მიმართვა დეკის ბოლოზე
        if (this.isEmpty()) {
            throw new NoSuchFieldException("The deque is empty");
        }
        else {
            return this.mainDeque[this.count - 1];
        }
    }

    private void pushFront(int element) { // ელემენტის ჩამატება დეკის სათავეში
        if (this.isFull()) {
            return;
        }
        this.rightShiftElements();
        this.mainDeque[0] = element;
        this.count ++;
    }

    private void pushBack(int element) { // ელემენტის ჩამატება დეკის ბოლოში
        if (this.isFull()) {
            return;
        }
        this.mainDeque[this.count] = element;
        this.count ++;
    }

    private int popFront() throws NoSuchFieldException { // ელემენტის წაშლა დეკის სათავეში
        if (this.isEmpty()) {
            throw new NoSuchFieldException("The deque is empty");
        }
        else {
            final int TARGET_ELEMENT = this.mainDeque[0];
            this.leftShiftElements();
            this.count --;
            return TARGET_ELEMENT;
        }
    }

    private int popBack() throws NoSuchElementException { // ელემენტის წაშლა დეკის ბოლოში
        if (this.isEmpty()) {
            throw new NoSuchElementException("The deque is empty");
        }
        else {
            final int TARGET_ELEMENT = this.mainDeque[this.count - 1];
            this.mainDeque[this.count - 1] = 0;
            this.count --;
            return TARGET_ELEMENT;
        }
    }

    private int size() { // აბრუნებს დეკში არსებულ ელემენტთა რაოდენობას
        return this.count;
    }

    private int totalSize() { // აბრუნებს დეკში შესაძლო არსებულ ელემენტთა მაქსიმალურ რაოდენობას
        return this.totalSize;
    }

    private boolean isEmpty() { // გვატყობინებს არის თუ არა დეკი ცარიელი: (True/False)
        return this.count == 0;
    }

    private boolean isFull() { //  გვატყობინებს არის თუ არა დეკი სავსე: (true/false)
        return this.count == this.totalSize;
    }

    private int[] toList() { // აბრუნებს დეკს სიად (სასარგებლო ილუზია :)))
        int[] dequeToList;
        if (this.isEmpty()) {
            return new int[0];
        }
        else {
            dequeToList = new int[this.count];
            for (int index = 0; index < this.count; index ++) {
                dequeToList[index] = this.mainDeque[index];
            }
        }
        return dequeToList;
    }

    private void print() { // პრინტავს დეკში დამატებულ ელემენტებს
        for (int index = 0; index < this.count; index ++) { // პრინტავს დეკში დამატებულ ელემენტებს
            System.out.print(this.mainDeque[index] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) throws NoSuchFieldException {
        Deque deque = new Deque(5);

        deque.pushFront(1);
        deque.pushFront(2);
        deque.pushBack(3);
        deque.pushBack(4);
        deque.pushFront(5);
        deque.popFront();
        deque.pushFront(6);
        deque.print();
        System.out.println(deque.size());
        System.out.println(deque.popBack());
        System.out.println(deque.popFront());
        deque.print();
        deque.pushFront(10);
        deque.print();
        System.out.println("---------------------");
        System.out.println(deque.size());
        System.out.println(deque.isFull());
        System.out.println(deque.totalSize());
        int [] dequeToList = deque.toList();
        System.out.println(Arrays.toString(dequeToList));
        System.out.println(deque.front());
        System.out.println(deque.back());
    }
}
