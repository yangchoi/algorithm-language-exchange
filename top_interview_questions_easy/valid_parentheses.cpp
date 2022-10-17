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
          // 괄호 짝이 맞으면 charStack을 비운다.
          charStack.pop();
        }
      }
      // charStack이 비워지면 괄호 짝이 맞는 것이 되므로 true
      return charStack.empty();
    }
};