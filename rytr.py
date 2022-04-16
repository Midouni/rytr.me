import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



SELECT_LANGUAGE=""
SELECT_TONE=""
CHOOSE_USE_CASE=""
NUMBER_OF_VARIANTS=""
CREATIVE_LEVEL=""

class rytr:

    def __init__(self, browser="chrome",headless=None, version=97):
        self.driver = None
        if browser.lower() == "chrome":
            import undetected_chromedriver.v2 as UC #import undetected chrome 
            #setup browser option
            options = UC.ChromeOptions() 
            #disable the GPU
            options.add_argument("--disable-gpu") 
            options.add_argument("--disable-dev-shm-usage")
            #disable notification to avoid non-clickable webelement issue
            options.add_argument("--disable-notifications")     
            if headless is not None:
                #run the browser in the headless mode.
                options.add_argument('--headless')
            #set window size to avoid any problem with the responsive websites.
            options.add_argument('--window-size=1920,1080')
            
            #start the chrome browser with the speicifed
            self.driver = UC.Chrome(version_main=version, options=options)
        elif browser.lower() == "firefox":
            pass
        elif browser.lower() == "safari":
            pass
        elif browser.lower() == "remote":
            pass



    def __open_rytr(self,url="https://rytr.me"):
        """
        private function open url in paramter
        """
        self.driver.get(url)
        WebDriverWait(self.driver,10).until(
            lambda driver: driver.execute_script('return document.readyState == "complete"')
        )

    
    def login(self,email,password):
        self.__open_rytr(url="https://app.rytr.me/")
        try:
            # btn = WebDriverWait(self.driver,30).until(
            #     EC.presence_of_element_located((By.XPATH,'//button[text() = "Start Ryting"]'))
            # )
            # btn.click()

            btn2 = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,'//button[text() = "Continue with Email"]'))
            )
            btn2.click()

            inputEmail=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.NAME,'email'))
            )
            inputEmail.send_keys(email)
            inputEmail.send_keys(Keys.RETURN)

            inputEmail=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.NAME,'password'))
            )
            inputEmail.send_keys(password)
            inputEmail.send_keys(Keys.RETURN)
            
        except Exception as e:
            print(e)
            
