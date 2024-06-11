import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        long N = Long.parseLong(br.readLine());
        long F = Long.parseLong(br.readLine());

        long T = N - (N % 100L);

        for(long n = 0; n < 100; n++) {
            if((T + n) % F != 0) continue;
            System.out.println(String.format("%02d", n));
            break;
        }
        

    }
    
}
