

from src.entrypoint.database import intents

class InMemoryRep:
    def get(self,input):
        for intent in intents["conversations"]:
            
            if input.lower() in intent["input"].lower():
                return intent["response"]
        return None  # Return None if no match is found
    
   

repo=InMemoryRep