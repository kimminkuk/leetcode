# 생각
 - 와 이거... 오랜만에 tree 구조 나와서 못풀었네????
 - 일단 다른 함수로 빼서, list로 저장해서 비교하려고 했는데...
 - 경우가 다른 부분이 있다고 생각했음 그래서 자체적으로 순회하면서 하려고 했는데
 - 자꾸 틀려서 뭐지 뭐지 하다가 하.. [], []  or  [0], [] 이런 케이스를 깜빡해서 계속 틀리고 에러나고 난리가 났네
 - 반성
<h2><a href="https://leetcode.com/problems/same-tree">100. Same Tree</a></h2><h3>Easy</h3><hr><p>Given the roots of two binary trees <code>p</code> and <code>q</code>, write a function to check if they are the same or not.</p>

<p>Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg" style="width: 622px; height: 182px;" />
<pre>
<strong>Input:</strong> p = [1,2,3], q = [1,2,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg" style="width: 382px; height: 182px;" />
<pre>
<strong>Input:</strong> p = [1,2], q = [1,null,2]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg" style="width: 622px; height: 182px;" />
<pre>
<strong>Input:</strong> p = [1,2,1], q = [1,1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in both trees is in the range <code>[0, 100]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>
