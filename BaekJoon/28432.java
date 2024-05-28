import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        // ======= INPUT =======
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] concludingRemarks = new String[N];
        for(int n = 0; n < N; n++) {
            concludingRemarks[n] = br.readLine();
        }

        int M = Integer.parseInt(br.readLine());
        String[] candidate = new String[M];
        for(int m = 0; m < M; m++) {
            candidate[m] = br.readLine();
        }

        // ======= SOLUTION =======

        char start = ' ', end = ' ';
        Set<String> usedWord = new HashSet<String>();

        for(int n = 0; n < N; n++) {
            if(concludingRemarks[n].equals("?")) {
                start = n > 0 ? concludingRemarks[n-1].charAt(concludingRemarks[n-1].length()-1) : ' ';
                end = n < N-1 ? concludingRemarks[n+1].charAt(0) : ' ';
            }
            if(!concludingRemarks[n].equals("?")) {
                usedWord.add(concludingRemarks[n]);
            }
        }

        for(int m = 0; m < M; m++) {
            if(usedWord.contains(candidate[m])) continue;

            if(start == ' ' && end == ' ') {
                System.out.println(candidate[m]);
                return;
            }
            else if(start == ' ') {
                if(candidate[m].charAt(candidate[m].length()-1) == end) {
                    System.out.println(candidate[m]);
                    return;
                }
            }
            else if(end == ' ') {
                if(candidate[m].charAt(0) == start) {
                    System.out.println(candidate[m]);
                    return;
                }
            }
            
            else {
                if(candidate[m].charAt(candidate[m].length()-1) == end && candidate[m].charAt(0) == start) {
                    System.out.println(candidate[m]);
                    return;
                }
            }
        }

    }

}
