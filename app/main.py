from fastapi import FastAPI
from app.schemas import chatres,chatreq
from app.agent import is_weather
from app.tools.weather import get_data
from app.tools.search import search_doc
from app.llm import llm_summarize
from app.db import save_chat,create_table

app=FastAPI(title="Mini AI Agent")
create_table()

@app.get("/health")
def check():
    return {'status':'ok'}


@app.post("/chat",response_model=chatres)
def chat(request:chatreq):
    question=request.question.lower()
    if is_weather(question):
        for city in['bengaluru','delhi','mumbai','hyderabad','chennai']:
            if city in question:
                weather=get_data(city)
                if weather:
                    save_chat(request.question,"weather API",
                              (f"Weather in {city.title().lower()}: " 
                                  f"Temperature:{weather['temperature']}, "
                                  f"Humidity:{weather['humidity']}, "
                                  f"Condition:{weather['condition']}"))
                    return chatres(
                        tool_used='Weather API',
                        response=(f"Weather in {city.title().lower()}: " 
                                  f"Temperature:{weather['temperature']}, "
                                  f"Humidity:{weather['humidity']}, "
                                  f"Condition:{weather['condition']}"),
                        context=None)
        return chatres(tool_used="weather Api",
                        response='city not found',
                        context=None)
        
    doc_keywords=['cybersecurity','online', 'learning','product', 'management','security','practices','security practices']
    if any(i in question for i in doc_keywords):    
        docs=search_doc(request.question)
        summary=llm_summarize(request.question,docs)
        if docs :
          save_chat(request.question,"Document search",summary)
          return chatres(
               tool_used='Document Search',
               response=summary,
               context=docs
                )
    
    fallback="Relevant info not found."

    save_chat(request.question,"LLM",fallback)
    
    return chatres(
            tool_used="llm ",
            response="Relevant info not found:",
            context=None
             )


   



