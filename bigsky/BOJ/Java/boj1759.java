import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj1759 {

    static int L, C;
    static char[] chars;
    static char[] password;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        chars = new char[C];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            chars[i] = st.nextToken().charAt(0);
        }

        Arrays.sort(chars);

        password = new char[L];
        generatePassword(0, 0);
    }

    public static void generatePassword(int index, int depth) {
        if (depth == L) {
            if (isValidPassword()) {
                System.out.println(String.valueOf(password));
            }
            return;
        }

        if (index == C) {
            return;
        }

        password[depth] = chars[index];
        generatePassword(index + 1, depth + 1);
        generatePassword(index + 1, depth);
    }

    public static boolean isValidPassword() {
        int vowelCount = 0;
        int consonantCount = 0;
        for (char ch : password) {
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                vowelCount++;
            } else {
                consonantCount++;
            }
        }
        return vowelCount >= 1 && consonantCount >= 2;
    }
}
