import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        StringTokenizer st;

        int T, N, M;

        T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            for(int m = 0; m < M; m++) br.readLine();

            // N개 모든 국가를 여행할 수 있는 최소 개수는 N-1개이다.
            sb.append(N-1).append("\n");
        }

        System.out.println(sb);

    }

}
