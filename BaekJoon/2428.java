import java.io.*;
import java.util.*;

public class Main {

    private static int N;
    private static int[] files;

    public static void main(String[] args) throws Exception {

        // ======= INPUT =======
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        
        st = new StringTokenizer(br.readLine());

        files = new int[N];
        for(int n = 0; n < N; n++) {
            files[n] = Integer.parseInt(st.nextToken());
        }

        // ======= SOLUTION =======
        long answer = 0;
        
        Arrays.sort(files);

        for(int n = 0; n < N-1; n++) {
            answer += (binarySearch(n) - n);
        }

        System.out.println(answer);
        
    }

    private static int binarySearch(int idx) {
        int start = idx+1;
        int end = N-1;
        int answer = idx+1;
        int mid = 0;

        if(files[idx] * 10 < files[idx+1] * 9) return idx;

        while(start <= end) {
            mid = (start + end) / 2;
            
            if(files[idx] <= files[mid] && files[idx] * 10 >= files[mid] * 9) {
                answer = mid;
                start = mid+1;
            }
            else {
                end = mid-1;
            }
        }

        return answer;
    }

}
