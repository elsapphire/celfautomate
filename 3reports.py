import time
from random import choice

import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException

pd = pandas.read_csv('')
emails = pd.to_dict()['email']
passwords = pd.to_dict()['password']

login_dict = {}
for i in range(len(emails)):
    login_dict[i] = {
        'email': emails[i],
        'password': passwords[i]
    }
# print(login_dict)
testimony_list = ['We had a wonderful meeting', 'We had a glorious time', 'We had an awesome time.',
                  'It was an awesome time studying the word and sharing our thoughts.', 'It was an exciting meeting.']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://celfonline.org/V3/index.php?r=Site/Login')

# log in
email = driver.find_element(By.NAME, 'username')
email.send_keys(login_dict[0]['email'])

password = driver.find_element(By.NAME, 'password')
password.send_keys(login_dict[0]['password'])
password.send_keys(Keys.ENTER)

# time.sleep(3)

# access report portal and click previous report
cell_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div'
                                            '/div/div[4]/a')
cell_report.click()

previous_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div'
                                                '/div[1]/ul/li[1]/a')
previous_report.click()

# time.sleep(1)

view_report = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[5]/a')
view_report.click()

# time.sleep(2)

# Get previous report and put in a list
title_report = driver.find_elements(By.CLASS_NAME, 'col-sm-4')
number_reports = driver.find_elements(By.CLASS_NAME, 'col-sm-6')

title_list = []
for i in title_report[11:20]:
    title_list.append(i.text)
# print(len(title_list))
# print(title_list)

number_list = []
for i in number_reports[11:20]:
    number_list.append(i.text)
# print(len(number_list))
# print(number_list)

# report_dict = {}
# for n in range(len(title_list)):
#     report_dict[n] = {
#         'title': title_list[n],
#         'report': number_list[n]
#     }
# print(report_dict)
#
# previous_attendance = report_dict[12]['report']
# previous_first_timers = report_dict[13]['report']
# previous_new_converts = report_dict[14]['report']
# previous_holy_spirit = report_dict[15]['report']
# previous_church = report_dict[16]['report']
# previous_midweek = report_dict[17]['report']

# print(title_list)
# print(number_list)
print('Previous Report:')
input_attendance = int(input(f'{title_list[3]}: {number_list[3]}. Add = '))
input_first_timers = int(input(f'{title_list[4]}: {number_list[4]}. Add = '))
input_new_converts = int(input(f'{title_list[5]}: {number_list[5]}. Add = '))
input_holy_spirit = int(input(f'{title_list[6]}: {number_list[6]}. Add = '))
input_church = int(input(f'{title_list[7]}: {number_list[7]}. Add = '))
input_midweek = int(input(f'{title_list[8]}: {number_list[8]}. Add = '))
# input_date = input('What is the date of the cell meeting? (DD/MM/YY): ')
print('Working...')

# Add inputed integer to previous report
new_attendance = int(number_list[3]) + input_attendance
new_first_timers = int(number_list[4]) + input_first_timers
new_new_converts = int(number_list[5]) + input_new_converts
new_holy_spirit = int(number_list[6]) + input_holy_spirit
new_church = int(number_list[7]) + input_church
new_midweek = int(number_list[8]) + input_midweek

try:
    close_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div'
                                                 '/div/div[1]/div[2]/table/tbody/tr[1]/td[5]/div[2]/div/div/div'
                                                 '[1]/button')
    print(close_report.text)
    close_report.click()
except NoSuchElementException:
    # -------------Close Pop Up----------------
    not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
    not_necessary.click()
    # -------------Close Pop Up----------------
    time.sleep(1)
    close_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div'
                                                 '[1]/div[2]/table/tbody/tr[1]/td[5]/div[2]/div/div/div[1]/button')
    print(close_report.text)
    close_report.click()
except ElementClickInterceptedException:
    # -------------Close Pop Up----------------
    not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
    not_necessary.click()
    # -------------Close Pop Up----------------
    time.sleep(1)
    close_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div'
                                                 '[1]/div[2]/table/tbody/tr[1]/td[5]/div[2]/div/div/div[1]/button')
    print(close_report.text)
    close_report.click()
