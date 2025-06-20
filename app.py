from langchain_openai import ChatOpenAI
#from langchain.schema import SystemMessage, HumanMessage
from langchain_core.messages import SystemMessage, HumanMessage
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# 選択された占い師と入力された日付に基づいて、占い結果を生成する関数
def fortune_telling(selected_fortune_teller, input_date):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    if selected_fortune_teller == "血液型占い師":
        messages = [
            SystemMessage(content="あなたは血液型占い師です。与えられた血液型に基づいて、その人の運勢を占います。"),
            HumanMessage(content=input_date),
        ]
    else:
        messages = [
            SystemMessage(content="あなたは名前占い師です。与えられた名前に基づいて、その人の運勢を占います。"),
            HumanMessage(content=input_date),
        ]    
    result = llm(messages)
    return result
    #print(result.content)


# 概要・操作法説明
st.title("占い師Webアプリ")
st.write("##### 1: 「血液型占い師」があなたの血液型を占います")
st.write("入力フォームに血液型(A,B,O,AB)を入力してください")
st.write("##### 2: 「名前占い師」があなたの名前を占います")
st.write("入力フォームに名前をフルネームで入力してください。")

selected_fortune_teller = st.radio(
    "占い師を選択してください。",
    ["血液型占い師", "名前占い師"]
)

st.divider()


# 選択された占い師に応じて、入力フォームを表示
if selected_fortune_teller == "血液型占い師":
    input_date = st.text_input(label="あなたの血液型(A,B,O,AB)を入力してください")

else:
    input_date = st.text_input(label="あなたの名前をフルネームで入力してください")
    text_count = len(input_date)


# 「実行」ボタンが押されたときの処理
if st.button("実行"):
    st.divider()
    if selected_fortune_teller == "血液型占い師":
        if input_date:
            if input_date in ["A", "B", "O", "AB"]:
                result = fortune_telling(selected_fortune_teller, input_date)
                st.success(f"占い結果: {result.content}")
            else:
                st.error("血液型はA, B, O, ABのいずれかを入力してください。")
        else:
            st.error("血液型を入力してから「実行」ボタンを押してください。")
    else:
        if input_date:
            if text_count >= 2:
                result = fortune_telling(selected_fortune_teller, input_date)
                st.success(f"占い結果: {result.content}")
            else:
                st.error("名前は2文字以上で入力してください。")
        else:
            st.error("名前を入力してから「実行」ボタンを押してください。")  



