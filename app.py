import streamlit as st

# ページの設定
st.set_page_config(
    page_title="しゅうがくりょこうの しおり",
    page_icon="🚌",
    layout="centered"
)

# かわいいデザインと読みやすい文字サイズの設定（CSS）
st.markdown("""
    <style>
    /* 全体の背景色とフォント設定 */
    .stApp {
        background-color: #FFF9F3;
        font-family: "Hiragino Sans", "Meiryo", sans-serif;
    }
    
    /* カード風の白い枠線（CSSの文法エラーを修正した部分） */
    .card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        border: 3px solid #FFD1DC;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* タイトルのスタイル */
    .title-text {
        color: #FF6F91;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    
    /* 本文の文字サイズ（大きめで見やすく） */
    p, div, label, li {
        font-size: 20px !important;
        line-height: 1.6 !important;
    }
    
    /* ルビ（フリガナ）のスタイル */
    ruby {
        font-size: 22px;
        font-weight: bold;
    }
    rt {
        font-size: 13px;
        color: #555555;
    }
    </style>
""", unsafe_allow_html=True)

# アプリのタイトル
st.markdown('<div class="title-text">🚌 <ruby>修学旅行<rt>しゅうがくりょこう</rt></ruby>の しおり 🌸</div>', unsafe_allow_html=True)

st.write("---")

# メインコンテンツ（カード表示）
st.markdown("""
<div class="card">
    <h3>📅 <ruby>日程<rt>にってい</rt></ruby>の ごあんない</h3>
    <p>
        <ruby>日<rt>ひ</rt></ruby>ちじ：10<ruby>月<rt>がつ</rt></ruby> 15<ruby>日<rt>にち</rt></ruby>（<ruby>木<rt>もく</rt></ruby>）〜 10<ruby>月<rt>がつ</rt></ruby> 16<ruby>日<rt>にち</rt></ruby>（<ruby>金<rt>きん</rt></ruby>）<br>
        <ruby>行<rt>い</rt></ruby>き<ruby>先<rt>さき</rt></ruby>：とうきょう・よこはま
    </p>
</div>

<div class="card">
    <h3>🎒 もちもの チェック</h3>
    <p>
        ・しおり<br>
        ・サイフ（お<ruby>金<rt>かね</rt></ruby>）<br>
        ・ハンカチ・ティッシュ<br>
        ・きがえ
    </p>
</div>
""", unsafe_allow_html=True)

# 生徒が操作できる入力フォーム
st.markdown("### 📝 <ruby>自分<rt>じぶん</rt></ruby>の <ruby>目標<rt>もくひょう</rt></ruby>")
goal = st.text_input("たのしみに している ことを かいてね！", placeholder="れい：水族館で ペンギンを 見る")

if goal:
    st.success(f"いいね！「{goal}」を たのしもうね！")
