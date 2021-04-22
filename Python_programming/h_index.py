def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    while answer < len(citations) and answer+1 <= citations[answer]:
        answer += 1

    return answer