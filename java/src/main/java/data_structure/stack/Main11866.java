package data_structure.stack;

import java.util.LinkedList;
import java.util.Scanner;

public class Main11866 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        LinkedList<Integer> list = new LinkedList<>();

        int N = in.nextInt();
        int K = in.nextInt();

        for(int i = 1; i <= N; i++) {
            list.add(i);
        }

        StringBuilder sb = new StringBuilder();
        sb.append('<');

        int index = 0;

        while(list.size() > 1){
            index = (index +(K-1))%list.size();
            sb.append(list.remove(index)).append(", ");
        }
        // 마지막으로 남은 요소 삭제함과 동시에 출력
        sb.append(list.remove()).append('>');
        System.out.println(sb);
    }
}