finally:
    # adding new report
    add_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div[1]/ul/'
                                               'li[2]/a')
    add_button.click()

    for num in range(3):
        if num == 0:
            type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                            '[2]/label/input')
            type_of_meeting.click()
            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('10')
        elif num == 1:
            type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                            '[3]/label')
            type_of_meeting.click()
            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('17')
        elif num == 2:
            type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                            '[4]/label')
            type_of_meeting.click()
            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('24')
        meeting_type = type_of_meeting.text

        # ---------------------------------------Time of meeting--------------------------------------------------
        start_time = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input1"]')
        start_time.click()

        start_hour = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div/div[8]')
        start_hour.click()

        start_pm = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[1]/div[4]/div[2]')
        start_pm.click()

        start_ok = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/table/tbody/tr/td[1]/a')
        start_ok.click()

        end_time = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input2"]')
        end_time.click()

        end_hour = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[9]')
        end_hour.click()

        end_pm = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[1]/div[4]/div[2]')
        end_pm.click()

        end_ok = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/table/tbody/tr/td[1]/a')
        end_ok.click()
        # --------------------------------------End time of meeting section---------------------------------------
        try:
            attendance = driver.find_element(By.NAME, 'CmisCellLeadersReport[1][total_no_at_bible_study]')
            attendance.send_keys(Keys.ARROW_RIGHT)
            attendance.send_keys(Keys.BACK_SPACE)
            attendance.send_keys(new_attendance)
        except ElementNotInteractableException:
            attendance = driver.find_element(By.NAME, 'CmisCellLeadersReport[total_no_at_cell_meeting]')
            attendance.send_keys(Keys.ARROW_RIGHT)
            attendance.send_keys(Keys.BACK_SPACE)
            attendance.send_keys(new_attendance)

        first_timers = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_first_timers]')
        first_timers.send_keys(Keys.ARROW_RIGHT)
        first_timers.send_keys(Keys.BACK_SPACE)
        first_timers.send_keys(new_first_timers)

        new_converts = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_new_converts]')
        new_converts.send_keys(Keys.ARROW_RIGHT)
        new_converts.send_keys(Keys.BACK_SPACE)
        new_converts.send_keys(new_new_converts)

        holy_spirit = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_infilling]')
        holy_spirit.send_keys(Keys.ARROW_RIGHT)
        holy_spirit.send_keys(Keys.BACK_SPACE)
        holy_spirit.send_keys(new_holy_spirit)

        midweek = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_wed_service]')
        midweek.send_keys(Keys.ARROW_RIGHT)
        midweek.send_keys(Keys.BACK_SPACE)
        midweek.send_keys(new_midweek)

        sunday_service = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_sun_service]')
        sunday_service.send_keys(Keys.ARROW_RIGHT)
        sunday_service.send_keys(Keys.BACK_SPACE)
        sunday_service.send_keys(new_church)

        testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
        testimony.send_keys(choice(testimony_list))

        # submit = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[13]/td[2]/input')
        # submit.click()
        print(f'Done for {meeting_type}')
    login_dict.pop(0)

