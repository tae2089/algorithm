import java.text.ParseException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.junit.jupiter.api.Test;

public class GreedyTest {
    


    @Test
    void bn14916(){
        int n = 14;
        int cnt = 0;
        while(true){
            if (n % 5  == 0){
                cnt += n/5;
                break;
            }else{
                n -=2;
                cnt+=1;
            }
            if(n < 0){
                break;
            }
        }
        if (n < 0 ){
            System.out.println(-1);
        }else{
            System.out.println(cnt);
        }
    }


    @Test
    void  bn1343(){
        int flag = 0;
        String input = "XX.XXXXXXXXXX..XXXXXXXX...XXXXXX";
        input = input.replaceAll("XXXX", "AAAA");
        input = input.replaceAll("XX", "BB");

        for(int i = 0; i <input.length(); i++){
            if(input.charAt(i)=='X'){
                flag = 1;
                break;
            }
        }
        if (flag == 0){
            System.out.println(input);
        }else{
            System.out.println(-1);
        }
    }

    @Test
    void pg1(){
        
        String x = "1500000000000000000000000000";
        String y = "44661111111111111111111111";
        List<String> result = new ArrayList<>();
        int findFriend = 0;
        
        for(int i = 0; i <x.length(); i++){
            String c = String.valueOf(x.charAt(i));
            boolean found =y.contains(String.valueOf(x.charAt(i)));
            // System.out.println(y);
            if(found){
                y = y.replaceFirst(c, "x");
                result.add(c);
                findFriend++;
            }
        }
        if(findFriend ==0){
            System.out.println("-1");
        }else{
            result.sort(Comparator.reverseOrder());
            int a = Integer.parseInt(String.join("", result));
            System.out.println(String.valueOf(a));
        }
    }


    @Test
    void pg2() {
        String s = "abccccdd";
        Set<Character> stringPool = new HashSet();
        int length = 0;
        for (int i  = 0; i < s.length(); i++) {
            Character key = s.charAt(i);
            System.out.println(stringPool.toString());
            if (stringPool.contains(key)) {
                length += 2;
                stringPool.remove(key);
            } else {
                stringPool.add(key);
            }
        }
        System.out.println(length);
    }


    @Test
    void leetCode409(){
        String s = "abccdddd";
        Set<Character> stringPool = new HashSet<>();

        int length = 0;

        for(int i=0; i<s.length(); i++){
            if(stringPool.contains(s.charAt(i))){
                length +=2;
                stringPool.remove(s.charAt(i));
            }else{
                stringPool.add(s.charAt(i));
            }
        }
        length = stringPool.isEmpty() ? length : length + 1;
    }


    
}
