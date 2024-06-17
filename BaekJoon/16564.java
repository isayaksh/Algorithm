import java.io.*;
import java.util.*;

public class Main {

    private static int N;
    private static long K;
    private static long[] X;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // INPUT
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Long.parseLong(st.nextToken());

        X = new long[N];

        for(int n = 0; n < N; n++) X[n] = Long.parseLong(br.readLine());

        // SOLUTION
        long answer = X[0];
        int n;

        Arrays.sort(X);

        for(n = 1; n < N; n++) {

            if(K < (X[n] - X[n-1]) * n) break;

            K -= (X[n] - X[n-1]) * n;
            answer = X[n];

        }
        
        System.out.println(answer + (K / n));

    }
    
}
