/* 删除元素 */

/* 删除索引 index 处的元素 */
// 注意：stdio.h 占用了 remove 关键词
void removeItem(int *nums, int size, int index) {
    // 把索引 index 之后的所有元素向前移动一位
    for (int i = index; i < size - 1; i++) {
        nums[i] = nums[i + 1];
    }
}