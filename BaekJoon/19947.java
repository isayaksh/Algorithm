import java.io.*;
import java.util.*;

public class Main {

    private static long H, Y;
    private static long answer = 0;

    public static void main(String[] args) throws Exception {

        // ======= INPUT =======
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        H = Long.parseLong(st.nextToken());
        Y = Long.parseLong(st.nextToken());

        dfs(H, Y);

        System.out.println(answer);

    }

    private static void dfs(long h, long y) {
        answer = Math.max(answer, h);

        if(y >= 1) dfs((long) Math.floor(h * 1.05), y-1);
        if(y >= 3) dfs((long) Math.floor(h * 1.20), y-3);
        if(y >= 5) dfs((long) Math.floor(h * 1.35), y-5);

    }

}
