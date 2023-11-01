import time
from random import choice

import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException

pd = pandas.read_csv('CECLF ')
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

# print(title_list)
# print(number_list)
print('Previous Report:')
previous_attendance = int(number_list[3])
previous_first_timers = int(number_list[4])
previous_new_converts = int(number_list[5])
previous_holy_spirit = int(number_list[6])
previous_church = int(number_list[7])
previous_midweek = int(number_list[8])
# input_date = input('What is the date of the cell meeting? (DD/MM/YY): ')
print('Working...')


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

    for num in range(4):
        # --------Prayer and Planning---------
        if num == 0:
            try:
                type_of_meeting = driver.find_element(By.NAME, 'CmisCellLeadersReport[type_of_meeting]')
                type_of_meeting.click()
            except ElementClickInterceptedException:
                # -------------Close Pop Up----------------
                not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
                not_necessary.click()
                # -------------Close Pop Up----------------
                type_of_meeting = driver.find_element(By.NAME, 'CmisCellLeadersReport[type_of_meeting]')
                type_of_meeting.click()

            date_of_meeting = driver.find_element(By.NAME, 'CmisCellLeadersReport[date_of_meeting]')
            date_of_meeting.click()
            date_of_meeting.send_keys('0610')

            if previous_attendance >= 55:
                new_attendance = previous_attendance + 4
                new_first_timers = choice([4, 5, 6, 7, 8, 9, 10, 11, 12])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([5, 6, 7, 8, 9])
                new_church = choice([20, 21, 22, 23, 24, 25])
            elif 40 < previous_attendance <= 54:
                num_to_add = choice([4, 5])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([11, 12, 13, 14, 15])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([4, 5, 6, 7])
                new_church = choice([15, 16, 17, 18, 19, 20])
            elif 20 < previous_attendance <= 40:
                num_to_add = choice([6, 7])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([5, 6, 7, 8])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([8, 9, 10, 11, 12, 13])
            elif previous_attendance <= 20:
                num_to_add = choice([8, 9])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6, 7])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([3, 4, 5, 6])
                new_church = choice([8, 9, 10, 11])

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.clear()
            testimony.send_keys('We prayed and planned for the growth of the cell.')

        # --------Bible Study 1------------------
        elif num == 1:
            try:
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[2]/label/input')
                type_of_meeting.click()
            except ElementClickInterceptedException:
                # -------------Close Pop Up----------------
                not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
                not_necessary.click()
                # -------------Close Pop Up----------------
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[2]/label/input')
                type_of_meeting.click()

            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('1310')

            if previous_attendance >= 55:
                new_attendance = previous_attendance + 17
                new_first_timers = choice([4, 5, 6, 7, 8, 9, 10, 11, 12])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([6, 7, 8, 9, 10])
                new_church = choice([22, 23, 24, 25, 26, 27])
            elif 40 < previous_attendance <= 54:
                num_to_add = choice([8, 9])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([13, 14, 15, 16, 17])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([9, 10, 11, 12, 13])
                new_church = choice([27, 28, 29, 30, 31, 32])
            elif 20 < previous_attendance <= 40:
                num_to_add = choice([4, 5])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([6, 7, 8, 9, 10])
            elif previous_attendance <= 20:
                num_to_add = choice([2, 3])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([6, 7, 8, 9])

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.clear()
            testimony.send_keys(choice(testimony_list))

        # --------Bible Study 2------------------
        elif num == 2:
            try:
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[3]/label')
                type_of_meeting.click()
            except ElementClickInterceptedException:
                # -------------Close Pop Up----------------
                not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
                not_necessary.click()
                # -------------Close Pop Up----------------
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[3]/label')
                type_of_meeting.click()

            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('2010')

            if previous_attendance >= 55:
                new_attendance = previous_attendance + 18
                new_first_timers = choice([5, 6, 7, 8, 9, 10, 11, 12])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([6, 7, 8, 9, 10])
                new_church = choice([22, 23, 24, 25, 26, 27])
            elif 40 < previous_attendance <= 54:
                num_to_add = choice([7, 8])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([13, 14, 15, 16, 17])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([9, 10, 11, 12, 13])
                new_church = choice([27, 28, 29, 30, 31, 32])
            elif 20 < previous_attendance <= 40:
                num_to_add = choice([4, 5])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([6, 7, 8, 9, 10])
            elif previous_attendance <= 20:
                num_to_add = choice([1, 2, 3])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([6, 7, 8, 9])

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.clear()
            testimony.send_keys(choice(testimony_list))

        # --------Cell Outreach------------------
        elif num == 3:
            try:
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[4]/label')
                type_of_meeting.click()
            except ElementClickInterceptedException:
                # -------------Close Pop Up----------------
                not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
                not_necessary.click()
                # -------------Close Pop Up----------------
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[4]/label')
                type_of_meeting.click()
            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('2710')

            if previous_attendance >= 55:
                new_attendance = previous_attendance + 76
                numbers = list(range(80, 121))
                new_first_timers = choice(numbers)
                new_new_converts = new_first_timers - 22
                new_holy_spirit = new_new_converts
                new_midweek = choice(list(range(6, 13)))
                new_church = choice(list(range(40, 61)))
            elif 40 < previous_attendance <= 54:
                num_to_add = choice(list(range(36, 38)))
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice(list(range(27, 38)))
                new_new_converts = new_first_timers - 11
                new_holy_spirit = new_new_converts
                new_midweek = choice(list(range(11, 18)))
                new_church = choice(list(range(33, 49)))
            elif 20 < previous_attendance <= 40:
                num_to_add = choice(list(range(20, 34)))
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice(list(range(10, 18)))
                new_new_converts = new_first_timers - 3
                new_holy_spirit = new_new_converts
                new_midweek = choice(list(range(7, 16)))
                new_church = choice(list(range(20, 27)))
            elif previous_attendance <= 20:
                num_to_add = choice(list(range(15, 17)))
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice(list(range(9, 16)))
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice(list(range(9, 12)))
                new_church = choice(list(range(16, 24)))

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.click()
            testimony.clear()
            testimony.send_keys('It was an amazing outreach. We hosted the Healing Streams Live Healing Service.')
        meeting_type = type_of_meeting.text

        # ---------------------------------------Time of meeting--------------------------------------------------
        try:
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
        except ElementClickInterceptedException:
            # -------------Close Pop Up----------------
            not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
            not_necessary.click()
            # -------------Close Pop Up----------------
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
            attendance.clear()
            attendance.send_keys(new_attendance)
        except ElementNotInteractableException:
            attendance = driver.find_element(By.NAME, 'CmisCellLeadersReport[total_no_at_cell_meeting]')
            attendance.clear()
            attendance.send_keys(new_attendance)

        first_timers = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_first_timers]')
        first_timers.clear()
        first_timers.send_keys(new_first_timers)

        new_converts = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_new_converts]')
        new_converts.clear()
        new_converts.send_keys(new_new_converts)

        holy_spirit = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_infilling]')
        holy_spirit.clear()
        holy_spirit.send_keys(new_holy_spirit)

        midweek = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_wed_service]')
        midweek.clear()
        midweek.send_keys(new_midweek)

        sunday_service = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_sun_service]')
        sunday_service.clear()
        sunday_service.send_keys(new_church)

        submit = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[13]/td[2]/input')
        submit.click()
        time.sleep(1)
        print(f'Done for {meeting_type}')
    print(f'Done for {login_dict[0]["email"]}')
    login_dict.pop(0)

