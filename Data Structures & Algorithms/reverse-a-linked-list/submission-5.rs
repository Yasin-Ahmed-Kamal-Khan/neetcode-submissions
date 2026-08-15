// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match head {
            None => return head,
            Some(mut node) => {
                let mut current_box = node.next.take();
                let mut last = Some(node);

                while let Some(mut current) = current_box {
                    let next_node = current.next.take();
                    current.next = last;
                    last = Some(current);
                    current_box = next_node;
                }

                return last;
            }
        }
    }
}
