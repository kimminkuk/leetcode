# 생각
 - 아 요즘 왜케 못 풀지..?? DP, TWO-POINTER 처럼 보이는거 나오면 하나도 못 푸네...
 - 일단 그 구현이 너무 어려움, 잘 안돼
 - 오늘거는 할 수 있었다고 생각 했는데, dict안에 값을 넣어 두고 right left를 구현할 엄두가 안남
 - 근데 또 솔루션 보니 쉽네 하.. 뭘 놓친거지.... left 부분의 값을 이동하면서 dict를 수정하는 부분 생각 못했고
 - right 이동 하면서, dict의 value 값으로 k를 구하는 방식을 생각 못함
 - 
<h2><a href="https://leetcode.com/problems/count-the-number-of-good-subarrays">2626. Count the Number of Good Subarrays</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the number of <strong>good</strong> subarrays of</em> <code>nums</code>.</p>

<p>A subarray <code>arr</code> is <strong>good</strong> if there are <strong>at least </strong><code>k</code> pairs of indices <code>(i, j)</code> such that <code>i &lt; j</code> and <code>arr[i] == arr[j]</code>.</p>

<p>A <strong>subarray</strong> is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], k = 10
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only good subarray is the array nums itself.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,4,3,2,2,4], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 10<sup>9</sup></code></li>
</ul>
