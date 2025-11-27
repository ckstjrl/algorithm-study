//BOJ1673(D1): 치킨 쿠폰
import java.util.Scanner;

public class boj1673 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            int n = sc.nextInt();
            int k = sc.nextInt();

            int total = n;
            int coupon = n;

            while (coupon >= k) {
                int newChicken = coupon / k;
                total += newChicken;
                coupon = coupon % k + newChicken;
            }

            System.out.println(total);
        }

        sc.close();
    }
}
