package _031_next_permutation

//https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
//如何得到这样的排列顺序？
// 第一是从后向前，确保发生改动的数位尽量小，因为越往后的数位代表的数越小
// 其次是第一个相邻升序，重点是第一个升序。如果之前一直是降序，遇到了一个更小的数字，便肯定与上一个数字组成了我们首次遇到的升序对，满足升序条件。
// 那么两数交换后，升序就能保证了更大的数字被交换到了更大的数位上，得到的数字也就必然更大。同时也能够满足第一个与相邻这两个条件
// 这里找到升序对后还不能直接交换，还要有一次寻找增大幅度最小的大数的过程





func nextPermutation(nums []int)  {
    if len(nums) <=1{
        return
    }
    // 此时i ,j 是倒数第二和倒数第一个数
    i, j , k:= len(nums)-2, len(nums)-1, len(nums)-1
    // 从后往前找第一个相邻的升序元素对
    for i>=0 && nums[i]>= nums[j]{
        i--
        j--
    }

    if i>=0 {   // 如果找到了第一个相邻的升序元素对，才进行交换操作
        // 此时i,j 是从后往前找第一个相邻的升序元素对，nums[i]<nums[j], [j,end)是降序，接着在 [j,end) 从后向前查找第一个满足 nums[i] < nums[k] 的 k (为了让增大的幅度最小)
        for k>=j && nums[i]>=nums[k] {
            k--
        }
        // 此时, nums[i] <= nums[j] <= nums[k], 将nums[i]和nums[k]交换, 交换后 [j,end) 必然是降序
        nums[i], nums[k] = nums[k], nums[i]
    }

    // 逆置 [j,end)，使其升序
    for i,j:=j,len(nums)-1;i<j; i,j =i+1, j-1{
        nums[i], nums[j] = nums[j], nums[i]
    }

}