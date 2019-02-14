from selenium import webdriver

# open Firefox 
driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')
# open whatsapp web using webdriver

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))
# insert the contact name , message and number of time you want the message

input('Enter anything after scanning QR code')
# Scan QR Code

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
# Look for the contact from whatsapp web

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
# Loop to send message for count # of times to the contact 