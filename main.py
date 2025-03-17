import pandas as pd 
import re
from wordcloud import STOPWORDS, WordCloud
import matplotlib.pyplot as plt

df = pd.read_excel('Spark! Civic Tech Expo Feedback Form for Students (Responses).xlsx')

def first_returning(df):
    '''finds how many people are returning to the hackathon and how many are new'''


    returning = df['Before this event, had you previously taken part in a hackathon of any kind?'].value_counts()['Yes']
    new = df['Before this event, had you previously taken part in a hackathon of any kind?'].value_counts()['No']
    return returning, new

def motivation_analysis(df):
    '''Returns the counts of the primary motivations for attending the hackathon'''


    # TODO: make a pie chart of the motivations
    motivation = df['What was your primary motivation for attending this hackathon (choose top reason)'].value_counts()
    return motivation

def motivation_satisfaction_trend(df):
    '''Finds the average rating of the hackathon based on the primary motivation of the participant'''


    improve = df[df['What was your primary motivation for attending this hackathon (choose top reason)'] == 'Improve skills']
    engage = df[df['What was your primary motivation for attending this hackathon (choose top reason)'] == 'Engaging in civic tech']
    exposure = df[df['What was your primary motivation for attending this hackathon (choose top reason)'] == 'Get exposure to employers']
    fun = df[df['What was your primary motivation for attending this hackathon (choose top reason)'] == 'Have fun']
    attempt = df[df['What was your primary motivation for attending this hackathon (choose top reason)'] == 'Just to try hackathons']
    learn = df[df['What was your primary motivation for attending this hackathon (choose top reason)'] == 'Learn from participants']

    # see how the reasoning for someone coming to the hackathon affects their satisfaction 
    imrpove_satisfaction = improve['Overall, how would you rate this hackathon?'].mean()
    engage_satisfaction = engage['Overall, how would you rate this hackathon?'].mean()
    exposure_satisfaction = exposure['Overall, how would you rate this hackathon?'].mean()
    fun_satisfaction = fun['Overall, how would you rate this hackathon?'].mean()
    attempt_satisfaction = attempt['Overall, how would you rate this hackathon?'].mean()
    learn_satisfaction = learn['Overall, how would you rate this hackathon?'].mean()
    print('Improve skills:', imrpove_satisfaction)
    print('Engage in civic tech:', engage_satisfaction)
    print('Get exposure to employers:', exposure_satisfaction)
    print('Have fun:', fun_satisfaction)
    print('Just to try hackathons:', attempt_satisfaction)
    print('Learn from participants:', learn_satisfaction)


    return imrpove_satisfaction, engage_satisfaction, exposure_satisfaction, fun_satisfaction, attempt_satisfaction, learn_satisfaction

def avg_rating_by_category(df):
    '''finds the average rating of each of the catagories in the feedback form'''

    # TODO: make a stacked bar chart of the ratings

    for col in df.columns[5:17]:
        print(col,'\n',df[col].value_counts())


def word_cloud(df,col):
    '''creates a word cloud of the feedback comments'''
    dummy = df
    stopwords = set(STOPWORDS)
    otherwords = ['well','good','great','like','really', 'getting', 'lot', 'new', 'things', 'thing', 'time', 'fun', 
                  'hackathon', 'hackathons', 'part', 'participate', 'participated', 'participating', 'participation', 
                  'participate', 'participated', 'participating', 'participation', 'participate', 'participated', 'participating', 
                  'participation', 'participate', 'participated', 'participating', 'participation', 'participate', 'participated', 
                  'participating', 'participation', 'participate', 'participated', 'participating', 'participation', 'participate', 
                  'participated', 'participating', 'participation', 'participate', 'participated', 'participating', 'participation', 
                  'participate', 'participated', 'participating', 'participation', 'participate', 'participated', 'participating', 
                  'participation', 'participate', 'participated', 'participating', 'participation', 'participate', 'participated', 
                  'participating', 'participation', 'meeting', 'something','think','went','loved','work','overall','helpful', 'didn',
                  'felt', 'bit', 'better', 'us', 'enough', 'wish', 'maybe', 't', 'less', 'given','know']
    for word in otherwords:
        stopwords.add(word)
    text = ''
    # clean the text
    for review in dummy[col]: 
        if pd.isna(review):
            continue
        # remove punctuation and numbers
        review = re.sub('[^a-zA-Z]', ' ', review)
        # lowercase 
        review = review.lower()
        # remove stopwords
        review = ' '.join([word for word in review.split() if word not in stopwords]) 
        
        # add it to the text
        text += review + ' '
    
    # make the wordclous 
    wordcloud = WordCloud(width = 800, height = 800, background_color='white', max_words=20).generate(text)

    plt.figure(figsize = (8, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title(col)
    plt.show()

# print(motivation_analysis(df))
# print(motivation_satisfaction_trend(df))
# print(avg_rating_by_category(df))
# word_cloud(df,'What went well?\nWhat were your favorite parts about this hackathon?')
word_cloud(df,"What didn't go well? How can we improve your hackathon experience? \nWhat changes would have made the hackathon and/or your project better? Was there anything that you would have liked to see?")
