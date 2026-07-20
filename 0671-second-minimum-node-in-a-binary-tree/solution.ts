/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function findSecondMinimumValue(root: TreeNode | null): number {
    if(!root) return -1;
    const minVal = root.val;
    let secondMin = Infinity;

    function dfs(node: TreeNode | null): void{
        if(!node) return;

        if (node.val > minVal && node.val < secondMin){
            secondMin = node.val;
            return;
        }

        if(node.val === minVal){
            dfs(node.left);
            dfs(node.right);
        }
    }
    dfs(root);

    return secondMin === Infinity ? -1 : secondMin;
};
