# Problem Statement: https://www.hackerrank.com/challenges/gem-stones
T = int(input())
rocks = (raw_input().strip()for _ in range(T))
element_sets = [set(rock) for rock in rocks]
gem_elements = set.intersection(*element_sets)
print len(gem_elements)
