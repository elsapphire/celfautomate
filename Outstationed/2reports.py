from random import choice

import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException

pd = pandas.read_csv('Karimo-dape-jiwa - Sheet1.csv')
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
                  'It was an awesome time studying the word and sharing our thoughts.', 'It was an exciting meeting.',
                  'We were blessed', 'We celebrated a birthday']

prayer_planning_testimony = ['We prayed and planned of the growth of the cell', 'We prayed and planned.',
                             'We took out time to pray and plan for the growth of the cell in the month']

cell_crusade_testimony = [
    "The movie outreach was a blessing to all",
    "It was a glorious global day of service",
    "Evangelism from door to door... Glory to God"
]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://celfonline.org/V3/index.php?r=Site/Login')

# previous_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div'
#                                                 '/div[1]/ul/li[1]/a')
# previous_report.click()
#
# # time.sleep(1)
#
# view_report = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[5]/a')
# view_report.click()
#
# # time.sleep(2)
#
# # Get previous report and put in a list
# title_report = driver.find_elements(By.CLASS_NAME, 'col-sm-4')
# number_reports = driver.find_elements(By.CLASS_NAME, 'col-sm-6')
# title_list = []
# for i in title_report[11:20]:
#     title_list.append(i.text)
# # print(len(title_list))
# # print(title_list)
# number_list = []
# for i in number_reports[11:20]:
#     number_list.append(i.text)
# print(title_list)
# print(number_list)
# print('Previous Report:')
# previous_attendance = int(number_list[3])
# previous_first_timers = int(number_list[4])
# previous_new_converts = int(number_list[5])
# previous_holy_spirit = int(number_list[6])
# previous_church = int(number_list[7])
# previous_midweek = int(number_list[8])
# input_date = input('What is the date of the cell meeting? (DD/MM/YY): ')

# try:
#     close_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div'
#                                                  '/div/div[1]/div[2]/table/tbody/tr[1]/td[5]/div[2]/div/div/div'
#                                                  '[1]/button')
#     print(close_report.text)
#     close_report.click()
# except NoSuchElementException:
#     # -------------Close Pop Up----------------
#     not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
#     not_necessary.click()
#     # -------------Close Pop Up----------------
#     time.sleep(1)
#     close_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div'
#                                                  '[1]/div[2]/table/tbody/tr[1]/td[5]/div[2]/div/div/div[1]/button')
#     print(close_report.text)
#     close_report.click()
# except ElementClickInterceptedException:
#     # -------------Close Pop Up----------------
#     not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
#     not_necessary.click()
#     # -------------Close Pop Up----------------
#     time.sleep(1)
#     close_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div'
#                                                  '[1]/div[2]/table/tbody/tr[1]/td[5]/div[2]/div/div/div[1]/button')
#     print(close_report.text)
#     close_report.click()
# finally:
#     # adding new report
#     add_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div[1]/ul/'
#                                                'li[2]/a')
#     add_button.click()

for n in range(len(login_dict)):
    print(f'Working on {login_dict[n]["email"]}')
    # log in
    email = driver.find_element(By.NAME, 'username')
    email.send_keys(login_dict[n]['email'])

    password = driver.find_element(By.NAME, 'password')
    password.send_keys(login_dict[n]['password'])
    password.send_keys(Keys.ENTER)

    # time.sleep(3)
    cell_report = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div'
                                                '/div/div[4]/a')
    cell_report.click()
    for num in range(2):
        # --------Cell Outreach---------
        if num == 0:
            try:
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div'
                                                                '/div[4]/label/input')
                type_of_meeting.click()
            except ElementClickInterceptedException:
                # -------------Close Pop Up----------------
                not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
                not_necessary.click()
                # -------------Close Pop Up----------------
                type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div'
                                                                '/div[4]/label/input')
                type_of_meeting.click()

            date_of_meeting = driver.find_element(By.NAME, 'CmisCellLeadersReport[date_of_meeting]')
            date_of_meeting.click()
            date_of_meeting.send_keys('2511')

            new_attendance = choice(list(range(80, 96)))
            new_first_timers = choice(list(range(14, 20)))
            new_new_converts = choice([new_first_timers - 3, new_first_timers - 4, new_first_timers - 5])
            new_holy_spirit = choice([new_new_converts - 2, new_new_converts - 3])
            new_midweek = choice(list(range(15, 23)))
            new_church = choice(list(range(21, 32)))

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.clear()
            testimony.send_keys(choice(cell_crusade_testimony))
            meeting_type = 'Cell Outreach'

        # --------Prayer and Planning------------------
        elif num == 1:
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

            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.send_keys('0212')

            new_attendance = choice(list(range(88, 107)))
            new_first_timers = choice(list(range(15, 20)))
            new_new_converts = choice([new_first_timers - 2, new_first_timers - 3, new_first_timers - 4,
                                       new_first_timers - 5])
            new_holy_spirit = choice([new_new_converts - 2, new_new_converts - 3])
            new_midweek = choice(list(range(14, 23)))
            new_church = choice(list(range(19, 31)))

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.clear()
            testimony.send_keys(choice(prayer_planning_testimony))
            meeting_type = 'Prayer and Planning'

        # ---------------------------------------Time of meeting--------------------------------------------------
        try:
            start_time = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input1"]')
            start_time.click()

            start_hour = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/div[8]')
            start_hour.click()

            start_pm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[4]/div[2]')
            start_pm.click()

            start_ok = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr/td[1]/a')
            start_ok.click()

            end_time = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input2"]')
            end_time.click()

            end_hour = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div/div[9]')
            end_hour.click()

            end_pm = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[1]/div[4]/div[2]')
            end_pm.click()

            end_ok = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/table/tbody/tr/td[1]/a')
            end_ok.click()
        except ElementClickInterceptedException:
            # -------------Close Pop Up----------------
            not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
            not_necessary.click()
            # -------------Close Pop Up----------------
            start_time = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input1"]')
            start_time.click()

            start_hour = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/div[8]')
            start_hour.click()

            start_pm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[4]/div[2]')
            start_pm.click()

            start_ok = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr/td[1]/a')
            start_ok.click()

            end_time = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input2"]')
            end_time.click()

            end_hour = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div/div[9]')
            end_hour.click()

            end_pm = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[1]/div[4]/div[2]')
            end_pm.click()

            end_ok = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/table/tbody/tr/td[1]/a')
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
        print(f'Done for {meeting_type}')
    print(f'Done for {login_dict[n]["email"]}. Number {n + 1}/{len(login_dict)}. \nLogging Out...')

    try:
        # Log out
        log_out = driver.find_element(By.LINK_TEXT, 'Log out')
        log_out.click()
    except ElementClickInterceptedException:
        # -------------Close Pop Up----------------
        not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
        not_necessary.click()
        # Log out
        log_out = driver.find_element(By.LINK_TEXT, 'Log out')
        log_out.click()

print(f'Completed. Submitted reports for {len(login_dict)} accounts')
driver.quit()
