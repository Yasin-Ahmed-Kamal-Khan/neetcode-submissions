class MinStack {
  private ArrayList<Integer> mainStack;
  private ArrayList<Integer> minStack;

  public MinStack() {
    this.minStack = new ArrayList<>();
    this.mainStack = new ArrayList<>();
  }
  
  public void push(int val) {
    
    mainStack.add(val);

    if (minStack.size() == 0) {
      minStack.add(val);
    } else if (minStack.get(minStack.size() - 1) < val) {
      minStack.add(minStack.get(minStack.size() - 1));
    } else {
      minStack.add(val);
    }
  }
  
  public void pop() {
    mainStack.remove(mainStack.size() - 1);
    minStack.remove(minStack.size() - 1);
  }
  
  public int top() {
    return mainStack.get(mainStack.size() - 1);
  }
  
  public int getMin() {
    return minStack.get(mainStack.size() - 1);
  }
}
