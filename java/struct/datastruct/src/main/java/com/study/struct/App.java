package com.study.struct;

/**
 * Hello world!
 */
public final class App {
    private App() {
    }

    /**
     * Says hello to the world.
     * 
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {
        System.out.println("Hello World!");
        StudyQueue<Integer> queue = new StudyQueue<>();
        queue.add(1);
        queue.add(2);
        queue.add(3);
        System.out.println(queue.getFistValue());
        queue.firstRemove();
        System.out.println(queue.getFistValue());
    }
}
