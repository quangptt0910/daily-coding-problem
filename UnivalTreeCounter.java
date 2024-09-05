/*
August 27th 2024
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 */
public class UnivalTreeCounter {
    public static void main(String[] args) {
        // Example tree
        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.right = new TreeNode(0);
        root.right.left = new TreeNode(1);
        root.right.right = new TreeNode(0);
        root.right.left.left = new TreeNode(1);
        root.right.left.right = new TreeNode(1);

        UnivalTreeCounter counter = new UnivalTreeCounter();
        System.out.println("Number of unival (sub)trees: " +counter.UnivalTreeCount(root) );
    }

    private int UnivalTreeCount(TreeNode root) {
        if (root == null) {
            return 0; // Empty tree, no unival subtrees
        }
        int[] cnt = {0};
        isUnival(root, cnt);
        return cnt[0];
    }
    private boolean isUnival(TreeNode node, int[] cnt) {
        if (node == null) {
            return true;
        }

        boolean leftUnival = isUnival(node.left, cnt);
        boolean rightUnival = isUnival(node.right, cnt);

        // check if current node is unival
        if (leftUnival && rightUnival) {
            if (node.left != null && node.left.val != node.val ) {
                return false;
            }
            if (node.right != null && node.right.val != node.val ) {
                return false;
            }
            cnt[0]++;
            return true;
        }
        return false;
    }
}

class TreeNode {
    TreeNode left;
    TreeNode right;
    int val;
    TreeNode(int val) {
        this.val = val;
    }
}

