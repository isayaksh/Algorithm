import java.io.*;
import java.util.*;

public class Main {

    private static final Map<String, Double> grade = new HashMap<String, Double>(){
        {
            put("A+", 4.5);
            put("A0", 4.0);
            put("B+", 3.5);
            put("B0", 3.0);
            put("C+", 2.5);
            put("C0", 2.0);
            put("D+", 1.5);
            put("D0", 1.0);
            put("F", 0.0);
        } 
    };

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        double score = 0;
        double total = 0;

        for(int i = 0; i < 20; i++) {
            String[] input = br.readLine().split(" ");

            if(input[2].equals("P")) continue;
            score += grade.get(input[2]) * Double.parseDouble(input[1]);
            total += Double.parseDouble(input[1]);
        }

        System.out.println(score/total);

        
    
    }

}
