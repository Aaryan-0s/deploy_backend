from src.convo.repository.repository import repo

class ConvoService:
    def __init__(self):
        self.repo=repo()

    def get(self,input):
        msg=self.repo.get(input=input)
        return msg
  

    


service=ConvoService