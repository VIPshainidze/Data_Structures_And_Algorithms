public class Stack {
    private int count = 0;
    private int size = 5;
    private int[] mainArray = new int[this.size];

    protected int[] commonActions(int[] array_1) {
        int[] array_2 = new int[this.size];
        for (int index = 0; index < this.count; index ++) {
            array_2[index] = array_1[index];
        }
        return array_2;
    }

    protected void push(int element) {
        if (this.count < this.size) {
            this.mainArray[this.count] = element;
            this.count ++;
        }
        else {
            int[] helperArray = this.commonActions(this.mainArray);
            this.size += 5;
            this.mainArray = this.commonActions(helperArray);
            this.mainArray[this.count] = element;
            this.count ++;
        }
    }

    protected int pop() {
        int targetElement = this.mainArray[this.count - 1];
        this.count --;
        this.mainArray = this.commonActions(this.mainArray);

        return targetElement;
    }

    protected int peek() {
        return this.mainArray[this.count - 1];
    }

    protected int[] toList() {
        return this.mainArray;
    }

    protected boolean isEmpty() {
        return this.count == 0;
    }

    protected void clear() {
        this.count = 0;
        this.size = 5;
        this.mainArray = new int[this.size];
    }

    protected int length() {
        return this.count - 1;
    }

    protected void print() {
        for (int index = 0; index < this.count; index ++) {
            System.out.print(this.mainArray[index] + " ");
        }
    }


    public static void main(String[] args) {
        Stack stack = new Stack();
        for (int i = 0; i < 12; i ++) {
            stack.push(i);
        }
        stack.print();
        System.out.println();
        stack.toList();
        System.out.println(stack.pop());
        System.out.println();
        stack.print();
        stack.push(15);
        System.out.println(stack.peek());
        System.out.println(stack.isEmpty());
        System.out.println(stack.length());
        stack.clear();
        stack.print();
    }
}
