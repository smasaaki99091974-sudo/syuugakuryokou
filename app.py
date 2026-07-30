import os
import streamlit as st
from PIL import Image

# ---- ページの設定（タイトルとアイコン） ----
st.set_page_config(
    page_title="金沢・福井 修学旅行クイズ",
    page_icon="🏯",
    layout="centered"
)

# ---- デザインをかわいくするCSS（カスタムスタイル） ----
st.markdown("""
    <style>
    /* 全体の背景色をやさしい色にする */
    .stApp {
        background-color: #FFF9F2;
    }
    /* ボタンを丸く・かわいくする */
    .stButton>button {
        border-radius: 20px;
        background-color: #FFE4E1;
        color: #4A4A4A;
        font-weight: bold;
        border: 2px solid #FFB6C1;
        padding: 10px 20px;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        background-color: #FFB6C1;
        color: white;
    }
    /* ふりがな（ルビ）を見やすく調整 */
    ruby {
        font-size: 1.3rem;
        font-weight: bold;
    }
    rt {
        font-size: 0.75rem;
        color: #FF69B4;
        font-weight: normal;
    }
    </style>
""", unsafe_allow_html=True)


# ---- 各問題の画像（写真）を読み込む関数 ----
def get_quiz_image(file_prefix):
    jpg_path = f"{file_prefix}.jpg"
    png_path = f"{file_prefix}.png"

    if os.path.exists(jpg_path):
        return Image.open(jpg_path)
    elif os.path.exists(png_path):
        return Image.open(png_path)
    else:
        st.warning(
            f"がぞうファイル '{file_prefix}.jpg' (または .png) が見つかりません。GitHubにアップロードしてください。"
        )
        return None


# ---- クイズのデータ（漢字にルビ <ruby>漢字<rt>かんじ</rt></ruby> を挿入） ----
quiz_list = [
    {
        "q": "<ruby>東<rt>ひがし</rt></ruby><ruby>茶屋街<rt>ちゃやがい</rt></ruby>の<ruby>美<rt>うつく</rt></ruby>しい<ruby>建物<rt>たてもの</rt></ruby>に<ruby>見<rt>み</rt></ruby>られる、<ruby>外<rt>そと</rt></ruby>から<ruby>中<rt>なか</rt></ruby>が<ruby>見<rt>み</rt></ruby>えにくく、<ruby>中<rt>なか</rt></ruby>から<ruby>外<rt>そと</rt></ruby>が<ruby>見<rt>み</rt></ruby>えやすい<ruby>木製<rt>もくせい</rt></ruby>の<ruby>格子<rt>こうし</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>ぶでしょう？",
        "opts": ["A: 出格子（でごうし）", "B: 木虫籠（きむすこ）", "C: 千本格子（せんぼんごうし）"],
        "ans": "B: 木虫籠（きむすこ）",
        "exp": "<ruby>金沢<rt>かなざわ</rt></ruby>の<ruby>町家<rt>まちや</rt></ruby><ruby>特有<rt>とくゆう</rt></ruby>の<ruby>細<rt>ほそ</rt></ruby>い<ruby>木格子<rt>きごうし</rt></ruby>のことで、<ruby>光<rt>ひかり</rt></ruby>を取り<ruby>入<rt>い</rt></ruby>れつつプライバシーを<ruby>守<rt>まも</rt></ruby>る<ruby>工夫<rt>くふう</rt></ruby>がされています。",
        "image_prefix": "kimusuko",
    },
    {
        "q": "<ruby>越前松島水族館<rt>えちぜんまつしますいぞくかん</rt></ruby>で<ruby>大人気<rt>だいにんき</rt></ruby>の、<ruby>透明<rt>とうめい</rt></ruby>なアクリルガラスの<ruby>上<rt>うえ</rt></ruby>に<ruby>寝<rt>ね</rt></ruby>ころがって<ruby>海<rt>うみ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>浮<rt>う</rt></ruby>いているような<ruby>体験<rt>たいけん</rt></ruby>ができるコーナーの<ruby>名前<rt>なまえ</rt></ruby>は？",
        "opts": ["A: さんごの海（うみ）", "B: 海（うみ）の浮島（うきしま）", "C: 水上（すいじょう）さんぽ"],
        "ans": "A: さんごの海（うみ）",
        "exp": "<ruby>床<rt>ゆか</rt></ruby><ruby>一面<rt>いちめん</rt></ruby>が<ruby>透明<rt>とうめい</rt></ruby>なガラス<ruby>張<rt>ば</rt></ruby>りになっていて、<ruby>魚<rt>さかな</rt></ruby>たちが<ruby>泳<rt>およ</rt></ruby>ぐプールの上（うえ）に<ruby>寝<rt>ね</rt></ruby>そべることができます。",
        "image_prefix": "aquarium",
    },
    {
        "q": "<ruby>福井県<rt>ふくいけん</rt></ruby><ruby>勝山市<rt>かつやまし</rt></ruby>で<ruby>発見<rt>はっけん</rt></ruby>され、<ruby>名前<rt>なまえ</rt></ruby>にも「フクイ」とついている<ruby>肉食恐竜<rt>にくしょくきょうりゅう</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>はつぎのうちどれでしょう？",
        "opts": ["A: フクイサウルス", "B: フクイティタン", "C: フクイラプトル"],
        "ans": "C: フクイラプトル",
        "exp": "フクイラプトルは<ruby>福井県<rt>ふくいけん</rt></ruby>で<ruby>発見<rt>はっけん</rt></ruby>された<ruby>肉食恐竜<rt>にくしょくきょうりゅう</rt></ruby>です（フクイサウルスは<ruby>草食恐竜<rt>そうしょくきょうりゅう</rt></ruby>です）。",
        "image_prefix": "museum",
    },
    {
        "q": "あわら<ruby>温泉<rt>おんせん</rt></ruby>の<ruby>湯<rt>ゆ</rt></ruby>まち<ruby>広場<rt>ひろば</rt></ruby>にある、<ruby>無料<rt>むりょう</rt></ruby>で誰（だれ）でも<ruby>気軽<rt>きがる</rt></ruby>にたのしめる<ruby>人気<rt>にんき</rt></ruby>スポットは<ruby>何<rt>なに</rt></ruby>でしょう？",
        "opts": ["A: 足湯（あしゆ）", "B: 温泉（おんせん）たまご作り場（つくりば）", "C: 温泉（おんせん）プール"],
        "ans": "A: 足湯（あしゆ）",
        "exp": "あわら<ruby>温泉<rt>おんせん</rt></ruby>の<ruby>足湯<rt>あしゆ</rt></ruby>はいくつかの<ruby>浴槽<rt>よくそう</rt></ruby>があり、<ruby>源泉<rt>げんせん</rt></ruby>かけ<ruby>流<rt>なが</rt></ruby>しの<ruby>湯<rt>ゆ</rt></ruby>を<ruby>無料<rt>むりょう</rt></ruby>でたのしめます。",
        "image_prefix": "onsen",
    },
]

