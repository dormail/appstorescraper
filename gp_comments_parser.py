# a function parsing the html code from google play comments into a 
# pandas data frame
import pandas as pd

def gp_comments_parser(source):
    tmp = {'stars': [], 'date': [], 'content': [], 'likes': []}
    result = pd.DataFrame(data = tmp)

    return result
