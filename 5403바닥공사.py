if __name__ == "__main__":
  N = int(input())
  dp = [0]*(N+1) # 테이블 초기화
  dp[0] = 1 # seed값 -> 0에 1을 준 이유는 0에서도 경우의 수가 발생해서 곱하기를 이용해서 편하게 처리하기 위함이다.
  for i in range(2, N+1):
      dp[i] = dp[i-2]*3 # 3x2 격자에 들어가는 경우가 3개 라서 그만큼 곱해준다.
      if i-4 >= 0 and i % 2 == 0:
          for j in range(i-4, -1, -2): # 0까지 짝수를 줄여가면서 해당 경우의 수와 발생가능한 경우의 수인 2를 곱해준다.
              dp[i] += dp[j]*2
  print(dp[N])
  

n = int(input())
if n == 1  :
    print(0)
else :
    dp = [0]*(n+1)
    dp[2] = 3
    for i in range(4,n+1) :
        if i%2 == 1 :
            dp[i] = 0
        else :
            dp[i] = dp[i-2]*3 + sum(dp[:i-2])*2 + 2
    print(dp[n])
