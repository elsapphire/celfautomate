# import time
from random import choice

import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

pd = pandas.read_csv('zc compiled - Sheet2.csv')
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

cell_crusade_testimony = [
    "The movie outreach was a blessing to all",
    "It was a glorious global day of service",
    "Evangelism from door to door... Glory to God"
]

new_testimony = [
    'We split the cell into two, prayed and planned for the growth of the cell.',
    'We prayed and planned for the growth of the cell and church.',
    'We spent time praying and planning for the growth of the cell.',
    'It was an amazing meeting, the cell split and we prayed and planned for the growth of the cell.'
]

bible_study = [
    'We were blessed studying the Word of God',
    'It was an awesome time being taught by The Word',
    'We had a glorious time, we celebrated a birthday',
]

# proxy_server_url = '198.199.86.11'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
# chrome_options.add_argument(f'--proxy-server={proxy_server_url}')

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://celfonline.org/V3/index.php?r=Site/Login')
problem_logins = {'email': [], 'password': []}
for n in range(len(login_dict)):
    print(f'Working on {login_dict[n]["email"]}')
    # log in
    email = driver.find_element(By.NAME, 'username')
    email.send_keys(login_dict[n]['email'])

    password = driver.find_element(By.NAME, 'password')
    password.send_keys(login_dict[n]['password'])
    password.send_keys(Keys.ENTER)

    # check if account is a cell leader
    # access report portal and click previous report
    try:
        cell_report = driver.find_element(By.LINK_TEXT, 'Submit Cell Reports')
    except NoSuchElementException:
        print(f'Problem with {login_dict[n]["email"]}. Number {n + 1}/{len(login_dict)}. \nLogging Out...')
        problem_logins['email'].append(login_dict[n]['email'])
        problem_logins['password'].append(login_dict[n]['password'])

        df = pandas.DataFrame(problem_logins)
        df.to_csv('problem_logs.csv')

        try:
            log_out = driver.find_element(By.LINK_TEXT, 'Log out')
            log_out.click()
            # log_out = driver.find_element(By.LINK_TEXT, 'LOGOUT')
            # log_out.click()
        except NoSuchElementException:
            # log_out = driver.find_element(By.LINK_TEXT, 'Log out')
            # log_out.click()

            email = driver.find_element(By.NAME, 'username')

    else:
        cell_report.click()

        # --------ADDING THE REPORTS---------
        try:
            type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div'
                                                            '/div[2]/label/input')
            type_of_meeting.click()
        except ElementClickInterceptedException:
            # -------------Close Pop Up----------------
            not_necessary = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
            not_necessary.click()
            # -------------Close Pop Up----------------
            type_of_meeting = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[1]/td[2]/div'
                                                            '/div[1]/label/input')
            type_of_meeting.click()
        except NoSuchElementException:
            print(f'Problem with {login_dict[n]["email"]}. Number {n + 1}/{len(login_dict)}. \nLogging Out...')
            problem_logins['email'].append(login_dict[n]['email'])
            problem_logins['password'].append(login_dict[n]['password'])

            df = pandas.DataFrame(problem_logins)
            df.to_csv('problem_logs.csv')

            log_out = driver.find_element(By.LINK_TEXT, 'Log out')
            log_out.click()
        else:
            date_of_meeting = driver.find_element(By.ID, 'CmisCellLeadersReport_date_of_meeting')
            date_of_meeting.click()
            date_of_meeting.send_keys('09')

            new_attendance = choice(list(range(47, 66)))
            new_first_timers = choice(list(range(10, 16)))
            new_new_converts = choice([new_first_timers - 3, new_first_timers - 4])
            new_holy_spirit = choice([new_new_converts - 2, new_new_converts - 3, new_new_converts - 4])

            new_midweek = choice(list(range(10, 21)))
            new_church = choice(list(range(18, 32)))

            attendance = driver.find_element(By.NAME, 'CmisCellLeadersReport[1][total_no_at_bible_study]')
            attendance.clear()
            attendance.send_keys(new_attendance)

            testimony = driver.find_element(By.NAME, 'CmisCellLeadersReport[testimony]')
            testimony.clear()
            testimony.send_keys(choice(bible_study))

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

            # -----------------------------------Time of meeting----------------------------------------------
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
            # ----------------------------------End time of meeting section------------------------------------

            submit = driver.find_element(By.XPATH, '//*[@id="fixed-table2"]/tbody/tr[13]/td[2]/input')
            submit.click()
            # time.sleep(1)
            print(f'Done for {login_dict[n]["email"]}. Number {n + 1}/{len(login_dict)}. \nLogging Out...')

            # Log out
            log_out = driver.find_element(By.LINK_TEXT, 'Log out')
            log_out.click()

print(f'Completed. Submitted reports for {len(login_dict) - len(problem_logins["email"])} accounts')

df = pandas.DataFrame(problem_logins)
# print(df)
df.to_csv('problem_logs.csv')
driver.quit()