#=====================================================================================================================================================================================================================
#
#=====================================================================================================================================================================================================================
    def __select_generator_option(self,select_langauage:str="english",select_tone:str="Convincing",choose_use_case:str="Facebook, Twitter, LinkedIn Ads",number_of_variants:int=3,creative_level:str="Optimal"):

        #select language
        self.__select_language(select_langauage)

        #selct Tone
        self.__select_tone(select_tone)

        #select use case
        self.__choose_use_case(choose_use_case)
        #select number of variants
        self.__Number_of_variants(number_of_variants)
        #select creativity level
        self.__creativity_level(creative_level)



    def __select_language(self,select_langauage:str):
        #private function used for select langauge

        try:
            #first click to choose language
            Select_language_btn=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.ID,"select-language"))
            )
            Select_language_btn.click()



            #click in language choosed
            languages_input=["arabic","bulgarian","chinese (S)","chinese (T)","czech","danish","dutch","english","farsi","filipino","finnish","french","german","greek","الكيان الصهيوني","hindi","hungarian","indonesian","italian","japanese","korean","lithuanian","malay","norwegian","polish","portuguese","romanian","russian","slovak","spanish","swedish","thai","turkish","vietnamese"]
            languages=["🇦🇪 Arabic","🇧🇬 Bulgarian","🇨🇳 Chinese (S)","🇹🇼 Chinese (T)","🇨🇿 Czech","🇩🇰 Danish","🇳🇱 Dutch","🇺🇸 English","🇮🇷 Farsi","🇵🇭 Filipino","🇫🇮 Finnish","🇫🇷 French","🇩🇪 German","🇬🇷 Greek","الكيان الصهيوني","🇮🇳 Hindi","🇭🇺 Hungarian","🇮🇩 Indonesian","🇮🇹 Italian","🇯🇵 Japanese","🇰🇷 Korean","🇱🇹 Lithuanian","🇲🇾 Malay","🇳🇴 Norwegian","🇵🇱 Polish","🇵🇹 Portuguese","🇷🇴 Romanian","🇷🇺 Russian","🇸🇰 Slovak","🇪🇸 Spanish","🇸🇪 Swedish","🇹🇭 Thai","🇹🇷 Turkish","🇻🇳 Vietnamese"]
            
            if(select_langauage.lower() in languages_input ):
                choosed=languages[languages_input.index(select_langauage.lower())]
                choose_language=WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.XPATH,"//*[contains(text(), '"+choosed+"')]"))
                )
                choose_language.click()
                print("select language done")
            else:
                raise Exception("Language not available!")
        except Exception as e:
            print(e)


    def __select_tone(self,select_tone:str):
        try:
            #first click to choose language
            Select_tone_btn=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.ID,"select-tone"))
            )
            Select_tone_btn.click()



            #click in tone choosed
            tone_input=["Appreciative","Assertive","Awestruck)","Candid","Casual","Cautionary","Compassionate","Convincing","Critical","Earnest","Enthusiastic","Formal","Funny","Humble","Humorous","Informative","Inspirational","Joyful","Passionate","Thoughtful","Urgent","Worried"]
            if(select_tone.capitalize() in tone_input ):
                choosed=select_tone.capitalize()
                choose_tone=WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.XPATH,"//*[contains(text(), '"+choosed+"')]"))
                )
                choose_tone.click()
                print("select tone done")
            else:
                raise Exception("Tone not available!")
        except Exception as e:
            print(e)


    def __choose_use_case(self,choose_use_case:str):
        try:
            #first click to choose type
            select_use_case_btn=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.ID,"select-type"))
            )
            select_use_case_btn.click()

            use_cases=["Blog Idea & Outline","Blog Section Writing","Brand Name","Business Idea Pitch","Business Ideas","Call To Action","Copywriting Framework: AIDA","Copywriting Framework: PAS","Email","Facebook, Twitter, LinkedIn Ads","Google Search Ads","Interview Questions","Job Description","Landing Page & Website Copies","Magic Command","Post & Caption Ideas","Product Description","Product Description (bullet points)","Profile Bio","Question & Answer","Reply to Reviews & Messages","SEO Meta Description","SEO Meta Title","SMS & Notifications","Song Lyrics","Story Plot","Tagline & Headline","Testimonial & Review","Video Channel Description","Video Description","Video Idea","Create Your Own Use-case"]
            if(choose_use_case in use_cases):
                choosed=choose_use_case
                choose_type=WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.XPATH,"//*[contains(text(), '"+choosed+"')]"))
                )
                choose_type.click()
                print("select type done")
            else:
                raise Exception ("type not available!")

        except Exception as e:
            print(e)

    def __Number_of_variants(self,number_of_variants):
        try:
            number_of_variants_btn=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Number of variants')]/following-sibling::button"))
            )
            number_of_variants_btn.click()

            Number_of_variants_possible=["1 variant","2 variants","3 variants"]
            if(4>number_of_variants>0):
                choosed=Number_of_variants_possible[number_of_variants-1]
                choose_type=WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.XPATH,"//*[contains(text(), '"+choosed+"')]"))
                )
                choose_type.click()
                print("select type done")
            else:
                raise Exception("only 1 2 or 3 variants possible")


        except Exception as e:
            print(e)

    def __creativity_level(self,creative_level:str):
        try:
            creative_level_btn=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Creativity level')]/following-sibling::button"))
            )
            creative_level_btn.click()

            creative_level_btn_possible=["Optimal","Low","Medium","High","Max"]
            if(creative_level.capitalize() in creative_level_btn_possible ):
                choosed=creative_level.capitalize()
                choose_type=WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.XPATH,"//*[contains(text(), '"+choosed+"')]"))
                )
                choose_type.click()
                print("select creative level done")
            else:
                raise Exception("only 1 2 or 3 variants possible")

        except Exception as e:
            print(e)


