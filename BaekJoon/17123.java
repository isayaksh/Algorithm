import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T, N, M, r1, c1, r2, c2, v, total;
        int[][] A, AA;

        T = Integer.parseInt(br.readLine());
        
        for(int t = 0; t < T; t++) {

            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            A = new int[N+1][N+1];
            AA = new int[N+2][N+2];

            for(int y = 1; y < N+1; y++) {
                st = new StringTokenizer(br.readLine());
                for(int x = 1; x < N+1; x++) {
                    A[y][x] = Integer.parseInt(st.nextToken());
                }
            }

            for(int m = 0; m < M; m++) {
                st = new StringTokenizer(br.readLine());
                r1 = Integer.parseInt(st.nextToken());
                c1 = Integer.parseInt(st.nextToken());
                r2 = Integer.parseInt(st.nextToken());
                c2 = Integer.parseInt(st.nextToken());
                v = Integer.parseInt(st.nextToken());

                for(int r = r1; r <= r2; r++) {
                    AA[r][c1] += v;
                    AA[r][c2+1] -= v;
                }

            }

            for(int r = 1; r < N+1; r++) {
                for(int c = 1; c < N+1; c++) {
                    AA[r][c] += AA[r][c-1];
                }
            }

            for(int r = 1; r < N+1; r++) {
                total = 0;
                for(int c = 1; c < N+1; c++) total += (A[r][c] + AA[r][c]);
                sb.append(total).append(" ");
            }

            sb.append("\n");

            for(int c = 1; c < N+1; c++) {
                total = 0;
                for(int r = 1; r < N+1; r++) total += (A[r][c] + AA[r][c]);
                sb.append(total).append(" ");
            }

            sb.append("\n");

        }

        System.out.println(sb);

    }
    
}
