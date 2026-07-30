import streamlit as st

# 1. ページ全体の基本設定
st.set_page_config(
    page_title="しゅうがくりょこうの しおり",
    page_icon="🚌",
    layout="centered"
)

# 2. かわいいデザインとフリガナ用のCSS（デザイン設定）
st.markdown("""
<style>
    /* 全体の背景色をやさしいパステルカラーに */
    .stApp {
        background-color: #FFF9F2;
    }
    
    /* 生徒が見やすい大きい文字と丸みのある枠線 */
    .main-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(255, 182, 193, 0.4);
        border: 3px solid #FFB6C1;
        margin-bottom: 20px;
    }
    
    /* タイトルの装飾 */
    h1 {
        color: #FF6B81;
        text-align: center;
        font-size: 2.2rem !important;
    }

    /* フリガナ（ルビ）のスタイル設定 */
    ruby {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333333;
    }
    rt {
        font-size: 0.8rem;
        color: #FF4757;
        font-weight: normal;
    }
    
    /* ボタンをかわいく大きく */
    .stButton>button {
        background-color: #FF7675;
        color: white;
        border-radius: 15px;
        font-size: 1.3rem;
        padding: 10px 25px;
        border: none;
        width: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #FF6B81;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# 3. アプリのメイン画面処理
def main():
    # ヘッダー画像・イラストの配置（パブリック画像URL）
    st.image("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800", use_column_width=True)
    
    # タイトル（HTMLの<ruby>タグを使って漢字にフリガナを配置）
    st.markdown("""
        <h1>
            <ruby>修学旅行<rt>しゅうがくりょこう</rt></ruby>の 
            <ruby>案内<rt>あんない</rt></ruby>
        </h1>
    """, unsafe_allow_html=True)
    
    st.write("---")

    # カード型の案内エリア
    st.markdown("""
        <div class="main-card">
            <h3>🚌 <ruby>行<rt>い</rt></ruby>き<ruby>先<rt>さき</rt></ruby></h3>
            <p style="font-size: 1.4rem;"><b>とうきょう ディズニーランド</b></p>
            <br>
            <h3>⏰ <ruby>集合<rt>しゅうごう</rt></ruby><ruby>時間<rt>じかん</rt></ruby></h3>
            <p style="font-size: 1.4rem;"><b>あさ 8<ruby>時<rt>じ</rt></ruby> 30<ruby>分<rt>ふん</rt></ruby></b></p>
            <br>
            <h3>🎒 もちもの</h3>
            <ul style="font-size: 1.2rem; line-height: 2;">
                <li>しおり</li>
                <li>おさいふ（おすきなおこづかい）</li>
                <li>ハンカチ・ティッシュ</li>
                <li>すいとう</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # インタラクティブ要素（持ち物チェック）
    st.markdown("### 📝 じゅんび チェック")
    
    chk1 = st.checkbox("しおり を カバン に いれた")
    chk2 = st.checkbox("おさいふ を いれた")
    chk3 = st.checkbox("すいとう を いれた")
    
    if chk1 and chk2 and chk3:
        st.balloons()
        st.success("🎉 じゅんび かんりょう！ たのしんできてね！")

    # ボタンを押した時のイラスト反応
    st.write("")
    if st.button("✨ おたのしみ ボタン"):
        st.write("🎈 たのしい おもいでを たくさん つくろうね！")
        st.image("https://images.unsplash.com/photo-1513151233558-d860c5398176?w=600", use_column_width=True)


if __name__ == "__main__":
    main()
