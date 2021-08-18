package com.study.struct;

import java.util.LinkedList;

public class StudyQueue<T> {

    private LinkedList<T> queue;

    public StudyQueue() {
        queue = new LinkedList<T>();
    }

    public LinkedList<T> getQueue() {
        return this.queue;
    }

    public Boolean add(T t) {
        return this.queue.add(t);
    }

    public T getFirstIndexAndRemove() {
        return this.queue.poll();
    }

    public T getFistValue() {
        return this.queue.peek();
    }

    public void firstRemove() {
        this.queue.remove();
    }

    public void removeAll() {
        this.queue.clear();
    }

    public int getSize() {
        return this.queue.size();
    }
}
