import java.util.ArrayList;
import java.util.List;

/*
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. 'i' is guaranteed to be smaller than or equal to N.
 */
public class OrderLog {
    private int n;
    List<String> logList = new ArrayList<>();

    public OrderLog(int n) {
        this.n = n;
    }

    // add order_id
    public void record(String order_id) {
        logList.add(order_id);
    }

    // get the ith last element
    public String get_last(int i) {
        int index = logList.size() - i;
        return logList.get(index);
    }

    // get the list of last ith elements
    public List<String> get_last_list(int i) {
        int len = logList.size();
        return logList.subList(Math.max(len - i, 0), len);
    }

    public static void main(String[] args) {
        OrderLog orderLog = new OrderLog(5);

        orderLog.record("1a");
        orderLog.record("2b");
        orderLog.record("3c");
        orderLog.record("4d");
        orderLog.record("5e");

        System.out.println(orderLog.get_last(2)); // should return 4d
        System.out.println(orderLog.get_last_list(3)); // should return 3c, 4d, 5e
    }

}


