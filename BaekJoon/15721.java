import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int A = Integer.parseInt(br.readLine());
        int T = Integer.parseInt(br.readLine());
        int G = Integer.parseInt(br.readLine());

        int n = 1, answer = -1;

        // 싸이클
        while((n + 3) < T) {
            answer += (2 * n + 6);
            T -= (n + 3);
            n++;
        }

        // 뻔(0)
        if(G == 0) {
            if(T == 1) answer += 1;
            else if(T == 2) answer += 3;
            else if(2 < T) answer += T+2;
        }

        // 데기(1)
        if(G == 1) {
            if(T == 1) answer += 2;
            else if(T == 2) answer += 4;
            else if(2 < T) answer += n+T+3;
        }

        System.out.println(answer%A);

    }

}
