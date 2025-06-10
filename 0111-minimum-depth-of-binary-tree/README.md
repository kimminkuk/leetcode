# 생각
 - level을 1씩 증가 시키고, child가 없을 때만 min 값 갱신. 그런데 속도가 많이 느리네..?
 - BFS로도 풀어보기 queue 사용해서 한층씩 내리면서, child 없는 node에서 level 취득하면 될듯?
<h2><a href="https://leetcode.com/problems/minimum-depth-of-binary-tree">111. Minimum Depth of Binary Tree</a></h2><h3>Easy</h3><hr><p>Given a binary tree, find its minimum depth.</p>

<p>The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg" style="width: 432px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [2,null,3,null,4,null,5,null,6]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>5</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>
