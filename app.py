import streamlit as st

# ページの基本設定
st.set_page_config(
    page_title="修学旅行クイズ",
    page_icon="🚌",
    layout="centered"
)

# --------------------------------------------------
# デザイン設定（CSS）
# エラーの原因だった padding などのスタイルはここに配置します
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* 背景色をやさしいクリーム色に */
    .stApp {
        background-color: #FFFDF0;
    }

    /* フリガナ（ルビ）のデザイン */
    ruby {
        font-size: 1.3rem;
        font-weight: bold;
        color: #333333;
    }
    rt {
        font-size: 0.75rem;
        color: #D9534F; /* フリガナを読みやすい赤色に */
    }

    /* 問題カード枠のデザイン */
    .quiz-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 20px; /* ← エラーの原因箇所を修正して配置 */
        margin-bottom: 20px;
        border: 3px solid #FFD1DC;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }

    /* ボタンのかわいいデザイン */
    .stButton>button {
        background-color: #FFB6C1;
        color: #FFFFFF;
        border-radius: 15px;
        border: none;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 10px 20px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# クイズアプリのメイン画面
# --------------------------------------------------

# タイトル
st.markdown("<h1>🚌 <ruby>修学<rt>しゅうがく</rt></ruby><ruby>旅行<rt>りょこう</rt></ruby>の たのしいクイズ 🎉</h1>", unsafe_allow_html=True)
st.write("ボタンを おして <ruby>問題<rt>もんだい</rt></ruby>に こたえてね！")

st.write("---")

# 第1問
st.markdown(
    """
    <div class="quiz-card">
        <h3>❓ <ruby>第<rt>だい</rt></ruby>1<ruby>問<rt>もん</rt></ruby></h3>
        <p><ruby>水族館<rt>すいぞくかん</rt></ruby>で ショーを する かわいい <ruby>動物<rt>どうぶつ</rt></ruby>は だれかな？ 🐬</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 選択肢ボタン
col1, col2 = st.columns(2)
with col1:
    q1_a = st.button("① イルカ 🐬")
with col2:
    q1_b = st.button("② ライオン 🦁")

if q1_a:
    st.balloons()
    st.success("⭕️ せいかい！ イルカさんの ダイナミックな ジャンプを たのしもうね！")
elif q1_b:
    st.error("❌ ざんねん！ ライオンは 動物園（どうぶつえん）に いるよ。")

st.write("---")

# 第2問
st.markdown(
    """
    <div class="quiz-card">
        <h3>❓ <ruby>第<rt>だい</rt></ruby>2<ruby>問<rt>もん</rt></ruby></h3>
        <p><ruby>夜<rt>よる</rt></ruby>、ホテルで ねるときに 守る（まもる）<ruby>約束<rt>やくそく</rt></ruby>は どれかな？ 🌙</p>
    </div>
    """,
    unsafe_allow_html=True
)

col3, col4 = st.columns(2)
with col3:
    q2_a = st.button("① はやく ねる 🛌")
with col4:
    q2_b = st.button("② おおごえで さわぐ 🗣️")

if q2_a:
    st.balloons()
    st.success("⭕️ せいかい！ しっかり すいみんをとって、あしたも たのしもうね！")
elif q2_b:
    st.error("❌ ざんねん！ しずかに すごすのが マナーだよ。")
