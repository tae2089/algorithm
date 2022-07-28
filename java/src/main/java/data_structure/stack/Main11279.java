package data_structure.stack;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

/**
 * Main11279
 */
public class Main11279 {
    private static final String NEWLINE = System.getProperty("line.separator");
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(reader.readLine());
        PriorityQueue<Integer> queue =new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 0; i < N; i++){
            int input = Integer.parseInt(reader.readLine());
            if(input == 0){
                int num = queue.isEmpty() ? 0 :queue.poll();
                sb.append(num).append(NEWLINE);
            }else{
                queue.add(input);
            }
        }
        System.out.println(sb.toString());
    }
}