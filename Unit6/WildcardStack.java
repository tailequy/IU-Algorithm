import java.util.Stack;

public class WildcardStack {
    private Stack<?> stack;

    public WildcardStack() {
        stack = new Stack<>();
    }

    public void push(Object item) {
        stack.push(item);
    }

    public Object pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return stack.pop();
    }

    public Object peek() {
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
        WildcardStack stack = new WildcardStack();
        stack.push(1);
        stack.push("Hello");
        stack.push(3.14);

        System.out.println("Top element: " + stack.peek()); // Output: Top element: 3.14
        System.out.println("Stack size: " + stack.size());  // Output: Stack size: 3

        while (!stack.isEmpty()) {
            System.out.println("Popped element: " + stack.pop());
        }
        // Output:
        // Popped element: 3.14
        // Popped element: Hello
        // Popped element: 1
    }
}
