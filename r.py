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
        timeout_duration = 60
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
        timeout_duration = 60
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
        timeout_duration = 60
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
        timeout_duration = 60
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
        timeout_duration = 60
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

def main(email,pwd,sec_code):
    while True:
        # pilih = int(input("==========================================================\n0 = nomer lama\n1 = nomer baru\nPilih: "))
        pilih = 1
        if providers == 0 or providers == 2 or providers == 3 or providers == 4:
            layanan_mapping = {
                0: "axis",
                1: "indosat",
                2: "three",
                3: "telkomsel",
                4: "smartfren",
                5: "any"
            }

            # layanan = int(input("==========================================================\n0 = axis\n1 = Indosat\n2 = Three\n3 = Telkomsel\n4 = Smartfren\n5 = Random\nPilih: "))
            layanan = 3
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
                # if phone_number is None:
                #     print("Order Phone Number ....")
                #     order_id, phone_number = get_phone(token, layanan_str)
                #     print(f"phone: {phone_number}")
                #     print(f"order id: {order_id}")
                #     print(f"Otp Before: {otp_code_2}")

                print(f"\n=====================Login Email ( Pribadi )=====================")
                fake_iphone_user_agent = random.choice(iphone_user_agents)
                driver = Driver(
                    uc=True,
                    # proxy="socks5://61mm2hp.localto.net:7695",
                    # agent=fake_iphone_user_agent,
                    extension_dir="data/capmonster"
                )
                driver.delete_all_cookies()
                driver.get("chrome://extensions/?id=pabjfbciaedomjjfelfafejkppknjleh")
                time.sleep(1)         
                driver.get('https://myaccount.google.com/security')
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div:nth-child(2) > div > c-wiz > c-wiz > div > div.s7iwrf.gMPiLc.Kdcijb > div > div > c-wiz > section > div > div > div > div > div > div > header > div.m6CL9 > div'))).click()
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'identifier'))).send_keys(email)
                print("Email : "+email)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#identifierNext > div > button'))).click()
                time.sleep(2)
                try:
                    checkings = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#headingText > span'))).text
                    done_solved = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c0 > div > div.cm-addon.cm-addon-recaptcha > div > span'))).text
                    while done_solved == "In process...":
                        print(done_solved)
                        time.sleep(1)
                        done_solved = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c0 > div > div.cm-addon.cm-addon-recaptcha > div > span'))).text
                    wait_and_click(driver, '#yDmH0d > c-wiz > div > div.JYXaTc.lUWEgd > div > div.TNTaPb > div > div > button')
                    time.sleep(2)
                    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'))).send_keys(pwd)
                    print("Password : "+pwd+"\n===================================")
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordNext > div > button'))).click()
                    try:
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
                        try:
                            disble = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#headingText > span'))).text
                            if disble == "Your account has been disabled":
                                print("Account Banned...")
                                emails.pop(0)
                                with open('list_back.txt', 'w') as file:
                                    file.writelines(emails)
                                driver.quit()
                                return False
                        except:
                            exci = 0
                        while True:
                            try:
                                if phone_number == None:
                                    order_id, phone_number = get_phone(token,layanan_str)
                                    print(f"phone: {phone_number}")
                                wait_and_send(driver, '#deviceAddress', phone_number)
                                time.sleep(1)
                                wait_and_click(driver, '#next-button')
                                time.sleep(3)
                                try:
                                    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#deviceAddress')))
                                    print("Number Not valid")
                                    if providers == 1 or providers == 4:
                                        status_cancel = cancel_order(order_id)
                                        print(status_cancel)
                                    order_id, phone_number = get_phone(token,layanan_str)
                                    print(f"new phone: {phone_number}")
                                    print(f"new order id: {order_id}")
                                except:
                                    break
                                    yel = 0
                            except:
                                print("Try Write Phone Number...")
                        print("Done Write Phone Number...")
                        status_otp, otp_code = get_inbox(order_id,token)
                        print(f"otp_code: {otp_code}")
                        if not status_otp:
                            if providers == 1 or providers == 4:
                                status_cancel = cancel_order(order_id)
                                print(status_cancel)
                            elif providers == 0:
                                change_status(0, order_id)
                            driver.quit()
                            return False
                        wait_and_send(driver, '#smsUserPin', otp_code)
                        time.sleep(1)
                        wait_and_click(driver, '#next-button')
                        time.sleep(5)
                        driver.quit()
                        return True
                    except Exception as e:
                        print("Gagal, Retry...")
                except:
                    try:
                        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')))
                        print("Next Account")
                        driver.quit()
                        return True
                    except:
                        print("Trying Get Captcha")
            except:
                driver.quit()
                print("Try Reopen Chrome...")
os.system('cls')
with open('list_back.txt', 'r') as file:
    emails = file.readlines()
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
change_lay = None
while True:
    email = emails[0].replace('\n', '')

    if not email:
        break
    
    bacot = re.split(r'[|:;]', email.strip())
    logins = main(bacot[0],bacot[1],bacot[2])
    if logins:
        emails.pop(0)
        with open('list_back.txt', 'w') as file:
            file.writelines(emails)
        with open('result_ortu.txt', 'a') as result_file:
            result_file.write(f"{bacot[0]}|{bacot[1]}|{bacot[2]}\n")
    else:
        print("Cant Get Otp Number...")
