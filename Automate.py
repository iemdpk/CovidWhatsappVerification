from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time


driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


driver.get("https://web.whatsapp.com/send?phone=918860885065")
time.sleep(10)

driver.get("https://covidtweet.com/")
time.sleep(3)
name = driver.find_element_by_name("search")
time.sleep(2)
name.send_keys("oxygen in noida")
name.send_keys(Keys.RETURN)

time.sleep(3)
main = driver.find_elements_by_class_name('font-medium')


chk1 = []
chk2 = []
for x in range(0,len(main)):
    if(8<int(len(main[x].text)) and int(len(main[x].text))<13):
        chk1.append(main[x].text)
        

for d in range(0,len(chk1)):
    if(chk1[d] == "Get Latest"):
        print()
    elif(chk1[d] == "All Results"):
        print()
    elif(chk1[d] == "Remdesivir"):
        print()
    elif(chk1[d] == "REMDESIVIR"):
        print()
    elif(chk1[d]=="Ventilator"):
        print()

    elif(chk1[d]=="#CovidHelp"):
        print()

    elif(chk1[d] == "Covid Tweet"):
        print()
    elif(chk1[d] == "Powered by"):
        print()
    elif(chk1[d] == "VENTILATOR"):
        print()

    else:
        chk2.append(chk1[d])


print(chk2)


for z in range(0,len(chk2)):

    try:    
        driver.get("https://web.whatsapp.com/send?phone=91"+chk2[z])
        time.sleep(15)


        inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
        input_box = driver.find_element_by_xpath(inp_xpath)
        time.sleep(1)
        input_box.send_keys("Oxygen Available hai Kya Sir" + Keys.ENTER)
        time.sleep(2)
    except:
        print("Not is in work")

print("All Your Message Has been send")
driver.close()
