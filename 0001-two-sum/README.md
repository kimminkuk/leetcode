<h2><a href="https://leetcode.com/problems/two-sum">1. Two Sum</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?

# My Thoughts
 - 바로 O(n^n) 생각을 했는데, 조금 아쉬워서 sort O(logn)*n 하고 시작 부분, 끝 부분 더해서 나누는 방법으로 logn 공략으로 시도

## 풀이 과정
1. sort 후, mid 와 target 이 일치하는지 조사 -> O(n*logn) + O(logn)
2. 하지만, sort 후 index 순서를 보장하지 않는다는 사실을 깜빡함
3. 이중 list를 생성해서, sorted(nums, key=lambda x:x[0])으로 이중 list의 첫 번째 인자를 보고 sort 하기로 생각 (index 순서 보장)
4. mid와 target 일치시킨 후, index return 

## 어려웠던 점
1. sorted(nums, key=lambda) 생각이 안났음

## 참고한 점 

## 개선할 점
1. key=lambda를 대충 알고 쓰는데, 한번 다시 관련 문서를 읽어봐야함
   
## 추가 팁