# for n in range(len(login_dict)):
#     # driver.get('https://celfonline.org/V3/index.php?r=Site/Login')
#     print(f'Working on {login_dict[n + 1]["email"]}')
#
#     # Log out
#     log_out = driver.find_element(By.LINK_TEXT, 'Log out')
#     log_out.click()
#
#     # log in
#     email = driver.find_element(By.NAME, 'username')
#     email.send_keys(login_dict[n + 1]['email'])
#
#     password = driver.find_element(By.NAME, 'password')
#     password.send_keys(login_dict[n + 1]['password'])
#     password.send_keys(Keys.ENTER)
#
#     # Access report portal and click previous report
#     cell_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div'
#                                                 '/div/div[4]/a')
#     cell_report.click()
#
#     previous_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div'
#                                                     '/div[1]/ul/li[1]/a')
#     previous_report.click()
#
#     # time.sleep(1)
#
#     view_report = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[5]/a')
#     view_report.click()
#
#     # Get previous report and put in a list
#     title_report = driver.find_elements(By.CLASS_NAME, 'col-sm-4')
#     number_reports = driver.find_elements(By.CLASS_NAME, 'col-sm-6')
#
#     title_list = []
#     for i in title_report[11:20]:
#         title_list.append(i.text)
#
#     number_list = []
#     for i in number_reports[11:20]:
#         number_list.append(i.text)
#
#     # Add inputed integer to previous report
#     new_attendance = int(number_list[3]) + input_attendance
#     new_first_timers = int(number_list[4]) + input_first_timers
#     new_new_converts = int(number_list[5]) + input_new_converts
#     new_holy_spirit = int(number_list[6]) + input_holy_spirit
#     new_church = int(number_list[7]) + input_church
#     new_midweek = int(number_list[8]) + input_midweek
#
#     try:
#         close_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div'
#                                                      '/div/div[1]/div[2]/table/tbody/tr[1]/td[5]/div[2]/div/div/div'
#                                                      '[1]/button')
#         print(close_report.text)
#         close_report.click()
#     except NoSuchElementException:
#         # -------------Close Pop Up----------------
#         not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
#         not_necessary.click()
#         # -------------Close Pop Up----------------
#         time.sleep(1)
#         close_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div'
#                                                      '[1]/div[2]/table/tbody/tr[1]/td[5]/div[2]/div/div/div[1]/button')
#         print(close_report.text)
#         close_report.click()
#     except ElementClickInterceptedException:
#         # -------------Close Pop Up----------------
#         not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
#         not_necessary.click()
#         # -------------Close Pop Up----------------
#         time.sleep(1)
#         close_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div'
#                                                      '[1]/div[2]/table/tbody/tr[1]/td[5]/div[2]/div/div/div[1]/button')
#         print(close_report.text)
#         close_report.click()
#     finally:
#         # adding new report
#         add_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div[1]/ul/'
#                                                    'li[2]/a')
#         add_button.click()
#
#         for num in range(3):
#             type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div[2]'
#                                                             '/label/input')
#             type_of_meeting.click()
#             meeting_type = type_of_meeting.text
#
#             date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
#             date_of_meeting.send_keys('10')
#
#             # ---------------------------------------Time of meeting--------------------------------------------------
#             start_time = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input1"]')
#             start_time.click()
#
#             start_hour = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div/div[8]')
#             start_hour.click()
#
#             start_pm = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[1]/div[4]/div[2]')
#             start_pm.click()
#
#             start_ok = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/table/tbody/tr/td[1]/a')
#             start_ok.click()
#
#             end_time = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input2"]')
#             end_time.click()
#
#             end_hour = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/div/div[9]')
#             end_hour.click()
#
#             end_pm = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[1]/div[4]/div[2]')
#             end_pm.click()
#
#             end_ok = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/table/tbody/tr/td[1]/a')
#             end_ok.click()
#             # --------------------------------------End time of meeting section---------------------------------------
#
#             attendance = driver.find_element(By.NAME, 'CmisCellLeadersReport[1][total_no_at_bible_study]')
#             attendance.send_keys(Keys.ARROW_RIGHT)
#             attendance.send_keys(Keys.BACK_SPACE)
#             attendance.send_keys(new_attendance)
#
#             first_timers = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_first_timers]')
#             first_timers.send_keys(Keys.ARROW_RIGHT)
#             first_timers.send_keys(Keys.BACK_SPACE)
#             first_timers.send_keys(new_first_timers)
#
#             new_converts = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_new_converts]')
#             new_converts.send_keys(Keys.ARROW_RIGHT)
#             new_converts.send_keys(Keys.BACK_SPACE)
#             new_converts.send_keys(new_new_converts)
#
#             holy_spirit = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_infilling]')
#             holy_spirit.send_keys(Keys.ARROW_RIGHT)
#             holy_spirit.send_keys(Keys.BACK_SPACE)
#             holy_spirit.send_keys(new_holy_spirit)
#
#             midweek = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_wed_service]')
#             midweek.send_keys(Keys.ARROW_RIGHT)
#             midweek.send_keys(Keys.BACK_SPACE)
#             midweek.send_keys(new_midweek)
#
#             sunday_service = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_sun_service]')
#             sunday_service.send_keys(Keys.ARROW_RIGHT)
#             sunday_service.send_keys(Keys.BACK_SPACE)
#             sunday_service.send_keys(new_church)
#
#             testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
#             testimony.send_keys(choice(testimony_list))
#
#             # submit = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[13]/td[2]/input')
#             # submit.click()
#             print(f'Done for {meeting_type}')
#
#         print(f'Done for {login_dict[n + 1]["email"]}. Moving on to next Log In...')
# driver.quit()
