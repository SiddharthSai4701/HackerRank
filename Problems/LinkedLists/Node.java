package Problems.LinkedLists;

public class Node {

    // Two properties

    // Reference to the next node
    Node next;

    // Assuming data is an integer. Could be any data type
    int data;

    // We will have two constructors

    public Node(int newData) {
        data = newData;
    }

    public Node(int newData, Node newNext) {

        data = newData;
        next = newNext;
    }

    // Getters and Setter

    // Get the data in the node
    public int getData() {
        return data;
    }

    // Get the next node
    public Node getNext() {
        return next;
    }

    // Set data to be the new data
    public void setData(int newData) {
        data = newData;
    }

    // Set next to point to the next node
    public void setNext(Node newNext) {
        next = newNext;
    }

}
