import streamlit as st

# ページの基本設定（タイトルや絵文字アイコン）
st.set_page_config(
    page_title="修学旅行のしおり",
    page_icon="🚌",
    layout="centered"
)

# --------------------------------------------------
# デザイン設定（CSS）
# エラーの原因だった padding などのスタイルはここへまとめます
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* 全体の背景色をやわらかいピンクベージュに */
    .stApp {
        background-color: #FFF9F5;
    }

    /* フリガナ（ルビ）の見栄えを調整 */
    ruby {
        font-size: 1.2rem;
        font-weight: bold;
        color: #333333;
    }
    rt {
        font-size: 0.7rem;
        color: #E05A47; /* フリガナの色を優しく */
    }

    /* カード風の丸みのある枠線デザイン */
    .custom-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 20px; /* ← エラーになっていた記述をこちらに配置 */
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        border: 2px solid #FFD1DC;
    }

    /* ボタンのかわいいデザイン */
    .stButton>button {
        background-color: #FFB7C5;
        color: #FFFFFF;
        border-radius: 15px;
        border: none;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #FF94A8;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# アプリの画面作成
# --------------------------------------------------

# ヘッダー（タイトルとイラスト）
st.markdown("<h1>🚌 <ruby>修学<rt>しゅうがく</rt></ruby><ruby>旅行<rt>りょこう</rt></ruby>のしおり 🎉</h1>", unsafe_allow_html=True)
st.write("たのしい <ruby>旅行<rt>りょこう</rt></ruby>の スケジュールを かくにんしよう！")

st.write("---")

# スケジュールカード 1
st.markdown(
    """
    <div class="custom-card">
        <h3>⏰ 1<ruby>日目<rt>にちめ</rt></ruby>：<ruby>出発<rt>しゅっぱつ</rt></ruby>！</h3>
        <p>🌸 <b>8:30</b> - <ruby>学校<rt>がっこう</rt></ruby>に <ruby>集合<rt>しゅうごう</rt></ruby>（バスに のるよ）</p>
        <p>🎨 <b>11:00</b> - <ruby>水族館<rt>すいぞくかん</rt></ruby>で イルカショーを みよう！ 🐬</p>
        <p>🍱 <b>12:30</b> - おいしい おべんとうタイム 🍙</p>
    </div>
    """,
    unsafe_allow_html=True
)

# スケジュールカード 2
st.markdown(
    """
    <div class="custom-card">
        <h3>🏨 ホテルでの すごしかた</h3>
        <p>♨️ <b>17:00</b> - おふろに はいろう</p>
        <p>🍽️ <b>18:30</b> - みんなで たのしい ゆうごはん 🍔</p>
        <p>🌙 <b>21:00</b> - <ruby>準備<rt>じゅんび</rt></ruby>をして ねましょう 🛌</p>
    </div>
    """,
    unsafe_allow_html=True
)

# インタラクティブなボタン（スタンプラリー感覚）
if st.button("✨ <ruby>準備<rt>じゅんび</rt></ruby>できたかな？ ボタンを押してみてね！"):
    st.balloons()
    st.success("ばっちり！ たのしい <ruby>旅行<rt>りょこう</rt></ruby>に しようね！ 🎈")