# ---- セッション状態の管理 ----
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected_opt" not in st.session_state:
    st.session_state.selected_opt = None

st.title("🏯 かなざわ・ふくい しゅうがくりょこうクイズ")

total_q = len(quiz_list)
current_idx = st.session_state.current_q

# ---- 全問題終了画面 ----
if current_idx >= total_q:
    st.balloons()
    st.header("🎉 クイズ おわり！")
    st.subheader(f"あなたのスコア: {total_q} もん ちゅう {st.session_state.score} もん せいかい")

    if st.button("さいしょから もういちど ちょうせんする", type="primary"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected_opt = None
        st.rerun()

# ---- 問題表示画面 ----
else:
    q_data = quiz_list[current_idx]

    # 進捗バーを表示
    st.progress((current_idx) / total_q)
    st.caption(f"だい {current_idx + 1} もん / ぜん {total_q} もん")

    # 画像の取得と表示
    img = get_quiz_image(q_data["image_prefix"])
    if img is not None:
        st.image(img, use_container_width=True)

    # 問題文（HTMLのrubyタグを使うため unsafe_allow_html=True）
    st.markdown(f"### {q_data['q']}", unsafe_allow_html=True)

    # 回答前：ボタンで選択
    if not st.session_state.answered:
        for opt in q_data["opts"]:
            if st.button(opt, key=opt, use_container_width=True):
                st.session_state.selected_opt = opt
                st.session_state.answered = True
                if opt == q_data["ans"]:
                    st.session_state.score += 1
                st.rerun()

    # 回答後：結果と解説を表示
    else:
        user_choice = st.session_state.selected_opt
        if user_choice == q_data["ans"]:
            st.success(f"⭕️ せいかい！ （あなたのこたえ: {user_choice}）")
        else:
            st.error(
                f"❌ ざんねん... 不正解（ふせいかい） （あなたのこたえ: {user_choice} / せいかい: {q_data['ans']}）"
            )

        # 解説文もルビ対応
        st.info(f"💡 **かいせつ:** {q_data['exp']}", icon="💡")

        # 次の問題へ進むボタン
        if st.button("つぎの もんだいへ ➔", type="primary", use_container_width=True):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.selected_opt = None
            st.rerun()
