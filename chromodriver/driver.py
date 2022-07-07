from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
#options.add_argument("--incognito")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
    })



driver = webdriver.Chrome(options=options)

#driverwindows = webdriver.Chrome(options=options)

#driverlinux = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)