class Solution {
public:
    bool isValid(string s) {
      stack<char> charStack;
      for(char charC : s) {
        if(charC == '(') {
          charStack.push(')');
        }else if(charC == '[') {
          charStack.push(']');
        }else if(charC == '{') {
          charStack.push('}');
        }else {
          if(charStack.empty() || charStack.top() != charC) {
            return false;
          }
          charStack.pop();
        }
      }
      return charStack.empty();
    }
};