# ---- for loop starts -----------------
for n in range(len(login_dict)):
    print(f'Working on {login_dict[n + 1]["email"]}')

    # Log out
    log_out = driver.find_element(By.LINK_TEXT, 'Log out')
    log_out.click()

    # log in
    email = driver.find_element(By.NAME, 'username')
    email.send_keys(login_dict[n + 1]['email'])

    password = driver.find_element(By.NAME, 'password')
    password.send_keys(login_dict[n + 1]['password'])
    password.send_keys(Keys.ENTER)

    # Access report portal
    cell_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div'
                                                '/div/div[4]/a')
    cell_report.click()

    # ------- add - report ----------
    for num in range(4):
        # --------Prayer and Planning---------
        if num == 0:
            try:
                type_of_meeting = driver.find_element(By.NAME, 'CmisCellLeadersReport[type_of_meeting]')
                type_of_meeting.click()
            except ElementClickInterceptedException:
                # -------------Close Pop Up----------------
                not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
                not_necessary.click()
                # -------------Close Pop Up----------------
                type_of_meeting = driver.find_element(By.NAME, 'CmisCellLeadersReport[type_of_meeting]')
                type_of_meeting.click()

            date_of_meeting = driver.find_element(By.NAME, 'CmisCellLeadersReport[date_of_meeting]')
            date_of_meeting.click()
            date_of_meeting.send_keys('0610')

            if previous_attendance >= 55:
                new_attendance = previous_attendance + 4
                new_first_timers = choice([4, 5, 6, 7, 8, 9, 10, 11, 12])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([5, 6, 7, 8, 9])
                new_church = choice([20, 21, 22, 23, 24, 25])
            elif 40 < previous_attendance <= 54:
                num_to_add = choice([4, 5])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([11, 12, 13, 14, 15])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([4, 5, 6, 7])
                new_church = choice([15, 16, 17, 18, 19, 20])
            elif 20 < previous_attendance <= 40:
                num_to_add = choice([6, 7])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([5, 6, 7, 8])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([8, 9, 10, 11, 12, 13])
            elif previous_attendance <= 20:
                num_to_add = choice([8, 9])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6, 7])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([3, 4, 5, 6])
                new_church = choice([8, 9, 10, 11])

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.clear()
            testimony.send_keys('We prayed and planned for the growth of the cell.')

        # --------Bible Study 1------------------
        elif num == 1:
            try:
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[2]/label/input')
                type_of_meeting.click()
            except ElementClickInterceptedException:
                # -------------Close Pop Up----------------
                not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
                not_necessary.click()
                # -------------Close Pop Up----------------
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[2]/label/input')
                type_of_meeting.click()

            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('1310')

            if previous_attendance >= 55:
                new_attendance = previous_attendance + 17
                new_first_timers = choice([4, 5, 6, 7, 8, 9, 10, 11, 12])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([6, 7, 8, 9, 10])
                new_church = choice([22, 23, 24, 25, 26, 27])
            elif 40 < previous_attendance <= 54:
                num_to_add = choice([8, 9])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([13, 14, 15, 16, 17])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([9, 10, 11, 12, 13])
                new_church = choice([27, 28, 29, 30, 31, 32])
            elif 20 < previous_attendance <= 40:
                num_to_add = choice([4, 5])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([6, 7, 8, 9, 10])
            elif previous_attendance <= 20:
                num_to_add = choice([2, 3])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([6, 7, 8, 9])

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.clear()
            testimony.send_keys(choice(testimony_list))

        # --------Bible Study 2------------------
        elif num == 2:
            try:
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[3]/label')
                type_of_meeting.click()
            except ElementClickInterceptedException:
                # -------------Close Pop Up----------------
                not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
                not_necessary.click()
                # -------------Close Pop Up----------------
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[3]/label')
                type_of_meeting.click()

            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('2010')

            if previous_attendance >= 55:
                new_attendance = previous_attendance + 18
                new_first_timers = choice([5, 6, 7, 8, 9, 10, 11, 12])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([6, 7, 8, 9, 10])
                new_church = choice([22, 23, 24, 25, 26, 27])
            elif 40 < previous_attendance <= 54:
                num_to_add = choice([7, 8])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([13, 14, 15, 16, 17])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([9, 10, 11, 12, 13])
                new_church = choice([27, 28, 29, 30, 31, 32])
            elif 20 < previous_attendance <= 40:
                num_to_add = choice([4, 5])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([6, 7, 8, 9, 10])
            elif previous_attendance <= 20:
                num_to_add = choice([1, 2, 3])
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice([3, 4, 5, 6])
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice([2, 3, 4, 5])
                new_church = choice([6, 7, 8, 9])

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.clear()

            testimony.send_keys(choice(testimony_list))

            # --------Cell Outreach------------------
        elif num == 3:
            try:
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[4]/label')
                type_of_meeting.click()
            except ElementClickInterceptedException:
                # -------------Close Pop Up----------------
                not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
                not_necessary.click()
                # -------------Close Pop Up----------------
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div/div'
                                                                '[4]/label')
                type_of_meeting.click()
            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('2710')

            if previous_attendance >= 55:
                new_attendance = previous_attendance + 76
                numbers = list(range(80, 121))
                new_first_timers = choice(numbers)
                new_new_converts = new_first_timers - 22
                new_holy_spirit = new_new_converts
                new_midweek = choice(list(range(6, 13)))
                new_church = choice(list(range(40, 61)))
            elif 40 < previous_attendance <= 54:
                num_to_add = choice(list(range(36, 38)))
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice(list(range(27, 38)))
                new_new_converts = new_first_timers - 11
                new_holy_spirit = new_new_converts
                new_midweek = choice(list(range(11, 18)))
                new_church = choice(list(range(33, 49)))
            elif 20 < previous_attendance <= 40:
                num_to_add = choice(list(range(20, 34)))
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice(list(range(10, 18)))
                new_new_converts = new_first_timers - 3
                new_holy_spirit = new_new_converts
                new_midweek = choice(list(range(7, 16)))
                new_church = choice(list(range(20, 27)))
            elif previous_attendance <= 20:
                num_to_add = choice(list(range(15, 17)))
                new_attendance = previous_attendance + num_to_add
                new_first_timers = choice(list(range(9, 16)))
                new_new_converts = new_first_timers - 2
                new_holy_spirit = new_new_converts
                new_midweek = choice(list(range(9, 12)))
                new_church = choice(list(range(16, 24)))

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.click()
            testimony.clear()
            testimony.send_keys('It was an amazing outreach. We hosted the Healing Streams Live Healing Service.')
        meeting_type = type_of_meeting.text

        # ---------------------------------------Time of meeting--------------------------------------------------
        try:
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
        except ElementClickInterceptedException:
            # -------------Close Pop Up----------------
            not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
            not_necessary.click()
            # -------------Close Pop Up----------------
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
            attendance.clear()
            attendance.send_keys(new_attendance)
        except ElementNotInteractableException:
            attendance = driver.find_element(By.NAME, 'CmisCellLeadersReport[total_no_at_cell_meeting]')
            attendance.clear()
            attendance.send_keys(new_attendance)

        first_timers = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_first_timers]')
        first_timers.clear()
        first_timers.send_keys(new_first_timers)

        new_converts = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_new_converts]')
        new_converts.clear()
        new_converts.send_keys(new_new_converts)

        holy_spirit = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_infilling]')
        holy_spirit.clear()
        holy_spirit.send_keys(new_holy_spirit)

        midweek = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_wed_service]')
        midweek.clear()
        midweek.send_keys(new_midweek)

        sunday_service = driver.find_element(By.NAME, 'CmisCellLeadersReport[no_of_members_at_sun_service]')
        sunday_service.clear()
        sunday_service.send_keys(new_church)

        submit = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[13]/td[2]/input')
        submit.click()
        time.sleep(1)
        print(f'Done for {meeting_type}')

    print(f'Done for {login_dict[n + 1]["email"]}. Moving on to next Log In...')
driver.quit()
