/*
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
 */


import java.util.Arrays;
import java.util.Comparator;

class Pair {
    int x;
    int y;

    // Constructor
    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "(" + x +
                ", " + y +
                ')';
    }


}

public class NumOfClassRoom {
    public static void Solve(Pair[] arr){
        Comparator<Pair> cmp = Comparator.comparingInt((Pair o) -> o.x)
                .thenComparingInt(o -> o.y);
        Arrays.sort(arr, cmp);
        System.out.println(Arrays.toString(arr));

        int room = 1;
        int start_time = arr[0].x;
        int end_time = Arrays.stream(arr)
                .mapToInt(pair -> pair.y)
                .max()
                .orElse(Integer.MIN_VALUE);

//        System.out.println("Start time: " + start_time);
//        System.out.println("End time: " + end_time);

        int[] timeLine = new int[end_time + 2];
        for(int i = 0; i < arr.length; i++) {
            timeLine[arr[i].x]++;
            timeLine[arr[i].y + 1]--;
        }

        for (int i = 1; i < timeLine.length; i++) {
            timeLine[i] += timeLine[i-1];
            room = Math.max(room, timeLine[i]);
        }
        System.out.println(room);
    }
    public static void main(String[] args) {
        Pair[] arr = new Pair[] {
                new Pair(4, 8),
                new Pair(1, 2),
                new Pair(0, 3),
                new Pair(4, 6),
                new Pair(6, 9),

        };

        Pair[] arr1 = new Pair[] {
                new Pair(30, 75),
                new Pair(0, 50),
                new Pair(60, 150),

        };
        Solve(arr);
        Solve(arr1);
    }
}
