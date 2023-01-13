import solutions.easy.wordpattern as word_pattern

def test_different_lengh_variables_return_false():
    assert word_pattern.solution("abbaa", "dog dog dog dog") == False
    assert word_pattern.solution("abba", "dog dog dog dog dog") == False

def test_valid_case():
    assert word_pattern.solution("abba", "dog cat cat dog") == True


def test_invalid_case():
    assert word_pattern.solution("abba", "dog cat cat fish") == False
    assert word_pattern.solution("aaaa", "dog cat cat dog") == False
