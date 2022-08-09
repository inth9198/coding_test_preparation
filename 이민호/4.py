# function solution(people, limit) //사람은 2명밖에 탑승할 수 없다는 중요한 조건이 필요합니다.
# {
#     var answer = 0;
#     people.sort((a,b) => a - b);
#     console.log(people);
#     let head = 0;
#     let tail = people.length - 1;
#     while (tail > head)
#     {
#         if (people[head] + people[tail] <= limit)
#         head++;
#         tail--;
#         answer++;
#         if (tail == head)
#             answer++;
#     }
#
#     return answer;
# }
# const r = solution([70, 50, 80, 50], 100);
# console.log(r);
