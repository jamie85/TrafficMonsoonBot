from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

passwords = ["password1", "password2"]
driver = webdriver.Firefox()

def WaitForPageLoad(driver):
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

def Login():
    #Open firefox and type in username and password
    print("Logging into TM...")
    driver.get("https://trafficmonsoon.com/login")
    username = driver.find_element_by_name("Username")
    password = driver.find_element_by_name("Password")
    turing = driver.find_element_by_name("turing")
    userUserName = input("Please enter username: ")
    userTuring = input("Please enter turing number: ")
    username.send_keys(userUserName)
    password.send_keys(passwords[0])
    turing.send_keys(userTuring)
    turing.send_keys(Keys.ENTER)
    WaitForPageLoad(driver)
    driver.find_element_by_name("argument").send_keys(passwords[1])
    driver.find_element_by_xpath("//div[@class='col-xs-12']/input[@type='submit']").click()
    WaitForPageLoad(driver)
    #Now we are in wait for the dashboard option and click it, needs 2 clicks
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/p/a/span")))
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/p/a").click()
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/p/a").click()
        print("Clicked through, entering dashboard...")
    except:
        print("Exception on second click!  Ignoring and moving on...")
    WaitForPageLoad(driver)

def StartSurfing():
    print("Starting surfing...")
    WaitForPageLoad(driver)
    driver.find_element_by_xpath("/html/body/nav/div/ul[1]/li[2]/a").click()

def ClickingAlgorithm(usrCycle):
    for click in range(1,usrCycle):
        if click == 1:
            print("Starting clicking algorithm...")
        else:
            print("Clicking algorithm #" + str(click) + "...")
        try:
            WaitForPageLoad(driver)
            wait = WebDriverWait(driver, 25)
            wait.until(EC.invisibility_of_element_located((By.ID, "progress")))
            images = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/img")
            time.sleep(1)
            imageName = []
            for image in images:
                src = image.get_attribute("src")
                #print(src)
                imageName.append(src)
            for i in range(0,5):
                if imageName[i] in imageName[i+1:]:
                    print("Duplicate is: " + str(i+1)) #+ "\nFilename = " + imageName[i])
                    imageXPath = "/html/body/div[1]/div[2]/div[1]/img[" + str(i+1) + "]"
                    driver.find_element_by_xpath(imageXPath).click()
                    break
            wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/a[1]")))
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/a[1]").click()
        except:
            print("ERROR - please check the browser, the TM page did not load correctly. Exiting program...")
    print("Clicks finished, restart if you want more\nGoodbye!")

usrCycle = int(input("WELCOME TO THE TM BOT V1.0!\nPlease enter how many clicks you want to cycle through: "))
Login()
StartSurfing()
ClickingAlgorithm(int(usrCycle+1))