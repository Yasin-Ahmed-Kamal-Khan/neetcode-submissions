impl Solution {
    pub fn has_cycle(head: *mut ListNode) -> bool {
        let mut slow = head;
        let mut fast = head;

        if fast.is_null() {
            return false;
        }

        loop {
            unsafe {
                if (*fast).next.is_null() {
                    return false;
                }

                if (*(*fast).next).next.is_null() {
                    return false;
                }

                fast = (*(*fast).next).next;
                slow = (*slow).next;

                if fast == slow {
                    return true;
                }
            }
        }
    }
}