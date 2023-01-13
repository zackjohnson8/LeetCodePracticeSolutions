def solution(pattern: str, s: str) -> bool:
    pattern_list = list(pattern)
    s_list = list(s.split(' '))
    dict_rep = {}

    if len(pattern_list) != len(s_list):
        return False

    for index in range(len(pattern_list)):
        if pattern_list[index] not in dict_rep:
            if s_list[index] in dict_rep.values():
                return False
            dict_rep[pattern_list[index]] = s_list[index]
        else:
            if dict_rep[pattern_list[index]] != s_list[index]:
                return False

    return True
