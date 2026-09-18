def predict_result(study_hours, attendance):

    score = (
        study_hours * 5
        + attendance * 0.5
    )

    if score >= 65:
        return "PASS"

    return "FAIL"