import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // INPUT
        int N = Integer.parseInt(br.readLine());
        
        long[] A = new long[N];
        for(int n = 0; n < N; n++) A[n] = Long.parseLong(br.readLine());

        // SOLUTION
        long MAX_VALUE = 0;
        long target = 0L;
        long answer = 0L;

        // 1. 가장 큰 값(MAX_VALUE) 찾기
        for(int n = 0; n < N; n++) if(MAX_VALUE < A[n]) MAX_VALUE = A[n];

        answer = MAX_VALUE - A[0];

        // 2. 빈칸 채우기
        for(int n = 0; n < N; n++) {
            if(target > A[n]) answer += (target - A[n]);
            target = A[n];
        }

        System.out.println(answer);

    }
    
}
