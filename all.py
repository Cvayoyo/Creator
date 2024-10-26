# from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from seleniumbase import Driver
import time, random, requests, csv, string, json, re, sys,os
from faker import Faker
from datetime import datetime
from fake_useragent import UserAgent
from smsactivate.api import SMSActivateAPI
with open('data/api.txt', 'r') as file:
    lines = file.readlines()
choser = int(1)
fake = Faker()
iphone_user_agents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.8 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.7 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.7 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.3 Mobile/14E277 Safari/602.1.50",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.2 Mobile/14E277 Safari/602.1.50",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.1 Mobile/14E277 Safari/602.1.50",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14E277 Safari/602.1.50",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.3 Mobile/13E233 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.2 Mobile/13E233 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.1 Mobile/13E233 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13E233 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.4 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.3 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.2 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.1 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.1 Mobile/11D201 Safari/537.51.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/537.51.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/6.1 Mobile/10B141 Safari/537.51.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/6.0 Mobile/10A5354d Safari/537.51.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/9537.53.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.0 Mobile/9A334 Safari/9537.53.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 4_3 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8F190 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 4_2 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8C148 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 4_1 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 4_0 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 3_2 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/7D11 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 3_1 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/7D11 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 3_0 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/7A341 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 2_2 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/2.2.1 Mobile/5F137 Safari/528.16",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 2_1 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/2.1.1 Mobile/5F137 Safari/528.16",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 2_0 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/2.0.1 Mobile/5A347 Safari/528.16",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 1_1 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/1.1.1 Mobile/5B150 Safari/528.16",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 1_0 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/1.0.1 Mobile/5A290 Safari/528.16",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.8 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.7 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.7 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.3 Mobile/14E277 Safari/602.1.50",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.2 Mobile/14E277 Safari/602.1.50",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.1 Mobile/14E277 Safari/602.1.50",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14E277 Safari/602.1.50",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.3 Mobile/13E233 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.2 Mobile/13E233 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.1 Mobile/13E233 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13E233 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.4 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.3 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.2 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.1 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/601.1.46",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.1 Mobile/11D201 Safari/537.51.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/537.51.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/6.1 Mobile/10B141 Safari/537.51.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/6.0 Mobile/10A5354d Safari/537.51.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/9537.53.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.0 Mobile/9A334 Safari/9537.53.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 4_3 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8F190 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 4_2 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8C148 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 4_1 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 4_0 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 3_2 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/7D11 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 3_1 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/7D11 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 3_0 like Mac OS X) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/7A341 Safari/531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 2_2 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/2.2.1 Mobile/5F137 Safari/528.16",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 2_1 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/2.1.1 Mobile/5F137 Safari/528.16",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 2_0 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/2.0.1 Mobile/5A347 Safari/528.16",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 1_1 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/1.1.1 Mobile/5B150 Safari/528.16",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 1_0 like Mac OS X) AppleWebKit/528.16 (KHTML, like Gecko) Version/1.0.1 Mobile/5A290 Safari/528.16",
]
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
        time.sleep(1)
        try:
            WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'))).send_keys(password)
            print("Password : "+password+"\n===================================")
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordNext > div > button'))).click()
            return True
        except:
            print("Captcha Require, Next Email...\n======================================")
            attempt += 1
            if attempt > max_retries:
                print("Max login attempts reached. Moving to the next email.")
                return False

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

def change_status(status_id, order_idst):
    if providers == 0:
        while True:
            response = requests.get(f'https://siotp.com/api/changestatus?apikey={api}&id={order_idst}&status={status_id}', timeout=20)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return True
                else:
                    print("Response status is not 'success'.")
            else:
                print(f"Failed to get data. Status code: {response.status_code}")
    elif providers == 1:
        while True:
            response = requests.get(f'https://tokoclaude.com/api/resend-order/ddbbf23ae4791048e8d82f42af3ad3a5/{order_idst}', timeout=20)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    print(data)
                    return True
                else:
                    print("Response status is not 'success'.")
            else:
                print(f"Failed to get data. Status code: {response.status_code}")
    elif providers == 2:
        while True:
            url = 'https://wnrstore.com/api/v1/transaction/resend'
            headers = {
                'Authorization': f'Bearer {order_idst}'
            }
            params = {
                "id": status_id
            }
            response = requests.post(url, headers=headers, json=params)
            response_data = response.json()
            return True
    elif providers == 4:
        while True:
            x = requests.get(f"https://smshub.org/stubs/handler_api.php?api_key={api}&action=setStatus&status=3&id={order_idst}")
            if x.status_code == 200:
                print(x.text)
                return True

