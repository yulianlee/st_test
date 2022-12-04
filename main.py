import streamlit as st

st.set_page_config(layout="centered")

st.subheader("手紙の内容を読むために、ブランクに正解の答えを入れてください。")
st.header("")

class Template:

    def __init__(self):
        self.ans_1 = st.text_input("Q1: 先生のお仕事は何ですか？")
        self.button_1 = st.button("答え")
        self.placeholder_1 = st.empty()
        self.ans_2 = st.text_input("Q2: 一番苦手な生徒の国籍は？")
        self.button_2 = st.button("答え",key=2)
        self.placeholder_2 = st.empty()
        self.ans_3 = st.text_input("Q3: 先生の好きなポケモンの名前は何ですか？")
        self.button_3 = st.button("答え",key=3)
        self.placeholder_3 = st.empty()
        self.ans_1_accepted = ["営業仕事","えいぎょうしごと","営業","エイギョウ"]
        self.ans_2_accepted = ["中国","ちゅうごく","チュウゴク"]
        self.ans_3_accepted = ["イーブイ"]
    
    def render(self):
        self.ans_1
        self.button_1
        self.placeholder_1     

        st.header("")
        self.ans_2
        self.button_2
        self.placeholder_2

        st.header("")
        self.ans_3 
        self.button_3
        self.placeholder_3


    def find_substring(self,lst,string):
        for i in lst:
            if i.find(string) != -1:
                return True
        else:
            return False


    def render_template(self,accepted_ans, button, ans, img_path, placeholder):
        # print(prev_corr)
        if button:
            if ans in accepted_ans:
                with placeholder:
                    st.image(img_path)
                return True
            else:
                st.text("間違いました。もう１回答えてください。")
            return False
    
    # elif not prev_corr:
    #     st.header("")
    #     st.subheader("前の質問を答えてください。")


if __name__ == '__main__':
    obj = Template()
    obj.render()
    
    if obj.button_1:
        obj.render_template(obj.ans_1_accepted,
        obj.button_1,obj.ans_1,
        "Images/job.jpg",
        obj.placeholder_1
        )
            
    if obj.button_2:
        obj.render_template(obj.ans_2_accepted,
        obj.button_2,obj.ans_2,
        "Images/doubt.jpg",
        obj.placeholder_2)

    if obj.button_3:
        obj.render_template(obj.ans_3_accepted,
        obj.button_1,obj.ans_3,
        "Images/job.jpg",
        obj.placeholder_3)
