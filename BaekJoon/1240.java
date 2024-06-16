import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int N, M, n1, n2, w;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[][] graph = new int[N+1][N+1];

        for(int y = 1; y < N+1; y++) {
            for(int x = 1; x < N+1; x++) {
                graph[y][x] = Integer.MAX_VALUE;
            }
        }

        for(int n = 0; n < N-1; n++) {
            st = new StringTokenizer(br.readLine());
            n1 = Integer.parseInt(st.nextToken());
            n2 = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());

            graph[n1][n2] = w;
            graph[n2][n1] = w;

        }
        
        for(int i = 1; i < N+1; i++) {
            for(int j = 1; j < N+1; j++) {
                for(int k = 1; k < N+1; k++) {
                    if(graph[j][i] == Integer.MAX_VALUE || graph[i][k] == Integer.MAX_VALUE) continue;
                    if(graph[j][k] > graph[j][i] + graph[i][k]) graph[j][k] = graph[j][i] + graph[i][k];
                }
            }
        }

        for(int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());
            n1 = Integer.parseInt(st.nextToken());
            n2 = Integer.parseInt(st.nextToken());
            
            sb.append(graph[n1][n2]).append("\n");
        }

        System.out.println(sb);

    }
    
}
