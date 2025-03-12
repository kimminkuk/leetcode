# 생각
 - 아..에라스토테네스체으로 프라임 넘버 데이터 만들어내고, 바로 대입하면 O(n2) 가 발생하는것은 확인
 - 그래서... left <-> right 를 조사하는것을 어떻게 for (i...) 를 사용안하고 찾아낼까 고민함
 - 하지만....생각처럼 잘 되지 않았음. 일단 실패한 계기는 예측으로 해볼려고 했음
 - 예를 들어, left가 1, right가 1000000이면 left다음으로 예측가능한 right는 left+1이니깐
 - for (left~right)로 에라스토 값을 계속 구함
 - 좋은 생각이라고 판단했었지만, 소수를 구하기 애매한 값들이 나오면 시간 over가 발생함
 - 결론적으로 In-Memory였나?? 메모이제이션(memoization)으로 판단했으면 쉽게 O(n2) 타임 over를 피할 수 있었음 아....

<h2><a href="https://leetcode.com/problems/closest-prime-numbers-in-range">2610. Closest Prime Numbers in Range</a></h2><h3>Medium</h3><hr><p>Given two positive integers <code>left</code> and <code>right</code>, find the two integers <code>num1</code> and <code>num2</code> such that:</p>

<ul>
	<li><code>left &lt;= num1 &lt; num2 &lt;= right </code>.</li>
	<li>Both <code>num1</code> and <code>num2</code> are <span data-keyword="prime-number">prime numbers</span>.</li>
	<li><code>num2 - num1</code> is the <strong>minimum</strong> amongst all other pairs satisfying the above conditions.</li>
</ul>

<p>Return the positive integer array <code>ans = [num1, num2]</code>. If there are multiple pairs satisfying these conditions, return the one with the <strong>smallest</strong> <code>num1</code> value. If no such numbers exist, return <code>[-1, -1]</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> left = 10, right = 19
<strong>Output:</strong> [11,13]
<strong>Explanation:</strong> The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> left = 4, right = 6
<strong>Output:</strong> [-1,-1]
<strong>Explanation:</strong> There exists only one prime number in the given range, so the conditions cannot be satisfied.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>6</sup></code></li>
</ul>

<p>&nbsp;</p>
<style type="text/css">.spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0; 
}
.spoiler {overflow:hidden;}
.spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;}
.spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-500%;}
.spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}
</style>
