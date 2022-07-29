package leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class SolutionA {

    public boolean isAnagram242(String s, String t) {
        char[] sCharArr = s.toCharArray();
        char[] tCharArr = t.toCharArray();

        Arrays.sort(sCharArr);
        Arrays.sort(tCharArr);
        return Arrays.equals(tCharArr, sCharArr);
    }


    public String seTest(){
        return "hello";
    }



}
