# 22:51 
# 
# 문제)
# N 개의 스위치 , N개 전구
# 
# _ _ _ _ _ _ _ _ 
# _ _ _ _ _ _ _ _
# 
#
#
# 입출력) 
# N의 길이 = 10만
#
#
#
# 풀이법) 
# i) 모든것은 양옆을 반대로 만들지만, 맨 왼쪽 -> 오른쪽은 그렇지 않다 
# ii) <- 있는게 이미 만족을 하는데 내꺼는 바꿔줘야한다면.. 다음 전등에 가서 눌러줘야한다
# 
# iii) 1이 아닌곳을 먼저 전부 1로 만들어줘야한다.. 그래야지 치지 않을떄.. 
#
#
# 예시)
# 000 -> 110 -> 101 -> 010
#
#
# 
# 00000000000
# 00000101100
# 
# 00001000000 
# 00001001011
# 00000111011
#
# 00000101100
# 00 -> 
#  000
#   000 -> 
#    000
#     010 유
#      000 유
#       010 유
#        010 유
#         000 
#







