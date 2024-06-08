import java.io.*;
import java.util.StringTokenizer;

public class Main {

    private static int N, M;

    private static int[][] J, O, I;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());

        J = new int[N+1][M+1];
        O = new int[N+1][M+1];
        I = new int[N+1][M+1];

        for(int n = 1; n < N+1; n++) {
            char[] input = br.readLine().toCharArray();
            for(int m = 1; m < M+1; m++) {
                if(input[m-1] == 'J') J[n][m] = 1;
                if(input[m-1] == 'O') O[n][m] = 1;
                if(input[m-1] == 'I') I[n][m] = 1;
            }
        }

        // 누적합 초기화
        for(int n = 1; n < N+1; n++) {
            for(int m = 2; m < M+1; m++) {
                J[n][m] += J[n][m-1];
                O[n][m] += O[n][m-1];
                I[n][m] += I[n][m-1];
            }
        }

        for(int n = 2; n < N+1; n++) {
            for(int m = 1; m < M+1; m++) {
                J[n][m] += J[n-1][m];
                O[n][m] += O[n-1][m];
                I[n][m] += I[n-1][m];
            }
        }

        int x1, y1, x2, y2;
        for(int k = 0; k < K; k++) {
            st = new StringTokenizer(br.readLine());

            y1 = Integer.parseInt(st.nextToken());
            x1 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());

            sb.append(J[y2][x2] - J[y2][x1-1] - J[y1-1][x2] + J[y1-1][x1-1]).append(" ")
            .append(O[y2][x2] - O[y2][x1-1] - O[y1-1][x2] + O[y1-1][x1-1]).append(" ")
            .append(I[y2][x2] - I[y2][x1-1] - I[y1-1][x2] + I[y1-1][x1-1]).append("\n");
        }

        System.out.println(sb);

    }



}
