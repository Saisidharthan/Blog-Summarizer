#import libraries required
from openai import OpenAI

import streamlit as st
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

st.header("Summarizer App using Openai + Streamlit")
article_text = st.text_area("Enter Your text to summarize")
if len(article_text) > 100:
    temp =st.slider("temperature",0.0,1.0,0.5)
    if st.button("As a Brief context"):
            # use GPT-3 to generate summary of the article
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that helps to summarize the content given to u"},
                    {"role": "user", "content": f"Please summarize this specific article for me in 100 words with heading {article_text}"}
                ],
                temperature =temp
            )

            print(response)
            res=response.choices[0].message.content
            st.info(res)

            st.download_button("Download the result",res)
else:
    st.warning("the sentence is not long enough !!")