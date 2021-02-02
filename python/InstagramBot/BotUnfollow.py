from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import json


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"./geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        sleep(3)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.ENTER)
        sleep(5)
        save_info_element = driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        turn_notifications_element = driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        self.curtir_fotos('florida') #Coloque a hashtag desejada

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(4)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            followButton = driver.find_element_by_xpath("//div[@class='bY2yH']/button")
            try:
                sleep(randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath("//*[local-name()='svg' and @aria-label='Unlike']")
                like_button().click()
            except Exception as e:
                sleep(2)

            if (followButton.text == 'Following'): #Deixar de seguir
                followButton.click()
                unfollow = driver.find_element_by_xpath('//button[contains(text(), "Unfollow")]').click()

                p_link = driver.find_element_by_xpath("//div[@class='e1e1d']").text
                link = ('https://www.instagram.com/{}/'.format(p_link))
                def write_json(data, filename="data.json"):
                    with open('data.json','w') as f:
                        json.dump(data, f, indent=4)
                with open ("data.json") as json_file:
                    data = json.load(json_file)
                    temp = data["links"]
                    y = {"unliked_link": link}
                    temp.append(y)

                    write_json(data)
                    sleep(randint(18,24))

            else:
                sleep(randint(18,21))

johnBot = InstagramBot('johnfake1510', 'fakejohn1510') #Coloque seu usuário e senha
johnBot.login()

# Para parar o script, basta digitar Ctrl + C no prompt de comando.


        
