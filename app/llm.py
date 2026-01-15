def llm_summarize(question:str,docs:list[str])->str:
    question_lower = question.lower()

    for doc in docs:
        doc_lower = doc.lower()

        for word in question_lower.split():
            if word in doc_lower:
                start_index = doc_lower.find(word)
                snippet = doc[start_index:start_index + 400]
                return f"Summary :  {snippet}"
    
    combined = " ".join(docs)
    return f"Summary: {combined[:300]}"