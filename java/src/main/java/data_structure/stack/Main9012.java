package data_structure.stack;

import common.FastReader;

public class Main9012 {
    public static void main(String [] args){
        FastReader fastReader = new FastReader();
        StringBuilder stringBuilder = new StringBuilder();
        int n = fastReader.nextInt();
        while(n-- > 0){
            stringBuilder.append(solve(fastReader.nextLine()));
        }
    }

    private static String solve(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if(c == '{'){
                count += 1;
            }else if(count == 0){
               return "NO";
            } else{
                count -=1;
            }
        }
        if (count == 0) {
            return "YES";
        }
        else {
            return "NO";
        }
    }
}
