import java.io.*;
import java.util.*;

public class Main {

    private static long[] recurrenceRelation = new long[36];

    public static void main(String[] args) throws Exception {

        // ======= INPUT =======
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());

        System.out.println(function(n));

    }

    private static long function(int n) {

        if(n == 0 || n == 1) return 1L;

        long answer = 0;

        for(int i = 0; i < n; i++) {
            if(recurrenceRelation[i] == 0) recurrenceRelation[i] = function(i);
            if(recurrenceRelation[n-i-1] == 0) recurrenceRelation[n-i-1] = function(n-i-1);
            answer += recurrenceRelation[i]*recurrenceRelation[n-i-1];
        }

        return answer;
    }

}
