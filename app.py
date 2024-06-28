import streamlit as st

from PIL import Image
import random
# from chatbot import generate_response


key = open("api.txt" , "r").read().strip("\n")

st.header("مرحبا في محادثة الذكاء الاصطناعي" ,divider='rainbow' )
st.image("How.jpg")
st.subheader(" عمل الطالب فارس محمود الخولي"  )
st.subheader(" مدرسة الخلفاء الراشدين الاعدادية ببورفؤاد"  )

col1, col2 = st.columns(2)

original = Image.open("learn.jpg")
col1.header("تعلم")
col1.image(original, use_column_width=True)

original2 = Image.open("ln.png")
col2.header("امرح")
col2.image(original2, use_column_width=True)

st.image("presdent.jpg")

st.markdown(
    """
قال الرئيس عبدالفتاح السيسي إنّه يجب الاستعداد جيدا لثورة الذكاء الاصطناعي القادمة، لأنّها قادمة لا محال، لذلك وجب الاستعداد للاستفادة منها، بدلا من أن تؤثر علينا سلبا.
"""
)

st.markdown(
    """

قال الرئيس عبدالفتاح السيسي إنّه يجب الاستعداد جيدا لثورة الذكاء الاصطناعي القادمة، لأنّها قادمة لا محال، لذلك وجب الاستعداد للاستفادة منها، بدلا من أن تؤثر علينا سلبا.



وأضاف السيسي خلال حديثه بجلسة "الذكاء الاصطناعي والبشر.. من المتحكم؟"، ضمن فعاليات منتدى شباب العالم بنسخته الثالثة: "القيم التي يتحدث عنها العلماء أثناء التجارب الصناعية للوصول للمنتج النهائي، يجب أن يعرفوا أنّ المنتج النهائي سيخضع دائما لقرار القيادة السياسية للاستفادة بها لصالح بلادهم".

وتابع السيسي: "المليارات التي تم إنفاقها على التعليم والأبحاث تأتي لخدمة مصالح الدول التي تنتج هذه العلوم والتكنولوجيا أولا، ثم يستفيد البقية حسب قدرته على الاستيعاب، فالقوانين والمبادئ خاضعة لمصالح الأمن القومي ورؤى القيادات السياسية العليا للدول".
"""
)

st.header("   " ,divider='rainbow' )

st.header("وعلشان كده ده برنامج ذكاء اصطناعي ممكن نسأله في اي مجال وهو هايرد علينا ")



import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyCymNgrCwe_4rR20OzIWLVPICGuIKZhYhM")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

history = []

chat_session = model.start_chat(
  history= history
)

prompt = st.text_input("اسأل الذكاء الاصطناعي ")

btn = st.button("ارسل سؤالك")

if btn:

    response = chat_session.send_message(prompt)
    model_respons = response.text
    history.append({"role" : "user" , "parts" : [prompt]})
    history.append({"role" : "user" , "parts" : [model_respons]})

    st.write(model_respons)

    
