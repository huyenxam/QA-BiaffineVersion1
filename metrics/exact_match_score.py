from metrics.normalize_answer import normalize_answer, chuan_hoa_dau_cau_tieng_viet

def exact_match_score(prediction, ground_truth):
    '''
    Returns exact_match_score of two strings.
    '''
    prediction_tokens = normalize_answer(chuan_hoa_dau_cau_tieng_viet(prediction.replace("_", " ")))
    ground_truth_tokens = normalize_answer(chuan_hoa_dau_cau_tieng_viet(ground_truth))

    return (prediction_tokens == ground_truth_tokens)
