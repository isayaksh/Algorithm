import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N, answer;
        int[] profit;

        while(true) {
            N = Integer.parseInt(br.readLine());
            if(N == 0) break;

            answer = Integer.MIN_VALUE;
            profit = new int[N];
            for(int n = 0; n < N; n++) {
                profit[n] = Integer.parseInt(br.readLine());
            }

            // function
            for(int n = 1; n < N; n++) {
                if(profit[n] < profit[n-1] + profit[n]) profit[n] = profit[n-1] + profit[n];
                if(answer < profit[n]) answer = profit[n];
            }

            sb.append(answer).append("\n");

        }

        System.out.println(sb);

    }

}
