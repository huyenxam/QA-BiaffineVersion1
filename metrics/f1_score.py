from metrics.normalize_answer import normalize_answer, chuan_hoa_dau_cau_tieng_viet
from collections import Counter

def f1_score(prediction, ground_truth):
    '''
    Returns f1 score of two strings.
    '''

    prediction_tokens = normalize_answer(chuan_hoa_dau_cau_tieng_viet(prediction.replace("_", " "))).split(" ")
    ground_truth_tokens = normalize_answer(chuan_hoa_dau_cau_tieng_viet(ground_truth)).split(" ")

    common = Counter(prediction_tokens) & Counter(ground_truth_tokens)
    num_same = sum(common.values())
    if num_same == 0:
        return 0
    precision = 1.0 * num_same / len(prediction_tokens)
    recall = 1.0 * num_same / len(ground_truth_tokens)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1