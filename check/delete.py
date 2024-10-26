import os,string,random,re,sys,urllib,time
from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures

def generate_random_string():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(10))
def wait_and_click(driver, css_selector):
    try:
        element = WebDriverWait(driver, 20).until(  # Menunggu elemen sampai muncul (default 10 detik)
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()  # Klik elemen setelah valid
    except TimeoutException:
        print("Element tidak ditemukan atau tidak bisa diklik.")

def wait_and_send(driver, css_selector, action):
    try:
        element = WebDriverWait(driver, 20).until(  # Menunggu elemen sampai muncul (default 10 detik)
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.send_keys(action)  # Kirim input setelah valid
    except TimeoutException:
        print("Element tidak ditemukan atau tidak bisa di send.")
def login(email,password,sec_code):
    max_retries = 5
    attempt = 0
    
    while attempt <= max_retries:
        driver.get('https://myaccount.google.com/security')
        print("Login Email...")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div > c-wiz > c-wiz > div > div.s7iwrf.gMPiLc.Kdcijb > div > div > c-wiz > section > div > div > div > div > div > div > header > div.m6CL9 > div'))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'identifier'))).send_keys(email)
        print("Email : "+email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#identifierNext > div > button'))).click()
        time.sleep(2)
        try:
            WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'))).send_keys(password)
            print("Password : "+password+"\n===================================")
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordNext > div > button'))).click()
            print("Retive OTP Auth...")
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get('https://totp.danhersam.com/#/'+sec_code)
            otp_auth = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#token'))).text
            print("OTP Auth : "+otp_auth)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            print("Submit OTP Auth...")
            wait_and_send(driver, '#totpPin', otp_auth)
            time.sleep(1)
            wait_and_click(driver, '#totpNext > div > button')
            time.sleep(2)
            return True
        except:
            print("Captcha Require, Next Email...\n======================================")
            attempt += 1
            if attempt > max_retries:
                print("Max login attempts reached. Moving to the next email.")
                return False
def loqout():
    driver.get('https://accounts.google.com/SignOutOptions?hl=en&continue=https://myaccount.google.com/security&ec=GBRAwAE')
    time.sleep(2)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#signout'))).click()

def family():
    driver.get("https://myaccount.google.com/family/details?hl=en_US")
    for i in range(3,8):
        href_links.append(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > c-wiz > div > div.s7iwrf.gMPiLc > div > div > c-wiz > section > div:nth-child(1) > div > div > div:nth-child({str(i)}) > div.VfPpkd-ksKsZd-XxIAqe.CmhoVd.I6g62c > a'))).get_attribute('href').split('/g/')[-1])
    print(href_links)
    for i in range(len(href_links)):
        driver.get(f"https://familylink.google.com/member/{str(href_links[i])}/delete")
        time.sleep(9)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
        time.sleep(1)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(0.3)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.3)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(0.3)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.3)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(0.3)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.3)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(5)


with open('result_ortu.txt', 'r') as file:
    emails = file.readlines()

failed_logins = []


while emails:
    href_links = []
    mail_list = []
    email = emails[0].replace('\n', '')
    
    if not email:
        break
    
    if email in failed_logins:
        emails.pop(0)
        continue
    
    bacot = re.split(r'[|:;]', email.strip())

    driver = Driver(uc=True)
    
    if login(bacot[0], bacot[1], bacot[2]):
        time.sleep(1)
        family()
        with open('result_ortu_delete.txt', 'a') as result_file:
            result_file.write(f"{bacot[0]}|{bacot[1]}|{bacot[2]}\n")
        time.sleep(2)
        loqout()
        time.sleep(2)
        
        emails.pop(0)
        
        with open('result_ortu.txt', 'w') as file:
            file.writelines(emails)
    else:
        failed_logins.append(email)
    driver.quit()


print("Done All")

# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     executor.map(main, [urls] * 5)