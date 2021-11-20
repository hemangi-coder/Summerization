import streamlit as st
from Summerization_Url import *
from Summerization_article import *


def main():

    #st.title("Machine Learning Based Employee Layoff Prediction")

    activities = ["Summerization by URL", "Paste Article"]
    choice = st.sidebar.selectbox("How do you wish to check Status", activities)

    if choice == 'Summerization by URL':
        url = st.text_input('Input News URL')
        summary_length = st.text_input('No. of bullet points')
        if st.button("Get Summary"):
            dict_str = summerize_by_url(url, summary_length)
            st.header(dict_str['title'])
            l = dict_str['summary'][0]['sentences']
            for i in l:
                st.write(i)
    else:
        text1 = st.text_area('Paste Article')
        title1 = st.text_input('Title')
        summary_length1 = st.text_input('No. of bullets points')
        if st.button("Get Summary"):
            dict_str = summerize_by_paste_article(text1,summary_length1,title1)
            st.header(dict_str['title'])
            l = dict_str['summary'][0]['sentences']
            for i in l:
                st.write(i)

if __name__ == '__main__':
    main()