def get_phone(tokens, layanans):
    if providers == 1:
        for i in range(100):
            response = requests.get(f'https://tokoclaude.com/api/set-orders/{api}/977', timeout=20)
            if response.status_code == 201:
                data = response.json()
                if data.get('success') == True:
                    order_ids = data['data']['data'].get('order_id')
                    numbers = data['data']['data'].get('number')
                    if numbers.startswith("0"):
                        number = f"62{numbers[1:]}"
                    return order_ids, number
                else:
                    print(data)
            time.sleep(2)
        print("Change Your Provider / Layanan -_-")
        sys.exit()
    elif providers == 0:
        for i in range(100):
            response = requests.get(f'https://api.siotp.com/api/order?apikey={api}&service=2&operator={layanans}&country=1', timeout=20)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    order_ids = data.get('id')
                    numbers = data.get('number')
                    return order_ids, numbers
                else:
                    print("Response status is not 'success'.")
            else:
                print(f"Failed to get data. Status code: {response.status_code}")
            time.sleep(2)
        print("Change Your Provider / Layanan -_-")
        sys.exit()
    elif providers == 2:
        for i in range(100):
            url = 'https://wnrstore.com/api/v1/transaction/add'
            headers = {
                'Authorization': f'Bearer {tokens}'
            }
            data = {
                "product_id": "price-20240213-1707820313093-8a7d99c0-4056-4323-859c-4d7fd28847ab",
                "product_country": "country-20230731-1690755002291-6278abd1-c5af-4947-9150-14eeb0f2eba4",
                "product_operator": layanans,
                "product_server": "1"
            }
            response = requests.post(url, headers=headers, json=data)
            response_data = response.json()
            print(response.json())
            if response_data['success']:
                data = response_data['data']
                return 0, data
            time.sleep(2)
        print("Change Your Provider / Layanan -_-")
        sys.exit()
    elif providers == 3:
        for i in range(100):
            if layanans == "Old":
                rent = sa.getRentList()
                try:
                    return rent['values']['0']['id'] , rent['values']['0']['phone']
                except:
                    print(rent['message'])
            else:
                rent = sa.getRentNumber(service='go', time=4, operator=layanans, country=6)
                try:
                    return rent['phone']['id'] , rent['phone']['number']
                except:
                    print(rent['message'])
        print("Change Your Provider / Layanan -_-")
        sys.exit()
    elif providers == 4:
        for ipo in range(1000):
            if layanans == "Old":
                x = requests.get(f"https://smshub.org/stubs/handler_api.php?api_key={api}&action=getCurrentActivations")
                data = x.json()
                data_list = []
                if data["status"] == "success":
                    for item in data["array"]:
                        data_list.append({
                            "id": item["id"],
                            "phone": item["phone"],
                            "status": item["status"]
                        })
                    print("==========================================================")
                    print("Daftar Order:")
                    for i, entry in enumerate(data_list):
                        print(f"{i + 1}. ID: {entry['id']}, Phone: {entry['phone']}, Status: {entry['status']}")
                    for inlop in range(3):
                        try:
                            print("==========================================================")
                            choice = int(input("Pilih nomor yang ingin pilih: ")) - 1
                            if 0 <= choice < len(data_list):
                                selected_data = data_list[choice]
                                print("==========================================================")
                                print(f"Data yang dipilih:")
                                return selected_data['id'], selected_data['phone'], selected_data['status']
                            else:
                                print("Pilihan tidak valid.")
                        except:
                            print("Input harus berupa angka.")
                    print("Change Your Provider / Layanan -_-")
                    sys.exit()
                else:
                    print("Data Order Not Found!!!")
                    time.sleep(3)
                    sys.exit()
            else:
                # x = requests.get(f"https://smshub.org/stubs/handler_api.php?api_key={api}&action=getNumber&service=go&operator={layanans}&country=6&&maxPrice=0.13&currency=643")
                x = requests.get(f"https://smshub.org/stubs/handler_api.php?api_key={api}&action=getNumber&service=go&operator={layanans}&country=6")
                data = x.text
                if x.status_code == 200 and data != "NO_NUMBERS":
                    order_id = f"{data.split(":")[1]}"
                    num = f"{data.split(":")[2]}"
                    return order_id , num
                else:
                    print("Empty Number Change Your Layanan")
        print("Change Your Provider / Layanan -_-")
        sys.exit()

