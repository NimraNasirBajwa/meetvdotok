import smtplib
import time
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import clipboard
from selenium.webdriver.common.by import By
from pom import login


class Test_001_Login:

    User_Name1 = "Nimra"
    User_Name2 = "Summen"
    User_Name3 = "Rida"
    User_Name4 = "Faiqa"
    Base_url = "https://meet.vdotok.com/"

    global driver
    global driver1
    def test_login(self):
        options = webdriver.FirefoxOptions()
        options.set_preference("media.navigator.permission.disabled", True)
        global driver
        driver = webdriver.Firefox(options=options, executable_path=r"C:\Program Files (x86)\geckodriver.exe")
        driver.maximize_window()
        driver.get('https://meet.vdotok.com/')
        driver.implicitly_wait(5)
        Test1 = login(driver)
        Test1.task1(self.User_Name1)
        Test1.copyurl()
        global message1
        message1 = clipboard.paste()

    #sendemail

        msg = EmailMessage()
        msg['Subject'] = 'Vdotok_link'
        msg['From'] = 'Nimra'
        msg['To'] = 'nimranasir254@gmail.com',
        msg.set_content(message1)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()

        server.starttls()
        server.ehlo()
        server.login("nimranasir301@gmail.com", "bpcqslovwihohelm")
        server.send_message(msg)
        server.quit()

    def test_login2(self):

        opt = Options()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        opt.add_argument('--start-maximized')
        opt.add_argument('--allow-file-access-from-files')
        opt.add_experimental_option("detach", True)
        opt.add_argument('--disable-gesture-requirement-for-media-playback')
        opt.add_argument('--use-fake-ui-for-media-stream')
        opt.add_argument('--use-fake-device-for-media-stream')
        opt.add_argument('--no-sandbox')
        opt.add_argument('--use-file-for-fake-video-capture=C:\\video\\myfile2.y4m')
        opt.add_argument('--use-file-for-fake-audio-capture=C:\\Users\\Nimra Nasir\\Downloads\\Music\\audio.wav')

        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,

        })
        driver = webdriver.Chrome(options=opt, executable_path="C:\Program Files (x86)\chromedriver.exe")
        driver.get(message1)
        driver.implicitly_wait(5)
        Test2 = login(driver)
        Test2.task1(self.User_Name2)

    def test_login3(self):

        opt = Options()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        opt.add_argument('--start-maximized')
        opt.add_argument('--allow-file-access-from-files')
        opt.add_experimental_option("detach", True)
        opt.add_argument('--disable-gesture-requirement-for-media-playback')
        opt.add_argument('--use-fake-ui-for-media-stream')
        opt.add_argument('--use-fake-device-for-media-stream')
        opt.add_argument('--no-sandbox')
        opt.add_argument('--use-file-for-fake-video-capture=C:\\video\\myfile2.y4m')
        opt.add_argument('--use-file-for-fake-audio-capture=C:\\Users\\Nimra Nasir\\Downloads\\Music\\audio.wav')

        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,

        })
        driver1 = webdriver.Chrome(options=opt, executable_path="C:\Program Files (x86)\chromedriver.exe")
        driver1.implicitly_wait(5)
        driver1.get(message1)
        Test3 = login(driver1)
        Test3.task1(self.User_Name3)


    def test_login4(self):
        global driver1
        opt = Options()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        opt.add_argument('--start-maximized')
        opt.add_argument('--allow-file-access-from-files')
        opt.add_experimental_option("detach", True)
        opt.add_argument('--disable-gesture-requirement-for-media-playback')
        opt.add_argument('--use-fake-ui-for-media-stream')
        opt.add_argument('--use-fake-device-for-media-stream')
        opt.add_argument('--no-sandbox')
        opt.add_argument('--use-file-for-fake-video-capture=C:\\video\\myfile2.y4m')
        opt.add_argument('--use-file-for-fake-audio-capture=C:\\Users\\Nimra Nasir\\Downloads\\Music\\audio.wav')

        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,

        })
        driver1 = webdriver.Chrome(options=opt, executable_path="C:\Program Files (x86)\chromedriver.exe")
        driver1.get(message1)
        driver1.implicitly_wait(5)
        Test3 = login(driver1)
        Test3.task1(self.User_Name4)
        time.sleep(5)

    def test_chat(self):
        chat1 = driver1.find_element(By.XPATH, "//img[@class='responseButtonImg AnalyticsReturnToChat']")
        chat1.click()
        time.sleep(2)
        for x in range(20):
            entertext = driver1.find_element(By.XPATH, "//input[@placeholder='Type to reply..']")
            entertext.send_keys("hi")
            send = driver1.find_element(By.XPATH, "//div[@class='col-sm-8 rightSide']//div[2]//img[1]")
            send.click()
            entertext2 = driver1.find_element(By.XPATH, "//input[@placeholder='Type to reply..']")
            entertext2.send_keys("How are you?")
            send2 = driver1.find_element(By.XPATH, "//div[@class='col-sm-8 rightSide']//div[2]//img[1]")
            send2.click()
            handles = driver.window_handles
            for y in handles:
                driver.switch_to.window(y)
                chat2 = driver.find_element(By.XPATH, "//img[@class='responseButtonImg AnalyticsReturnToChat']")
                chat2.click()
                entertext = driver.find_element(By.XPATH, "//input[@placeholder='Type to reply..']")
                entertext.send_keys("hi")
                send = driver.find_element(By.XPATH, "//div[@class='col-sm-8 rightSide']//div[2]//img[1]")
                send.click()
                returncal = driver.find_element(By.XPATH, "//div[@class='AnalyticsReturnToCall']")
                returncal.click()
                if x == 10:
                    break








