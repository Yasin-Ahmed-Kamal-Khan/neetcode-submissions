class Solution:
  def isValid(self, s: str) -> bool:
    brackets = []
    
    for i in s:
      if i == '(':
        brackets.append('(')
        
      elif i == '[':
        brackets.append('[')
        
      elif i == '{':
        brackets.append('{')
      
      elif i in (')', ']', '}'):
        
        if len(brackets) == 0:
          return False
        
        elif i == ')':
          if brackets.pop() != '(':
            return False
          
        elif i == ']':
          if brackets.pop() != '[':
            return False
          
        elif i == '}':
          if brackets.pop() != '{':
            return False
        
    return len(brackets) == 0