def get_inbox(id_order, tokens):
    if providers == 1:
        url = f'https://tokoclaude.com/api/get-orders/{api}/{id_order}'
        start_time = time.time()
        timeout_duration = 2 * 60
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout_duration:
                print("Timeout reached. No SMS received within 2 minutes.")
                return False, 0
            response = requests.get(url)
            if response.status_code == 201:
                data = response.json()
                if data.get('success') == True:
                    order_data = data["data"]["data"][0]
                    if order_data.get("status_sms") == "1":
                        sms_data = json.loads(order_data.get("sms", "[]"))
                        if sms_data:
                            sms_data.sort(key=lambda x: datetime.strptime(x["date"], '%Y-%m-%d %H:%M:%S'), reverse=True)
                            latest_sms = sms_data[0]["sms"]
                            otp = re.search(r'\b\d{6}\b', latest_sms)
                            if otp:
                                return True, otp.group()
                        else:
                            print("No SMS data found. Retrying...")
                    else:
                        print("Both conditions (status_sms == 1 and status == 3) not met yet. Retrying...")
            else: 
                print(f"Failed to get data. Status code: {response.status_code}. Retrying...")
            time.sleep(2)
    elif providers == 0:
        url = f'https://siotp.com/api/getotp?apikey={api}&id={id_order}'
        start_time = time.time()
        timeout_duration = 2 * 60
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout_duration:
                print("Timeout reached. No SMS received within 2 minutes.")
                return False, 0
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    data_content = data.get('data', {})
                    if data_content.get('status') == '3':
                        otp_message = data_content.get('inbox')
                        change_status(2, id_order)
                        return True, otp_message
                    else:
                        time.sleep(1)
                else:
                    print("Response status is not 'success'. Retrying...")
                    time.sleep(5)
            else:
                print(f"Failed to get data. Status code: {response.status_code}. Retrying...")
                time.sleep(5)
    elif providers == 2:
        start_time = time.time()
        timeout_duration = 2 * 60
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout_duration:
                print("Timeout reached. No SMS received within 2 minutes.")
                return False, 0
            url = 'https://wnrstore.com/api/v1/order/data'
            headers = {
                'Authorization': f'Bearer {tokens}'
            }
            params = {
                "page": 1,
                "query": "",
                "status": "",
                "created_on": ""
            }
            response = requests.get(url, headers=headers, params=params)
            response_data = response.json()
            if response_data['success']:
                latest_data = response_data['data']['data'][0]
                if latest_data['phone_message'] is not None and latest_data['status'] == 'completed':  # Jika ada pesan
                    print("OTP:", latest_data['phone_message'])
                    change_status(latest_data['id'], tokens)
                    return True, latest_data['phone_message']
            else:
                print("Request gagal")

    elif providers == 3:
        start_time = time.time()
        timeout_duration = 2 * 60
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout_duration:
                print("Timeout reached. No SMS received within 2 minutes.")
                return False, 0
            status = sa.getRentStatus(id_order)
            try:
                return True, re.search(r'\b\d{6}\b', status['values']['0']['text']).group()
            except:
                print(status['message']) # Error text

    elif providers == 4:
        start_time = time.time()
        timeout_duration = 2 * 60
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout_duration:
                print("Timeout reached. No SMS received within 2 minutes.")
                return False, 0
            x = requests.get(f"https://smshub.org/stubs/handler_api.php?api_key={api}&action=getStatus&id={id_order}")
            data = x.text
            if x.status_code == 200:
                if data != "STATUS_WAIT_CODE":
                    otp_data = data.split(":")[1]
                    change_status(0,id_order)
                    return True, otp_data


def cancel_order(id_order):
    if providers == 1:
        url = f'https://tokoclaude.com/api/cancle-orders/{api}/{id_order}'
        response = requests.get(url)
        data = response.json()
        return data
    elif providers == 4:
        x = requests.get(f"https://smshub.org/stubs/handler_api.php?api_key={api}&action=setStatus&status=8&id={id_order}")
        return x.text