#=====================================================================================================================================================================================================================
#       use case section
#=====================================================================================================================================================================================================================

    def facebook_ads(self,product_name:str,product_description:str,select_langauage:str="english",select_tone:str="Appreciative",number_of_variants:int=3,creative_level:str="Optimal"):
        self.__select_generator_option(select_langauage=select_langauage,select_tone=select_tone,number_of_variants=number_of_variants,creative_level=creative_level)
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Product name')]/following-sibling::input"))
            ).send_keys(product_name)


            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Product description')]/following-sibling::textarea"))
            ).send_keys(product_description)
            time.sleep(4)
            #i use time.sleep because it dont wait the elemnt to be clickable IDK why
            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Ryte for me')]"))
            ).click()

        except Exception as e:
            print(e)


    def googel_search_ads(self,product_name:str,product_description:str,Target_keyword:str,select_langauage:str="english",select_tone:str="Appreciative",number_of_variants:int=3,creative_level:str="Optimal"):
        self.__select_generator_option(choose_use_case="Google Search Ads",select_langauage=select_langauage,select_tone=select_tone,number_of_variants=number_of_variants,creative_level=creative_level)
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Product name')]/following-sibling::input"))
            ).send_keys(product_name)


            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Product description')]/following-sibling::textarea"))
            ).send_keys(product_description)

            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Product name')]/following-sibling::input"))
            ).send_keys(Target_keyword)

            time.sleep(3)
            #i use time.sleep because it dont wait the elemnt to be clickable IDK why
            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Ryte for me')]"))
            ).click()

        except Exception as e:
            print(e)
    
    def blog_idea_and_outline(self,Primary_keyword:str,select_langauage:str="english",select_tone:str="Appreciative",number_of_variants:int=1,creative_level:str="Optimal"):
        self.__select_generator_option(choose_use_case="Blog Idea & Outline",select_langauage=select_langauage,select_tone=select_tone,number_of_variants=number_of_variants,creative_level=creative_level)

        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Primary keyword')]/following-sibling::input"))
            ).send_keys(Primary_keyword)
            time.sleep(3)
            #i use time.sleep because it dont wait the elemnt to be clickable IDK why
            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Ryte for me')]"))
            ).click()
        except Exception as e:
            print(e)
        
    
    def blog_section_writing(self,Section_topic:str,Section_keywords:str,select_langauage:str="english",select_tone:str="Appreciative",number_of_variants:int=1,creative_level:str="Optimal"):
        self.__select_generator_option(choose_use_case="Blog Section Writing",select_langauage=select_langauage,select_tone=select_tone,number_of_variants=number_of_variants,creative_level=creative_level)

        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Section topic')]/following-sibling::textarea"))
            ).send_keys(Section_topic)

            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Section keywords')]/following-sibling::textarea"))
            ).send_keys(Section_keywords)
            time.sleep(3)
            #i use time.sleep because it dont wait the elemnt to be clickable IDK why
            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Ryte for me')]"))
            ).click()
        except Exception as e:
            print(e)


    def brand_name(self,Brand_Description:str,select_langauage:str="english",select_tone:str="Appreciative",number_of_variants:int=1,creative_level:str="Optimal"):
        self.__select_generator_option(choose_use_case="Brand Name",select_langauage=select_langauage,select_tone=select_tone,number_of_variants=number_of_variants,creative_level=creative_level)

        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Brand Description')]/following-sibling::textarea"))
            ).send_keys(Brand_Description)
            time.sleep(3)
            #i use time.sleep because it dont wait the elemnt to be clickable IDK why
            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Ryte for me')]"))
            ).click()
        except Exception as e:
            print(e)


    def business_idea_pitch(self,business_idea:str,select_langauage:str="english",select_tone:str="Appreciative",number_of_variants:int=2,creative_level:str="Optimal"):
        self.__select_generator_option(choose_use_case="Business Idea Pitch",select_langauage=select_langauage,select_tone=select_tone,number_of_variants=number_of_variants,creative_level=creative_level)

        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Business idea')]/following-sibling::textarea"))
            ).send_keys(business_idea)
            time.sleep(3)
            #i use time.sleep because it dont wait the elemnt to be clickable IDK why
            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Ryte for me')]"))
            ).click()
        except Exception as e:
            print(e)


    def Email(self,key_points:str,select_langauage:str="english",select_tone:str="Appreciative",number_of_variants:int=2,creative_level:str="Optimal"):
        self.__select_generator_option(choose_use_case="Business Idea Pitch",select_langauage=select_langauage,select_tone=select_tone,number_of_variants=number_of_variants,creative_level=creative_level)

        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Key points')]/following-sibling::textarea"))
            ).send_keys(key_points)
            time.sleep(3)
            #i use time.sleep because it dont wait the elemnt to be clickable IDK why
            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Ryte for me')]"))
            ).click()
        except Exception as e:
            print(e)




        

class organizer:
    def __init__(self,driver):
        self.driver=driver


    def home_dir(self):
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//a[contains(text(), 'Home')]"))
                ).click()
        except Exception as e:
            print("you are in file to click home you have to be in folder. you can use back() function and next use home_dir()")
            print(e)
    def back(self):
        self.driver.back()

    def cd(self,folderName):
        """entry to file or directory with name"""
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//a[contains(text(), '"+folderName+"')]"))
                ).click()
        except Exception as e:
            print(e)

    def mkdir(self,dir_name):
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//button[contains(text(), 'New folder')]"))
                ).click()
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//div[contains(text(), 'New folder')]/following-sibling::div//div//input"))
                ).send_keys(dir_name)
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//button[contains(text(), 'Create')]"))
                ).click()
        except Exception as e:
            print(e)

    def touch(self,file_name):
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//button[contains(text(), 'New document')]"))
                ).click()
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//div[contains(text(), 'New document')]/following-sibling::div//div//input"))
                ).send_keys(file_name)
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//button[contains(text(), 'Create')]"))
                ).click()
        except Exception as e:
            print(e)



class extract:
    def __init__(self,driver):
        self.driver=driver

    def facebook_ads(self):
        try:
            text=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//h3/following-sibling::p/ancestor::div[@class='ProseMirror']"))
            )
            text=str(text.get_attribute('innerHTML'))
            n=text.count('<h3 dir="auto">')
            data={}
            for i in range(n):
                key=text[text.index('<h3 dir="auto">')+15:text.index('</h3>')]
                value=text[text.index('Ad Copy: ')+9:text.index('</p>')]
                data[key]=value
                if i!=n-1:
                    text=text[text.index('<h3 dir="auto">',2):]
            return data
        except Exception as e:
            print(e)
