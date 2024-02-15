from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import pyautogui as pg
import pandas as pd
from datetime import datetime
import os
import warnings
import smtplib as smtp

warnings.filterwarnings('ignore')
pg.FAILSAFE = False
cls = lambda: os.system('cls')
cwd = os.getcwd()
data = datetime.today().strftime("%d%m")
month = datetime.today().strftime("%m")


class Autofill():
    def __init__(self):
        self.driver_path = cwd + r'\driver\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--log-level=3')
        self.options.add_experimental_option('debuggerAddress', 'localhost:8051')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.implicitly_wait(4)
        
    def adicionar_colaborador(self):
        sleep(1)
        self.add_colaborador_bt = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/main/section/div/div[3]/div[3]/button')
        self.add_colaborador_bt.click()
        sleep(1)
        
    def locate_inputs(self):
        self.nome_input = self.driver.find_element(by=By.ID, value='nome')
        self.cpf_input = self.driver.find_element(by=By.ID, value='cpf')
        self.rg_input = self.driver.find_element(by=By.ID, value='rg')
        self.exp_input = self.driver.find_element(by=By.ID, value='orgaoExpedidor')
        self.email_input = self.driver.find_element(by=By.ID, value='email')
        self.sexo_input = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/main/section/div/div[3]/form/div[2]/form/div/div[6]/div/div/div/div/div/div/div[1]')
        
        # self.tel_input = self.driver.find_element(by=By.NAME, value='telefone01')
        # self.nascimento_input = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[2]/div/div[2]/form/div[1]/div[3]/div[1]/div/div/div[2]/fieldset/div[1]/div[1]/div/div[1]/div/input')
        sleep(1)
    
    def fill_sexo(self, d):
        self.d = d
        if self.d.upper() == 'M':
            self.sexo_input.click()
            sleep(1)
            self.masc_input = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/main/section/div/div[3]/form/div[2]/form/div/div[6]/div/div/div/div/div[2]/div/div[1]/div/div/li[1]')
            self.masc_input.click()

        elif self.d.upper() == 'F':
            self.sexo_input.click()
            sleep(1)
            self.fem_input = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/main/section/div/div[3]/form/div[2]/form/div/div[6]/div/div/div/div/div[2]/div/div[1]/div/div/li[2]')
            self.fem_input.click()
        

bot = Autofill()
bot.locate_inputs()