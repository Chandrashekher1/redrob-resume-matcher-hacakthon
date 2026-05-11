import math


def computecosinesimilarity(vector1, vector2):
    if isinstance(vector1, dict) and isinstance(vector2, dict):
        dot_product = sum(vector1.get(skill, 0.0) * vector2.get(skill, 0.0) for skill in vector1)
        magnitude1 = math.sqrt(sum(value * value for value in vector1.values()))
        magnitude2 = math.sqrt(sum(value * value for value in vector2.values()))
        return dot_product / (magnitude1 * magnitude2) if magnitude1 and magnitude2 else 0.0

    if isinstance(vector1, list) and isinstance(vector2, list):
        dot_product = sum(a * b for a, b in zip(vector1, vector2))
        magnitude1 = math.sqrt(sum(a * a for a in vector1))
        magnitude2 = math.sqrt(sum(b * b for b in vector2))
        return dot_product / (magnitude1 * magnitude2) if magnitude1 and magnitude2 else 0.0

    return 0.0