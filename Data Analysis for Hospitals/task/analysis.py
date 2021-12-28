# write your code here
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

prenatal.rename(columns={'Sex': 'gender', 'HOSPITAL': 'hospital'}, inplace=True)
sports.rename(columns={'Male/female': 'gender', 'Hospital': 'hospital'}, inplace=True)

df = pd.concat([general, prenatal, sports], ignore_index=True)
df.drop(columns=['Unnamed: 0'], inplace=True)

df.dropna(how='all', inplace=True)

df.loc[df['gender'] == 'male', 'gender'] = 'm'
df.loc[df['gender'] == 'man', 'gender'] = 'm'
df.loc[df['gender'] == 'female', 'gender'] = 'f'
df.loc[df['gender'] == 'woman', 'gender'] = 'f'

df['gender'].fillna('f', inplace=True)
df['bmi'].fillna('0', inplace=True)
df['diagnosis'].fillna('0', inplace=True)
df['blood_test'].fillna('0', inplace=True)
df['ecg'].fillna('0', inplace=True)
df['ultrasound'].fillna('0', inplace=True)
df['mri'].fillna('0', inplace=True)
df['xray'].fillna('0', inplace=True)
df['children'].fillna('0', inplace=True)
df['months'].fillna('0', inplace=True)

# Stage 4/5
# print('The answer to the 1st question is {}'.format(df.pivot_table(index='hospital', aggfunc='count').index[0]))
#
# diagnosis = df.pivot_table(index='hospital', columns='diagnosis', values='age', aggfunc='count')
# print('The answer to the 2nd question is {}'.format(round(diagnosis.loc['df', 'stomach'] / diagnosis.loc['df'].sum(), 3)))
# print('The answer to the 3rd question is {}'.format(round(diagnosis.loc['sports', 'dislocation'] / diagnosis.loc['sports'].sum(), 3)))
#
# median_age = df.groupby('hospital')[['hospital', 'age']].agg('median')
# print('The answer to the 4th question is {}'.format(int(median_age.loc['df'] - median_age.loc['sports'])))
#
# max_tests = df.pivot_table(index='hospital', columns='blood_test', values='age', aggfunc='count')
# print('The answer to the 5th question is {}, {} blood tests'.format(max_tests.t.idxmax(), int(max_tests.t.max())))

# Stage 5/5
df.plot(y='age', kind='hist', bins=6)
plt.show()
print('The answer to the 1st question: 15-35')
df['diagnosis'].value_counts().plot(kind='pie')
plt.show()
print('The answer to the 2nd question: pregnancy')
fig, axes = plt.subplots()
df['diagnosis'].value_counts().plot(kind='pie')
print("The answer to the 3rd question: It's because the plot wont show up")

plt.show()
