from collections import Counter
def empirical_pmf(samples):
    result = []
    n = len(samples)
    counts = Counter(samples)
    for key, appears in counts.items():
        probability = appears / n
        initial_res = (key, probability)
        result.append(initial_res)

    return result 

        