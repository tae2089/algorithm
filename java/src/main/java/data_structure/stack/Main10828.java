package data_structure.stack;

import common.FastReader;

import java.util.Stack;

public class Main10828 {
    public static void main(){
        FastReader rd = new FastReader();
        int n = rd.nextInt();
        Stack<String> stack = new Stack<>();

        StringBuilder out = new StringBuilder();
        for(int i=0;i<n;i++){
            String[] Line = rd.nextLine().split(" ");
            String cmd = Line[0];

            if(cmd.equals("push")) {
                stack.push(Line[1]);
            }
            else if(cmd.equals("pop")) {
                if(stack.empty()){
                    out.append("-1");
                }
                else {
                    out.append(stack.peek());
                    stack.pop();
                }
                out.append("\n");
            }
            else if(cmd.equals("size")) {
                out.append(stack.size() + "\n");
            }
            else if(cmd.equals("empty")) {
                out.append(stack.empty() ? "1" : "0");
                out.append("\n");
            }
            else if(cmd.equals("top")) {
                if(stack.empty()){
                    out.append("-1\n");
                }
                else {
                    out.append(stack.peek() + "\n");
                }
            }
        }
        System.out.print(out);
    }
}
