# # import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('http://127.0.0.1:5000/celfwebtest')
#
# # meeting_type = input('Type of Meeting: ')
# # if meeting_type == 'Prayer and Planning':
# type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div[1]/label/'
#                                                 'input')
# type_of_meeting.click()
#
# date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
# date_of_meeting.send_keys('30/10/2023')
#
# attendance = driver.find_element(By.NAME, 'CmisCellLeadersReport[total_no_at_cell_meeting]')
# attendance.send_keys(Keys.ARROW_RIGHT)
# attendance.send_keys(Keys.BACK_SPACE)
# attendance.send_keys('25')
#
# first_timers = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_first_timers]')
# first_timers.send_keys(Keys.ARROW_RIGHT)
# first_timers.send_keys(Keys.BACK_SPACE)
# first_timers.send_keys('4')
#
# new_converts = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_new_converts]')
# new_converts.send_keys(Keys.ARROW_RIGHT)
# new_converts.send_keys(Keys.BACK_SPACE)
# new_converts.send_keys('4')
#
# holy_spirit = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_infilling]')
# holy_spirit.send_keys(Keys.ARROW_RIGHT)
# holy_spirit.send_keys(Keys.BACK_SPACE)
# holy_spirit.send_keys('4')
#
# midweek = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_wed_service]')
# midweek.send_keys(Keys.ARROW_RIGHT)
# midweek.send_keys(Keys.BACK_SPACE)
# midweek.send_keys('10')
#
# sunday_service = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_sun_service]')
# sunday_service.send_keys(Keys.ARROW_RIGHT)
# sunday_service.send_keys(Keys.BACK_SPACE)
# sunday_service.send_keys('27')
#
# testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
# testimony.send_keys('Healing happened at the cell meeting')
#
# submit = driver.find_element(By.NAME, 'yt0')
# submit.click()

# from random import choice
# testimony_list = ['We had a wonderful meeting', 'We had a glorious time', 'We had an awesome time.']
# print(choice(testimony_list))

# for n in range(3):
#     if n == 3:
#         print('N')
