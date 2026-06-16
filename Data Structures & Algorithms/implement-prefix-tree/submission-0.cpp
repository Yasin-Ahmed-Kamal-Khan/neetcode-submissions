
class PrefixTree {
  private:
  class Node {
    public:
        Node* children[26];
        bool isEnd; // optional: marks end of a word

        Node(bool isEnd) {
            this->isEnd = isEnd;
            for (int i = 0; i < 26; i++) {
                children[i] = nullptr;
            }
        }

        Node* insertChar(char c) {
          if (!children[c - 'a']) {
            children[c - 'a'] = new Node(false);
          }

          return children[c - 'a'];
        }

        void setEnd() {
          isEnd = true;
        }

        bool contains(char c) {
          return children[c - 'a'] != nullptr;
        }

        Node* next(char c) {
          return children[c - 'a'];
        }
  };

  public:
    Node* head = new Node(false);

    PrefixTree() {

    }

    void insert(string word) {
      Node* cur = head;
      for (char c : word) {
        cur = cur->insertChar(c);
      }

      cur->setEnd();
    }

    bool search(string word) {
      auto cur = head;
      for (char c : word) {
        if (!cur->contains(c)) return false;

        cur = cur->next(c);
      }

      return cur->isEnd;

    }

    bool startsWith(string prefix) {
      auto cur = head;
      for (char c : prefix) {
        if (!cur->contains(c)) return false;

        cur = cur->next(c);
      }

      return true;
    }
};
