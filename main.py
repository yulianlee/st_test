import streamlit as st

st.set_page_config(layout="centered")
st.beta_set_page_config(page_title='arisa_ohashi',layout = 'wide', initial_sidebar_state = 'auto')

class Template:

    def __init__(self):
        self.ans_1 = None
        self.button_1 = None
        self.ans_2 = None
        self.button_2 = None
        self.ans_3 = None
        self.button_3 = None
        self.feedback = st.empty()
        self.ans_1_accepted = ["営業仕事","えいぎょうしごと","営業","エイギョウ"]
        self.ans_2_accepted = ["中国","ちゅうごく","チュウゴク","中国人"]
        self.ans_3_accepted = ["イーブイ"]
        self.header = st.header("")

        if 'checker' not in st.session_state:
            st.session_state.checker = 0
    
    def render(self):
        if st.session_state.checker == 0:
            st.subheader("手紙の内容を読むために、ブランクに正解の答えを入れてください。")
            st.header("")
            self.ans_1 = st.text_input("Q1: 先生のお仕事は何ですか？")
            self.button_1 = st.button("答え", on_click=self.render_template, args = (self.ans_1_accepted,self.ans_1))
            self.header
            st.subheader(f"正しい答え: {st.session_state.checker}")

        if st.session_state.checker == 1:
            st.subheader("手紙の内容を読むために、ブランクに正解の答えを入れてください。")
            st.header("")
            self.header
            self.ans_2 = st.text_input("Q2: 一番苦手な生徒の国籍は？")
            self.button_2 = st.button("答え",key=2, on_click=self.render_template, args = (self.ans_2_accepted,self.ans_2))
            self.header
            st.subheader(f"正しい答え: {st.session_state.checker}")

        if st.session_state.checker == 2:
            st.subheader("手紙の内容を読むために、ブランクに正解の答えを入れてください。")
            st.header("")
            self.header
            self.ans_3 = st.text_input("Q3: 先生の好きなポケモンの名前は何ですか？")
            self.button_3 = st.button("答え",key=3, on_click=self.render_template, args = (self.ans_3_accepted,self.ans_3))
            self.header
            st.subheader(f"正しい答え: {st.session_state.checker}")
                
        if st.session_state.checker >= 3:
            st.header("今まで、どうもありがとうございます。")
            st.header("")
            self.render_imgs()

    def find_substring(self,lst,string):
        for i in lst:
            if i.find(string) != -1:
                return True
        else:
            return False

    def render_imgs(self):
        st.image("Images/job.jpg")
        
        col1, col2 = st.columns(2)
        with col1:
            st.image("Images/doubt.jpg")
        with col2:
            st.image("Images/doubt2.jpg")

        st.image("Images/pokemon.jpg")
        st.image("Images/final.jpg")
        return 

    def render_template(self,accepted_ans,  ans):
        if ans in accepted_ans:
            st.session_state.checker = st.session_state.checker + 1 if st.session_state.checker <3 else st.session_state.checker
        else: 
            st.subheader("間違いました。もう１回答えてください。")

if __name__ == '__main__':
    obj = Template()
    obj.render()