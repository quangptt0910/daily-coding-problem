import java.util.HashSet;
import java.util.Scanner;

/*
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
 */
public class Aug20 {
    public static void main(String[] args) {
        solve();
    }
    static void solve() {
        Scanner sc = new Scanner(System.in);
        HashSet<Integer> arrayInput = new HashSet<>();

        int n; // array size/length
        System.out.print("Size of array: ");
        n = sc.nextInt();

        // Array input
        for(int i = 0; i < n; i++)
            arrayInput.add(sc.nextInt());

        // k input
        System.out.print("k: ");
        int k = sc.nextInt();

        // Search for sum
        boolean flg = false;
        for(Integer s : arrayInput){
            if (arrayInput.contains(k - s)){
                flg = true;
                break;
            }
        }
        System.out.println(flg);// result
    }
}
