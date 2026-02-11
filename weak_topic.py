def detect_weak_topics(results):
    weak = []
    for topic, score in results.items():
        if score < 0.6:
            weak.append(topic)
    return weak
