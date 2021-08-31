# [剑指 Offer 09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)


用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例1:
```
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

```

示例2:
```
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

```

说明：
["CQueue","appendTail","deleteHead","deleteHead"] 
这一行表示每一行代码的操作

[[],[3],[],[]]
这个表示每一行代码操作所需要的参数

举例：
CQueue 表示新建一个CQueue对象，对应的所需参数为[]，即此操作不需要参数。
appendTail 表示执行一个appendTail()操作，对应要被操作的元素为3。
deleteHead 表示执行一个deleteHead操作，对应的所需参数为[]，即此操作不需要参数。
deleteHead 表示执行一个deleteHead操作，对应的所需参数为[]，即此操作不需要参数。

以上的输入其实是一个代码执行的步骤描述与其对应所需参数。

即两个纬度：
1、操作描述
2、此次操作所需参数
3、操作描述与操作所需参数是通过默认顺序一一对应的。

null就是返回空或者不返回值，-1是想删除元素时已经空了就返回-1

提示：

- 1 <= values <= 10000
- 最多会对 appendTail、deleteHead 进行 10000 次调用