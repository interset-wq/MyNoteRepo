"""
链表的组成单位是节点（node）对象。
每个节点都包含两项数据：
节点的“值”和指向下一节点的“引用”。

链表的首个节点被称为“头节点”，最后一个节点被称为“尾节点”。

尾节点指向的是“空”，
它在 Java、C++ 和 Python 中分别被记为 null、nullptr 和 None 。
在 C、C++、Go 和 Rust 等支持指针的语言中，
上述“引用”应被替换为“指针”。

在相同数据量下，链表比数组占用更多的内存空间。
"""


class ListNode:
    """链表节点类"""

    def __init__(self, val: int):
        self.val: int = val  # 节点值
        self.next: ListNode | None = None  # 后继节点引用


def list_to_linked_list(arr: list[int]) -> ListNode | None:
    """将列表反序列化为链表"""
    dum = head = ListNode(0)
    for a in arr:
        node = ListNode(a)
        head.next = node
        head = head.next
    return dum.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    """将链表序列化为列表"""
    arr: list[int] = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
