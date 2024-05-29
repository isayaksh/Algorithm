import java.io.*;
import java.util.*;

public class Main {

    private static final int[] dx = {1, -1, 0, 0};
    private static final int[] dy = {0, 0, 1, -1};

    private static int N, M, K;
    private static boolean[][] board;

    public static void main(String[] args) throws IOException {

        // ======= INPUT =======
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        board = new boolean[N][M];

        for(int k = 0; k < K; k++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            board[r-1][c-1] = true;
        }

        // ======= SOLUTION =======

        int answer = 0;

        for(int r = 0; r < N; r++) {
            for(int c = 0; c < M; c++) {
                if(!board[r][c]) continue;
                board[r][c] = false;
                answer = Math.max(answer, dfs(c, r));
            }
        }
        
        System.out.println(answer);

    }

    private static int dfs(int x, int y) {
        int count = 1;
        int nx, ny;

        for(int i = 0; i < 4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];
            if(nx < 0 || nx >= M || ny < 0 || ny >= N || !board[ny][nx]) continue;
            board[ny][nx] = false;
            count += dfs(nx, ny);
        }

        return count;
    }

}
