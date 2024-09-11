import java.util.Arrays;
import java.util.stream.IntStream;

/*
Given an array of integers, return a new array such that each element at index i of
the new array is the product of all the numbers in the original array except the one
at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120,
60, 40, 30, 24]. If our input was [3, 2, 1],the expected output would be [2,
3, 6].
Follow-up: What if you can't use division?
 */
public class ProductOfAllOtherElements {

    //with division
    public static int[] solve_withDivision(int[] array) {
        int product = IntStream.of(array)
                .reduce(1, (a, b) -> a * b);
        int[] result = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            result[i] = product / array[i];
        }
        return result;
    }

    // without division
    // we calculate the prefix and suffix product
    public static int[] solve_noDivision(int[] array) {
        int[] prefix_product = new int[array.length];
        int[] suffix_product = new int[array.length];
        int[] result = new int[array.length];

        // generate prefix product
        prefix_product[0] = array[0];
        for (int i = 1; i < array.length; i++) {
            prefix_product[i] = prefix_product[i - 1] * array[i];
        }

        // generate suffix product
        suffix_product[array.length - 1] = array[array.length - 1];
        for(int i = array.length - 2; i >= 0; i--) {
            suffix_product[i] = suffix_product[i + 1] * array[i];
        }

        // generate result
        for(int i = 0; i < array.length; i++) {
            if( i == 0) result[i] = suffix_product[i+1];
            else if (i == array.length - 1) result[i] = prefix_product[i-1];
            else result[i] = prefix_product[i-1] * suffix_product[i+1];
        }
        return result;
    }

    public static void main(String[] args) {
        int[] array0 = {1, 2, 5, 4, 3};
        int[] array1 = {3, 2, 1};

        System.out.println(Arrays.toString(solve_withDivision(array0)));
        System.out.println(Arrays.toString(solve_noDivision(array0)));

        System.out.println(Arrays.toString(solve_withDivision(array1)));
        System.out.println(Arrays.toString(solve_noDivision(array1)));
    }
}
