import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] area = new int[N+1][M+1];

        for(int n = 1; n < N+1; n++) {
            st = new StringTokenizer(br.readLine());
            for(int m = 1; m < M+1; m++) {
                area[n][m] = Integer.parseInt(st.nextToken());
            }
        }

        // 누적합1
        for(int n = 1; n < N+1; n++) {
            for(int m = 2; m < M+1; m++) {
                area[n][m] += area[n][m-1];
            }
        }

        // 누적합2
        for(int n = 2; n < N+1; n++) {
            for(int m = 1; m < M+1; m++) {
                area[n][m] += area[n-1][m];
            }
        }

        int K = Integer.parseInt(br.readLine());

        int x1, y1, x2, y2;
        for(int k = 0; k < K; k++) {
            st = new StringTokenizer(br.readLine());
            y1 = Integer.parseInt(st.nextToken());
            x1 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());

            sb.append(area[y2][x2] - area[y1-1][x2] - area[y2][x1-1] + area[y1-1][x1-1]).append("\n");
        }

        System.out.println(sb);
        

    }

}
