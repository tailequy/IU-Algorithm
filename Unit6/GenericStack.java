import java.util.Stack;

public class GenericStack<T> {
    private Stack<T> stack;

    public GenericStack() {
        stack = new Stack<>();
    }

    public void push(T item) {
        stack.push(item);
    }

    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return stack.pop();
    }

    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return stack.peek();
    }

    public boolean isEmpty() {
        return stack.isEmpty();
    }

    public int size() {
        return stack.size();
    }

    public static void main(String[] args) {
        // Example usage
        GenericStack<Integer> intStack = new GenericStack<>();
        intStack.push(1);
        intStack.push(2);
        intStack.push(3);

        System.out.println("Top element: " + intStack.peek()); // Output: Top element: 3
        System.out.println("Stack size: " + intStack.size());  // Output: Stack size: 3

        while (!intStack.isEmpty()) {
            System.out.println("Popped element: " + intStack.pop());
        }
        // Output:
        // Popped element: 3
        // Popped element: 2
        // Popped element: 1
    }
}