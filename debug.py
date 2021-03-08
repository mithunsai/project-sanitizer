from collections import Counter
counter_dict = Counter()

counter_dict['1'] = 23
counter_dict['2'] = 40
counter_dict['3'] = 15
counter_dict['4'] = 70
print(counter_dict.most_common(2))
