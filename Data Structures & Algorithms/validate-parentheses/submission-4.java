class Solution {
  public boolean isValid(String s) {
    Stack<Character> brackets = new Stack<>();
    Set<Character> opening = new HashSet<>(Arrays.asList('(', '{', '[')); 
    Set<Character> closing = new HashSet<>(Arrays.asList(')', '}', ']')); 

    for (char c : s.toCharArray()) {
      if (opening.contains(c)) 
        brackets.push(c);

      else if (closing.contains(c)) {
        if (brackets.size() == 0)
          return false;

        else if (c == ')') {
          if (brackets.pop() != '(')
            return false;
        }

        else if (c == ']') {
          if (brackets.pop() != '[')
            return false;
        }

        else if (c == '}') {
          if (brackets.pop() != '{')
            return false;
        }
      }
    }

  return brackets.size() == 0;
  }
}