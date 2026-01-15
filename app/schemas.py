from pydantic import BaseModel
from typing import List,Optional
class chatreq(BaseModel):
    question:str

class chatres(BaseModel):
    tool_used:str
    response:str
    context:Optional[List[str]]=None
