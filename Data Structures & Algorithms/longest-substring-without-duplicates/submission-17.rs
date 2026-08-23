impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut left = 0;
        let mut longest = 0;
        let mut dict: HashMap<char, usize> = HashMap::new();

        let chars: Vec<char> = s.chars().collect();

        for i in 0..s.len() {
            if dict.contains_key(&chars[i]) {
                let temp = dict[&chars[i]];
                left = max(left, temp + 1);
            }
            dict.insert(chars[i], i);

            longest = max(longest, i - left + 1)
        }

        return longest as i32;
    }
}