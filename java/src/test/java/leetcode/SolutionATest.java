package leetcode;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;


import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SolutionATest {

   static SolutionA solution;

    @BeforeAll
    public static void beforeAllSetup(){
        solution = new SolutionA();
    }


    @Test
    void testIsAnagram242() {
        boolean result = solution.isAnagram242("asd","asd");
        System.out.println("result = " + result);
        assertTrue(result);
    }

    @Test
    void seTestCode(){
        String result = solution.seTest();
        System.out.println("result = " + result);
         assertEquals("hello",result);
    }


}
