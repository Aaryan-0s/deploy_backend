
import re
from bs4 import BeautifulSoup
from selenium import webdriver


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy.orm import Session
from src.share.repository.share_repository import ShareRepo
from src.entrypoint.database import get_db



driver = webdriver.Firefox()

URL="https://www.nepalipaisa.com/live-market"

def save_data_to_sql(data):
    db:Session=get_db()
    for row in data:
        company_data = ShareRepo(
            Company=row['Company'],
            LTP=row['LTP'],
            CHG=row['CHG'],
            CHG_percent=row['%CHG'],
            HIGH=row['HIGH'],
            LOW=row['LOW'],
            Open=row['OPEN'],
            Quantity=row['Quantity'],
            txn=row['txn']
        )
        db.add(company_data)
    db.commit()



def get_data()->dict[any]:
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tr.bg-negative-lv-1')))

    soap=BeautifulSoup(driver.page_source,'html.parser')
    

    list=soap.find_all('tr',attrs={'class':re.compile('bg-')},limit=20)
    
    data=[]
    row={}

    for (index,company) in enumerate(list):
        row={"id":index+1,"Company":None,"LTP":None,"CHG":None,"%CHG":None,"VOL":None,"HIGH":None,"LOW":None,"OPEN":None,"Quantity":None,"txn":""} 
        
        for (i,td) in enumerate(company.find_all('td')):
            if i==0:
                row['Company']=td.text
            if i==1:
                row['LTP']=td.text
            if i==2:
                row['CHG']=td.text
            if i==3:
                row['%CHG']=td.text
            
            if i==4:
                row['HIGH']=td.text
            if i==5:
                row['LOW']=td.text
            if i==6:
                row['OPEN']=td.text
            if i==7:
                row['Quantity']=td.text
            if i==8:
                row['txn']=td.text
            
        data.append(row)
            
    driver.close() 
       
          
       
    
    return data  
   

        
def main():
    data = get_data()
    save_data_to_sql(data)
    print("Data saved to MySQL successfully!")


if __name__ == "__main__":
    main()
