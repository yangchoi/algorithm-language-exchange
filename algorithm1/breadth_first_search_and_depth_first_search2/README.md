### 617. Merge Two Binary Trees
root1, root2 두개의 이진수 트리를 가진다. <br>
이들 중 하나를 다른 것으로 덮는 것을 상상해보라. <br>
두 트리 중 어느 노드들은 겹치게 될 것이다.<br>
두 트리를 새 이진 트리로 merge 하라. <br>
그리고 두개의 노드가 오버랩되면 merge된 노드의 새 값은 노드들의 값들을 더하여 채워넣는다. <br>
그렇지 않으면 새 트리에 노드로서 null 노드가 리턴된다.


### 116. 각 노드의 다음 오른쪽 
모든 리프들이 똑같은 레벨에 똑같은 두개의 자식을 가진 부모인 완벽한 이진수 트리가 주어진다. <br> 
이진 트리는 아래와 같이 정의된다. <br>

```typescript
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
(이 문제는 유보)
