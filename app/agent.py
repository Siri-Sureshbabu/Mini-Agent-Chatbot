keywords=['weather','condition','temperature','forcast','humidity']
def is_weather(question: str)->bool:
    question=question.lower()
    return any(keyword in question for keyword in keywords)