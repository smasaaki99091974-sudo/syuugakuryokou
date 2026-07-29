import streamlit as st

st.title("金沢・福井 修学旅行クイズ")

# クイズのデータ
quiz_list = [
    {
        "q": "【ひがし茶屋街】外から中が見えにくく、中から外が見えやすい木製の格子を何と呼ぶ？",
        "opts": ["A: 出格子", "B: 木虫籠（きむすこ）", "C: 千本格子"],
        "ans": "B: 木虫籠（きむすこ）",
        "exp": "金沢の町家特有の細い木格子のことです。",
    },
    {
        "q": "【越前松島水族館】透明なガラスの上に寝転がって魚を鑑賞できるコーナーの名前は？",
        "opts": ["A: さんごの海", "B: 海の浮島", "C: 水上さんぽ"],
        "ans": "A: さんごの海",
        "exp": "床一面が透明で、海の上に浮かんでいる気分になれます。",
    },
    {
        "q": "【恐竜博物館】福井県で発見された肉食恐竜の名前は？",
        "opts": ["A: フクイサウルス", "B: フクイティタン", "C: フクイラプトル"],
        "ans": "C: フクイラプトル",
        "exp": "フクイラプトルは肉食恐竜です。",
    },
    {
        "q": "【あわら温泉】湯まち広場にある、無料で手軽に楽しめるスポットは？",
        "opts": ["A: 足湯", "B: 温泉卵作り場", "C: 温泉プール"],
        "ans": "A: 足湯",
        "exp": "本格的な数種類の温泉足湯が無料で楽しめます。",
    },
]

# セッション状態（回答の保持）の初期化
if "user_answers" not in st_session_state:
    st.session_state["user_answers"] = {}

score = 0

# 各問題の表示
for i, q in enumerate(quiz_list, start=1):
    st.subheader(f"第 {i} 問")
    st.write(q["q"])

    # 選択肢ラジオボタン
    choice = st.radio("選択してください", q["opts"], key=f"q_{i}")
    st.session_state["user_answers"][i] = choice
    st.divider()

# 採点ボタン
if st.button("答え合わせをする", type="primary"):
    correct_count = 0
    for i, q in enumerate(quiz_list, start=1):
        user_ans = st.session_state["user_answers"].get(i)
        if user_ans == q["ans"]:
            correct_count += 1
            st.success(f"第 {i} 問：正解！ ⭕️")
        else:
            st.error(f"第 {i} 問：不正解... ❌（正解: {q['ans']}）")
        st.caption(f"解説: {q['exp']}")

    st.balloons()  # 風船を飛ばす演出
    st.header(f"結果：{len(quiz_list)} 問中 {correct_count} 問正解！")
