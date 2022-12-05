import streamlit as st

st.set_page_config(layout="centered")

st.subheader("手紙の内容を読むために、ブランクに正解の答えを入れてください。")
st.header("")

class Template:

    def __init__(self):
        self.ans_1 = None
        self.button_1 = None
        self.ans_2 = None
        self.button_2 = None
        self.ans_3 = None
        self.button_3 = None
        self.ans_1_accepted = ["営業仕事","えいぎょうしごと","営業","エイギョウ"]
        self.ans_2_accepted = ["中国","ちゅうごく","チュウゴク"]
        self.ans_3_accepted = ["イーブイ"]
        self.header = st.header("")

        if 'checker' not in st.session_state:
            st.session_state.checker = 0
    
    def render(self):
        if st.session_state.checker == 0:
            self.ans_1 = st.text_input("Q1: 先生のお仕事は何ですか？")
            self.button_1 = st.button("答え")
            self.header
            st.subheader(f"正しい答え: {st.session_state.checker}")

        if st.session_state.checker == 1:
            self.header
            self.ans_2 = st.text_input("Q2: 一番苦手な生徒の国籍は？")
            self.button_2 = st.button("答え",key=2)
            self.header
            st.subheader(f"正しい答え: {st.session_state.checker}")

        if st.session_state.checker == 2:
            self.header
            self.ans_3 = st.text_input("Q3: 先生の好きなポケモンの名前は何ですか？")
            self.button_3 = st.button("答え",key=3)

            self.header
            st.subheader(f"正しい答え: {st.session_state.checker}")
            print(st.session_state.checker)
        
        if st.session_state.checker > 3:

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

    def render_template(self,accepted_ans, button, ans):
  
        if button:
            if ans in accepted_ans:
                st.session_state.checker = st.session_state.checker + 1 if st.session_state.checker <3 else st.session_state.checker
                if st.session_state.checker >=3:
                    self.render_imgs()
                return True
            else:
                st.subheader("間違いました。もう１回答えてください。")
            return False
    


if __name__ == '__main__':
    obj = Template()
    obj.render()

    if obj.button_1:
        obj.render_template(obj.ans_1_accepted,
                                    obj.button_1,
                                    obj.ans_1,
                                    )
        obj.render()
    if obj.button_2:
        res2 = obj.render_template(obj.ans_2_accepted,
        obj.button_2,
        obj.ans_2,
        )
        obj.render()
    if obj.button_3:
        obj.render_template(obj.ans_3_accepted,
        obj.button_3,
        obj.ans_3,
        )
        obj.render()