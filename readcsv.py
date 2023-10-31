import pandas

pd = pandas.read_csv('LOG INS - Sheet1.csv')
emails = pd.to_dict()['email']
passwords = pd.to_dict()['password']
# kc = pd.to_dict()['kc']

login_dict = {}
for i in range(len(emails)):
    login_dict[i] = {
        'email': emails[i],
        'password': passwords[i],
        # 'kc': kc[i]
    }

print(login_dict[0]['email'])
print(login_dict[0])
# login_dict.pop(0)
# for n in range(len(login_dict)):
#     print(login_dict[n])
#     print('Done')
