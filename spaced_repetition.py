from datetime import datetime, timedelta

def next_review(last_review_date, score):
    days_gap = 1

    if score > 0.8:
        days_gap = 5
    elif score > 0.6:
        days_gap = 3
    else:
        days_gap = 1

    return last_review_date + timedelta(days=days_gap)