def get_balance():
    if providers == 1:
        while True:
            response = requests.get(f'https://tokoclaude.com/api/get-profile/{api}', timeout=20)
            if response.status_code == 201:
                data = response.json()
                if data.get('success') == True:
                    username = data['data']['data'].get('username')
                    saldo = data['data']['data'].get('saldo')
                    return username, saldo, 0               
                else:
                    print(data)
            time.sleep(2)
    elif providers == 0:
        while True:
            response = requests.get(f'https://api.siotp.com/api/getbalance?apikey={api}', timeout=20)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    saldo = data.get('balance')
                    username = "unknow"
                    return username, saldo, 0
                else:
                    print("Response status is not 'success'.")
            else:
                print(f"Failed to get data. Status code: {response.status_code}")
            time.sleep(2)
    elif providers == 2:
        while True:
            url = 'https://api.wnrgroup.id/api/v1/auth/login'
            data = {
                "id": "235a7849-3132-4fdf-a300-4c162f49466e-1690384136058",
                "username": email_wnr,
                "password": password_wnr,
                "api_key": api
            }

            response = requests.post(url, headers=headers, json=data)
            response_data = response.json()
            if response_data['success']:
                fullname = response_data['data']['fullname']
                balance = response_data['data']['balance']
                access_token = response_data['data']['access_token']
                return fullname, balance, access_token

    elif providers == 3:
        while True:
            balance = sa.getBalance() # {'balance': '100.00'}
            try:
                return "unknow", balance['balance'], 0
            except:
                print(balance['message']) # Error text
    elif providers == 4:
        while True:
            x = requests.get(f"https://smshub.org/stubs/handler_api.php?api_key={api}&action=getBalance")
            if x.status_code == 200:
                balance = f"${x.text.split(":")[1]}"
                return "unknow", balance, 0

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

