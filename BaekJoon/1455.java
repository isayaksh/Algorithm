import java.io.*;
import java.util.*;

public class Main {

    private static int N, M;

    private static int[][] coins;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // INPUT
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        coins = new int[N][M];

        for(int n = 0; n < N; n++) {
            String[] input = br.readLine().split("");
            for(int m = 0; m < M; m++) {
                coins[n][m] = Integer.parseInt(input[m]);
            }
        }

        int answer = 0;

        // SOLUTION
        for(int n = N-1; 0 <= n; n--) {
            for(int m = M-1; 0 <= m; m--) {
                if(coins[n][m] == 1) {
                    reverse(n, m);
                    answer++;
                }
            }
        }

        System.out.println(answer);

    }

    private static void reverse(int tn, int tm) {
        for(int n = 0; n <= tn; n++) {
            for(int m = 0; m <= tm; m++) {
                coins[n][m] = coins[n][m] == 0 ? 1 : 0;
            }
        }
    }
    
}