def main():
    while True:
        pilih = int(input("==========================================================\n0 = nomer lama\n1 = nomer baru\nPilih: "))
        if providers == 0 or providers == 2 or providers == 3 or providers == 4:
            layanan_mapping = {
                0: "axis",
                1: "indosat",
                2: "three",
                3: "telkomsel",
                4: "smartfren",
                5: "any"
            }

            layanan = int(input("==========================================================\n0 = axis\n1 = Indosat\n2 = Three\n3 = Telkomsel\n4 = Smartfren\n5 = Random\nPilih: "))
            layanan_str = layanan_mapping.get(layanan, "Layanan tidak valid")
            print("Layanan yang dipilih:", layanan_str)
        else:
            layanan_str = "aaa"
        # ortua = str(input("==========================================================\nEmail Ortu: "))
        # try:
        if pilih == 0 and providers == 3:
            order_id, phone_number = get_phone("0", "Old")
            otp_code = None
            stat, otp_code_2 = get_inbox(order_id,0)
        if pilih == 0 and providers == 4:
            order_id, phone_number,status_smshub = get_phone("0", "Old")
            otp_code = None
            if (status_smshub == 2 and status_smshub == "6") or (status_smshub == 2 and status_smshub == 6):
                stat, otp_code_2 = get_inbox(order_id,0)
            else:
                otp_code_2 = None
        elif pilih == 0 and providers != 2:
            order_id = str(input("order_id : "))
            phone_number = str(input("phone_number : "))
            otp_code = None
            otp_code_2 = None
        elif pilih == 0 and providers == 2:
            order_id = None
            phone_number = str(input("phone_number : "))
            otp_code = None
            otp_code_2 = None
        else:
            order_id = None
            phone_number = None
            otp_code = None
            otp_code_2 = None
        if pilih == 0:
            print(f"phone: {phone_number}")
            print(f"order id: {order_id}")
            print(f"otp_code_2: {otp_code_2}")
        inc = 0
        while True:
            try:
                print("==========================================================")
                username, saldo, token = get_balance()
                print(f"Username : {username}")
                print(f"Balance  : {saldo}")
                print(f"Token    : {token}")
                print("==========================================================")
                if phone_number is None:
                    print("Order Phone Number ....")
                    order_id, phone_number = get_phone(token, layanan_str)
                    print(f"phone: {phone_number}")
                    print(f"order id: {order_id}")
                    print(f"Otp Before: {otp_code_2}")

                print(f"\n=====================Create Email ( Pribadi )=====================")
                fake_iphone_user_agent = random.choice(iphone_user_agents)
                print(fake_iphone_user_agent)
                driver = Driver(
                    uc=True,
                    # proxy="socks5://61mm2hp.localto.net:7695",
                    agent=fake_iphone_user_agent
                    # extension_dir="proxy_auth_extension"
                )
                driver.delete_all_cookies()
                
                driver.get('https://myaccount.google.com/security')
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div > c-wiz > c-wiz > div > div.s7iwrf.gMPiLc.Kdcijb > div > div > c-wiz > section > div > div > div > div > div > div > header > div.m6CL9 > div')
                    )
                ).click()
                time.sleep(1)
                wait_and_click(driver, '#yDmH0d > c-wiz > div > div.JYXaTc > div > div.FO2vFd > div > div > div:nth-child(1) > div > button')
                try:
                    wait_and_click(driver, '#yDmH0d > c-wiz > div > div.JYXaTc > div > div.FO2vFd > div > div > div:nth-child(2) > div > ul > li:nth-child(2)')
                except:
                    slsloo = 0
                firs = fake.first_name()
                last = fake.last_name()
                wait_and_send(driver, '#firstName', firs)
                wait_and_send(driver, '#lastName', last)
                wait_and_click(driver, '#collectNameNext > div > button')
                wait_and_send(driver, '#day', random.randint(1, 9))
                dropdown_element = driver.find_element(By.ID, 'month')
                random_value = str(random.randint(1, 12))
                select = Select(dropdown_element)
                select.select_by_value(random_value)

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#year'))
                ).send_keys("2000")
                dropdown_element = driver.find_element(By.ID, 'gender')
                random_value = str(random.randint(1, 2))
                select = Select(dropdown_element)
                select.select_by_value(random_value)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#birthdaygenderNext > div > button'))
                ).click()
                time.sleep(3)
                email_ortu = f"{firs}{last}{str(random.randint(1, 100000000))}"
                print(f"email: {email_ortu}@gmail.com")
                try:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div > form > span > section > div > div > div.myYH1.v5IR3e.V9RXW > div.Hy62Fc > div > span > div:nth-child(3) > div > div.uxXgMe > div')
                        )
                    ).click()
                    timr.sleep(1)
                    wait_and_send(driver, '#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div > form > span > section > div > div > div.BvCjxe > div.AFTWye > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input', email_ortu)
                    wait_and_click(driver, "#next > div > button")
                except:
                    xops = "ffggg"
                try:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div > form > span > section > div > div > div > div.AFTWye > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
                        )
                    ).send_keys(email_ortu)
                    wait_and_click(driver, '#next > div > button')
                except:
                    sj = "yeah"
                time.sleep(2)
                wait_and_send(driver, '#passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input', '123456tujuh')
                wait_and_send(driver, '#confirm-passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input', '123456tujuh')
                wait_and_click(driver, '#createpasswordNext > div > button')
                time.sleep(5)
                while True:
                    try:
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, '#phoneNumberId'))
                        ).clear()
                        print("Get Phone Number")
                        if phone_number is None:
                            order_id, phone_number = get_phone(token, layanan_str)
                        print(f"phone: {phone_number}")
                        print(f"order id: {order_id}")
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, '#phoneNumberId'))
                        ).clear()
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, '#phoneNumberId'))
                        ).send_keys("+" + str(phone_number))
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.JYXaTc > div > div > div > div > button'))
                        ).click()
                        time.sleep(5)
                        try:
                            WebDriverWait(driver, 20).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div.AcKKx > form > span > section > div > div > div.sg1AX.Jj6Lae > div > div.MK96uf > div.hLRWIe')
                                )
                            )
                            print("nomer tidak valid")
                            if providers == 1 or providers == 4:
                                status_cancel = cancel_order(order_id)
                                print(status_cancel)
                            order_id, phone_number = get_phone(token, layanan_str)
                        except:
                            break
                    except:
                        ksko = 0
                time.sleep(2)
                status_otp, otp_code = get_inbox(order_id, token)
                while True:
                    if otp_code_2 == otp_code:
                        status_otp, otp_code = get_inbox(order_id, token)
                    else:
                        if providers != 0 and providers != 2 and providers != 4:
                            status_otp, otp_code_2 = get_inbox(order_id,token)
                        break
                if not status_otp:
                    if providers == 1 or providers == 4:
                        status_cancel = cancel_order(order_id)
                        print(status_cancel)
                    elif providers == 0:
                        change_status(0, order_id)
                    print("Can't Get OTP Code Loop Use New Number")
                    phone_number = None
                    order_id =None
                else:
                    try:
                        print(f"otp_code: {otp_code}")
                        wait_and_send(driver, '#code', otp_code)
                        time.sleep(2)
                        wait_and_click(driver, '#next > div > button')
                        time.sleep(3)
                        wait_and_click(driver, "#recoverySkip > div > button")
                        time.sleep(3)
                        wait_and_click(driver, "#yDmH0d > c-wiz > div > div.JYXaTc > div > div > div > div > button")
                        time.sleep(3)
                        wait_and_click(driver, "#yDmH0d > c-wiz > div > div.JYXaTc.lUWEgd > div > div.TNTaPb > div > div > button")
                        time.sleep(15)
                        print("done")
                        with open('new_account.txt', 'a') as result_file:
                            result_file.write(email_ortu + '@gmail.com\n')
                        inc += 1
                    except:
                        ksoo = 0 
                driver.get("https://myaccount.google.com/signinoptions/recoveryoptions?opendialog=collectphone")
                time.sleep(5)
                if phone_number == None:
                    order_id, phone_number = get_phone(token,layanan_str)
                wait_and_send(driver, "#c6", "+"+phone_number)
                time.sleep(3)
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.iteLLc.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div.VfPpkd-T0kwCb > div > div > button'))).click()
                time.sleep(3)
                
                max_loop = 10
                h_done = False
                inc = 0
                link_anak ="https://accounts.google.com/embedded/v2/kidsignup/createaccount"
                while not h_done :
                    try:
                        if inc == "6" or inc == 6:
                            break
                        username, saldo, token = get_balance()
                        print(f"\n=====================Create Email ( {inc+1} )=====================")
                        driver.get(link_anak)
                        wait_and_send(driver, '#firstName',fake.first_name())
                        wait_and_send(driver, '#lastName',fake.last_name())
                        wait_and_click(driver, '#collectNameNext > div > button')
                        wait_and_send(driver, '#day',random.randint(1, 9))
                        dropdown_element = driver.find_element(By.ID, 'month')
                        random_value = str(random.randint(1, 12))
                        select = Select(dropdown_element)
                        select.select_by_value(random_value)

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#year'))).send_keys("2015")
                        dropdown_element = driver.find_element(By.ID, 'gender')
                        random_value = str(random.randint(1, 2))
                        select = Select(dropdown_element)
                        select.select_by_value(random_value)
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#birthdaygenderNext > div > button'))).click()
                        time.sleep(2)
                        try:
                            email = f"{fake.first_name()}{fake.last_name()}{str(random.randint(1, 10000000))}"
                            print(f"{email}@gmail.com")
                            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > div.d2CFce.cDSmF > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input'))).send_keys(email)
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#next > div > button'))).click()
                        except:
                            try:
                                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.IhH7Wd.hdGwMb.V9RXW > div.ci67pc > div > span > div:nth-child(1) > div > div.enBDyd > div'))).click()
                                wait_and_click(driver, "#next > div > button")
                            except:
                                xops = "ffggg"
                        time.sleep(2)
                        wait_and_send(driver, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input', '123456tujuh')
                        link_anak = driver.current_url
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#createpasswordNext > div > button'))).click()
                        time.sleep(2)
                        while True:
                            try:
                                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#phoneNumberId'))).clear()
                                print("Get Phone Number")
                                if phone_number == None:
                                    order_id, phone_number = get_phone(token,layanan_str)
                                print(f"phone: {phone_number}")
                                print(f"order id: {order_id}")
                                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#phoneNumberId'))).clear()
                                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#phoneNumberId'))).send_keys("+"+str(phone_number))
                                time.sleep(1)
                                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div > div > div > button'))).click()
                                try:
                                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.bAnubd.Jj6Lae > div > div.gFxJE > div.jPtpFe')))
                                    print("nomer tidak valid")
                                    if providers == 1 or providers == 4:
                                        status_cancel = cancel_order(order_id)
                                        print(status_cancel)
                                    driver.get("https://myaccount.google.com/signinoptions/recoveryoptions?opendialog=collectphone")
                                    order_id, phone_number = get_phone(token,layanan_str)
                                    wait_and_send(driver, "#c6", phone_number)
                                    try:
                                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.uW2Fw-Sx9Kwc.uW2Fw-Sx9Kwc-OWXEXe-n2to0e.iteLLc.uW2Fw-Sx9Kwc-OWXEXe-FNFY6c > div.uW2Fw-wzTsW > div > div.uW2Fw-T0kwCb > div.qsqhnc > div > button'))).click()
                                    except:
                                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.iteLLc.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div.VfPpkd-T0kwCb > div > div > button'))).click()
                                    print(f"new phone: {phone_number}")
                                    print(f"new order id: {order_id}")
                                    max_loop = max_loop + 1
                                    time.sleep(7)
                                except:
                                    status_otp, otp_code = get_inbox(order_id,token)
                                    print(f"otp_code: {otp_code}")
                                    while True : 
                                        if otp_code_2 == otp_code  :
                                            status_otp, otp_code = get_inbox(order_id,token)
                                        else :
                                            break 
                                    if not status_otp:
                                        if providers == 1 or providers == 4:
                                            status_cancel = cancel_order(order_id)
                                            print(status_cancel)
                                        elif providers == 0:
                                            change_status(0, order_id)
                                        print("Can't Get OTP Code Loop Use New Number")
                                        max_loop = max_loop + 1
                                        driver.get("https://myaccount.google.com/signinoptions/recoveryoptions?opendialog=collectphone")
                                        order_id, phone_number = get_phone(token,layanan_str)
                                        wait_and_send(driver, "#c6", phone_number)
                                        try:
                                            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.uW2Fw-Sx9Kwc.uW2Fw-Sx9Kwc-OWXEXe-n2to0e.iteLLc.uW2Fw-Sx9Kwc-OWXEXe-FNFY6c > div.uW2Fw-wzTsW > div > div.uW2Fw-T0kwCb > div.qsqhnc > div > button'))).click()
                                        except:
                                            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.iteLLc.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div.VfPpkd-T0kwCb > div > div > button'))).click()
                                        break
                                    try:
                                        wait_and_send(driver, '#code', otp_code)
                                        time.sleep(1)
                                        wait_and_click(driver, '#next > div > button')
                                        time.sleep(2)
                                        try:
                                            time.sleep(1)
                                            wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section:nth-child(7) > div > div > div:nth-child(2) > div.ci67pc > div")
                                            wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section:nth-child(7) > div > div > div:nth-child(1) > div.ci67pc > div")
                                            wait_and_click(driver, "#dnpPage-next > div > button")
                                            time.sleep(2)
                                        except:
                                            slos = 0
                                        try:
                                            wait_and_send(driver, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input", "123456tujuh")
                                            time.sleep(1)
                                            wait_and_click(driver, "#passwordNext > div > button")
                                            time.sleep(3)
                                            wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div > div > div > button")
                                            time.sleep(2)
                                            wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > ul > li:nth-child(1) > div")
                                            time.sleep(2)
                                            wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button")
                                            time.sleep(8)
                                            try : 
                                                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input'))).clear()

                                                status_otp, otp_code_2 = get_inbox(order_id,token)
                                                while True : 
                                                    if otp_code_2 == otp_code  :
                                                        status_otp, otp_code_2 = get_inbox(order_id,token)
                                                    else :
                                                        break 
                                                if not status_otp:
                                                    if providers == 1 or providers == 4:
                                                        status_cancel = cancel_order(order_id)
                                                        print(status_cancel)
                                                    elif providers == 0:
                                                        change_status(0, order_id)
                                                    print("Can't Get OTP Code Loop Use New Number")
                                                    max_loop = max_loop + 1
                                                    driver.get("https://myaccount.google.com/signinoptions/recoveryoptions?opendialog=collectphone")
                                                    order_id, phone_number = get_phone(token,layanan_str)
                                                    wait_and_send(driver, "#c6", phone_number)
                                                    try:
                                                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.uW2Fw-Sx9Kwc.uW2Fw-Sx9Kwc-OWXEXe-n2to0e.iteLLc.uW2Fw-Sx9Kwc-OWXEXe-FNFY6c > div.uW2Fw-wzTsW > div > div.uW2Fw-T0kwCb > div.qsqhnc > div > button'))).click()
                                                    except:
                                                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.iteLLc.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div.VfPpkd-T0kwCb > div > div > button'))).click()
                                                    break    
                                                wait_and_send(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input", otp_code_2)
                                                time.sleep(1)
                                                wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button")
                                                time.sleep(8)
                                                inc = inc + 1
                                                

                                            except :
                                                
                                                h_done = True
                                                break
                                        except:
                                            
                                            slos = 0
                                    except:
                                        
                                        print("otp salah")
                                        input("Done")
                                break
                            except:
                                print("Bypass Phone!!!")
                                if providers != 0 and providers != 2 and providers != 4:
                                    status_otp, otp_code = get_inbox(order_id,token)
                                try:
                                    wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section:nth-child(7) > div > div > div:nth-child(2) > div.ci67pc > div")
                                    wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section:nth-child(7) > div > div > div:nth-child(1) > div.ci67pc > div")
                                    wait_and_click(driver, "#dnpPage-next > div > button")
                                    time.sleep(2)
                                except:
                                    slos = 0
                                try:
                                    wait_and_send(driver, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input", "123456tujuh")
                                    time.sleep(1)
                                    wait_and_click(driver, "#passwordNext > div > button")
                                    time.sleep(3)
                                    wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div > div > div > button")
                                    time.sleep(3)
                                    wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > ul > li:nth-child(1) > div")
                                    time.sleep(3)
                                    wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button")
                                    time.sleep(8)
                                    try : 
                                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input'))).clear()

                                        status_otp, otp_code_2 = get_inbox(order_id,token)
                                        while True : 
                                            if otp_code_2 == otp_code  :
                                                status_otp, otp_code_2 = get_inbox(order_id,token)
                                            else :
                                                break 
                                        if not status_otp:
                                            if providers == 1 or providers == 4:
                                                status_cancel = cancel_order(order_id)
                                                print(status_cancel)
                                            elif providers == 0:
                                                change_status(0, order_id)
                                            print("Can't Get OTP Code Loop Use New Number")
                                            max_loop = max_loop + 1
                                            driver.get("https://myaccount.google.com/signinoptions/recoveryoptions?opendialog=collectphone")
                                            order_id, phone_number = get_phone(token,layanan_str)
                                            wait_and_send(driver, "#c6", phone_number)
                                            try:
                                                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.uW2Fw-Sx9Kwc.uW2Fw-Sx9Kwc-OWXEXe-n2to0e.iteLLc.uW2Fw-Sx9Kwc-OWXEXe-FNFY6c > div.uW2Fw-wzTsW > div > div.uW2Fw-T0kwCb > div.qsqhnc > div > button'))).click()
                                            except:
                                                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.iteLLc.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div.VfPpkd-T0kwCb > div > div > button'))).click()
                                            break
                                        print(f"otp_code: {otp_code_2}")
                                        wait_and_send(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input", otp_code_2)
                                        time.sleep(1)
                                        wait_and_click(driver, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button")
                                        time.sleep(10)
                                        inc = inc + 1
                                        

                                    except :
                                        
                                        h_done = True
                                        break
                                except:
                                    
                                    slos = 0
                                max_loop = max_loop + 1
                                break
                    except:
                        
                        print("reload")
                driver.quit()
                return email_ortu
                break
            except:
                driver.quit()
                print("Try Reopen Chrome...")
os.system('cls')
while True:
    if choser == 1 or choser == "1":
        providers = int(input("==========================================================\n0. Siotp\n1. tokoclaude\n2. wnrstore\n3. smsactive\n4. smshub\nPilih: "))
        if providers == 0:
            api = lines[0].strip()
        elif providers == 1:
            api = lines[1].strip()
        elif providers == 2:
            api = lines[2].strip()
            email_wnr = lines[3].strip()
            password_wnr = lines[4].strip()
        elif providers == 3:
            api = lines[5].strip()
            sa = SMSActivateAPI(api)
            sa.debug_mode = False
        elif providers == 4:
            api = lines[6].strip()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        try:
            email_ortu_ret = main()
            href_links = []
            mail_list = []
            driver = Driver(uc=True)
            if login(email_ortu_ret, "123456tujuh"):
                time.sleep(1)
                prom()
                time.sleep(2)
                family()
                time.sleep(2)
                sec_code = auth_2fa()
                for i in range(len(mail_list)):
                    with open('result_anak.txt', 'a') as result_file:
                        result_file.write(f"{mail_list[i]}|{email_ortu_ret}@gmail.com\n")
                with open('result_ortu.txt', 'a') as result_file:
                    result_file.write(f"{email_ortu_ret}@gmail.com|123456tujuh@|{sec_code}\n")
                change_password()
                time.sleep(2)
                loqout()
                time.sleep(2)
                driver.quit()
        except:
            os.system('cls')
            print("==========================================================")
            print("Change Your Provider / Layanan -_-")
            jsk = 0    
