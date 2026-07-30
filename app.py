import os
from PIL import Image
import streamlit as st

# ---- ページの設定（タイトルとアイコン） ----
st.set_page_config(
    page_title="金沢・福井 修学旅行クイズ", page_icon="🏯", layout="centered"
)

# ---- デザインをかわいくするCSS（カスタムスタイル） ----
st.markdown(
    """
    <style>
    /* 全体の背景色をやさしい色にする */
    .stApp {
        background-color: #FFF9F2;
    }
    
    /* ---- ボタン（選択肢など）を大きく・丸く・かわいくする ---- */
    .stButton>button {
        border-radius: 20px;
        background-color: #FFE4E1;
        color: #4A4A4A;
        font-weight: bold;
        border: 2px solid #FFB6C1;
        padding: 12px 24px;
        font-size: 1.4rem; /* 選択肢の文字を大きく調整 */
        line-height: 1.5;   /* 文字の天地にゆとりを持たせる */
    }
    .stButton>button:hover {
        background-color: #FFB6C1;
        color: white;
    }
    
    /* ---- ルビ（フリガナ）のスタイル調整 ---- */
    /* 漢字（本文）を大きく表示 */
    ruby {
        font-size: 1.4rem;
        font-weight: bold;
        line-height: 2.2; /* ルビと被らないように行間を確保 */
    }
    /* フリガナ（ルビ）を小さく・見やすい濃い青色に調整 */
    rt {
        font-size: 0.85rem;
        color: #1A5276; /* 見やすい濃い青色 */
        font-weight: bold;
    }
    
    /* カスタム解説ボックス（HTMLルビ対応） */
    .explanation-box {
        background-color: #E6F3FF;
        border: 2px solid #B0E0E6;
        border-radius: 15px;
        padding: 15px;
        margin-top: 15px;
        margin-bottom: 15px;
        color: #333333;
        font-size: 1.1rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# ---- 各問題の画像（写真・イラスト）を読み込む関数 ----
def get_quiz_image(file_prefix):
    jpg_path = f"{file_prefix}.jpg"
    png_path = f"{file_prefix}.png"

    if os.path.exists(png_path):
        return Image.open(png_path)
    elif os.path.exists(jpg_path):
        return Image.open(jpg_path)
    else:
        st.warning(
            f"がぞうファイル '{file_prefix}.png' (または .jpg) が見つかりません。GitHubにアップロードしてください。"
        )
        return None


# ---- クイズのデータ（全10問） ----
quiz_list = [
    # ① 1日目に行くところ
    {
        "q": "1<ruby>日目<rt>にちめ</rt></ruby>に<ruby>行<rt>い</rt></ruby>くところはどこでしょう？",
        "opts": [
            "A: 越前松島水族館（えちぜんまつしますいぞくかん）",
            "B: 東茶屋街（ひがしちゃやがい）",
            "C: 恐竜博物館（きょうりゅうはくぶつかん）",
        ],
        "ans": "A: 越前松島水族館（えちぜんまつしますいぞくかん）",
        "exp": "1<ruby>日目<rt>にちめ</rt></ruby>は<ruby>越前松島水族館<rt>えちぜんまつしますいぞくかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます！<ruby>楽<rt>たの</rt></ruby>しみですね。",
        "image_prefix": "aquarium",
    },
    # ② 2日目に行くところ
    {
        "q": "2<ruby>日目<rt>にちめ</rt></ruby>に<ruby>行<rt>い</rt></ruby>くところはどこでしょう？",
        "opts": [
            "A: 金沢城公園（かなざわじょうこうえん）",
            "B: 福井県立恐竜博物館（ふくいけんりつきょうりゅうはくぶつかん）",
            "C: 湯町広場（ゆまちひろば）",
        ],
        "ans": "B: 福井県立恐竜博物館（ふくいけんりつきょうりゅうはくぶつかん）",
        "exp": "2<ruby>日目<rt>にちめ</rt></ruby>は<ruby>大人気<rt>だいにんき</rt></ruby>の<ruby>福井県立恐竜博物館<rt>ふくいけんりつきょうりゅうはくぶつかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます！",
        "image_prefix": "museum",
    },
    # ③ 3日目に行くところ
    {
        "q": "3<ruby>日目<rt>にちめ</rt></ruby>に<ruby>行<rt>い</rt></ruby>くところはどこでしょう？",
        "opts": [
            "A: ひがし茶屋街（ちゃやがい）",
            "B: 越前松島水族館（えちぜんまつしますいぞくかん）",
            "C: あわら温泉（おんせん）",
        ],
        "ans": "A: ひ发し茶屋街（ちゃやがい）",
        "exp": "3<ruby>日目<rt>にちめ</rt></ruby>は<ruby>風情<rt>ふぜい</rt></ruby>ある<ruby>金沢<rt>かなざわ</rt></ruby>の「ひがし<ruby>茶屋街<rt>ちゃやがい</rt></ruby>」を<ruby>散策<rt>さんさく</rt></ruby>します！",
        "image_prefix": "kimusuko",
    },
    # ④ ティラノサウルスの大きさ
    {
        "q": "ティラノサウルスの<ruby>大<rt>おお</rt></ruby>きさはどれくらいでしょう？",
        "opts": [
            "1: 軽自動車（けいじどうしゃ）",
            "2: 観光（かんこう）バス",
            "3: 新幹線（しんかんせん）の車両（しゃりょう）",
        ],
        "ans": "2: 観光（かんこう）バス",
        "exp": "ティラノサウルスは<ruby>全長<rt>ぜんちょう</rt></ruby>およそ12〜13メートルあり、<ruby>大型<rt>おおがた</rt></ruby>の<ruby>観光<rt>かんこう</rt></ruby>バスとほぼ<ruby>同<rt>おな</rt></ruby>じくらいの<ruby>大<rt>おお</rt></ruby>きさです！",
        "image_prefix": "museum",
    },
    # ⑤ 福井県で発見された恐竜の数
    {
        "q": "<ruby>福井県<rt>ふくいけん</rt></ruby>で<ruby>発見<rt>はっけん</rt></ruby>された<ruby>恐竜<rt>きょうりゅう</rt></ruby>は<ruby>何種類<rt>なんしゅるい</rt></ruby>でしょう？",
        "opts": ["1: 3種類（しゅるい）", "2: 6種類（しゅるい）", "3: 10種類（しゅるい）"],
        "ans": "2: 6種類（しゅるい）",
        "exp": "<ruby>福井県<rt>ふくいけん</rt></ruby>ではフクイラプトルやフクイサウルスなど、これまでに6<ruby>種類<rt>しゅるい</rt></ruby>の新種（しんしゅ）の<ruby>恐竜<rt>きょうりゅう</rt></ruby>が<ruby>発見<rt>はっけん</rt></ruby>されています！",
        "image_prefix": "museum",
    },
    # ⑥ 恐竜の子孫
    {
        "q": "<ruby>恐竜<rt>きょうりゅう</rt></ruby>の<ruby>子孫<rt>しそん</rt></ruby>はどれでしょう？",
        "opts": [
            "1: トカゲ／ワニ",
            "2: 鳥（とり）",
            "3: 哺乳類（ほにゅうるい）",
        ],
        "ans": "2: 鳥（とり）",
        "exp": "じつは<ruby>恐竜<rt>きょうりゅう</rt></ruby>（<ruby>獣脚類<rt>じゅうきゃくるい</rt></ruby>）の<ruby>一部<rt>いちぶ</rt></ruby>が<ruby>進化<rt>しんか</rt></ruby>したものが、いまの<ruby>鳥<rt>とり</rt></ruby>たちです！",
        "image_prefix": "museum",
    },
    # ⑦ キャラクターの名前
    {
        "q": "このキャラクターの<ruby>名前<rt>なまえ</rt></ruby>はなにでしょう？",
        "opts": [
            "A: 湯巡権三（ゆめぐりごんぞう）",
            "B: あわら湯たろう（ゆたろう）",
            "C: 温泉ごんちゃん（おんせんごんちゃん）",
        ],
        "ans": "A: 湯巡権三（ゆめぐりごんぞう）",
        "exp": "あわら<ruby>温泉<rt>おんせん</rt></ruby>の<ruby>キャラクター<rt>きゃらくたー</rt></ruby>「<ruby>湯巡権三<rt>ゆめぐりごんぞう</rt></ruby>」さんです！",
        "image_prefix": "gonzo",  # GitHubに gonzo.png または gonzo.jpg を用意してください
    },
    # ⑧ 既存：東茶屋街の格子
    {
        "q": "<ruby>東茶屋街<rt>ひがしちゃやがい</rt></ruby>の<ruby>美<rt>うつく</rt></ruby>しい<ruby>建物<rt>たてもの</rt></ruby>に<ruby>見<rt>み</rt></ruby>られる、<ruby>外<rt>そと</rt></ruby>から<ruby>中<rt>なか</rt></ruby>が<ruby>見<rt>み</rt></ruby>えにくく、<ruby>中<rt>なか</rt></ruby>から<ruby>外<rt>そと</rt></ruby>が<ruby>見<rt>み</rt></ruby>えやすい<ruby>木製<rt>もくせい</rt></ruby>の<ruby>格子<rt>こうし</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>ぶでしょう？",
        "opts": [
            "A: 出格子（でごうし）",
            "B: 木虫籠（きむすこ）",
            "C: 千本格子（せんぼんごうし）",
        ],
        "ans": "B: 木虫籠（きむすこ）",
        "exp": "<ruby>金沢<rt>かなざわ</rt></ruby>の<ruby>町家<rt>まちや</rt></ruby><ruby>特有<rt>とくゆう</rt></ruby>の<ruby>細<rt>ほそ</rt></ruby>い<ruby>木格子<rt>きごうし</rt></ruby>のことで、<ruby>光<rt>ひかり</rt></ruby>を取り<ruby>入<rt>い</rt></ruby>れつつプライバシーを<ruby>守<rt>まも</rt></ruby>る<ruby>工夫<rt>くふう</rt></ruby>がされています。",
        "image_prefix": "kimusuko",
    },
    # ⑨ 既存：あわら温泉の足湯
    {
        "q": "あわら<ruby>温泉<rt>おんせん</rt></ruby>の<ruby>湯<rt>ゆ</rt></ruby>まち<ruby>広場<rt>ひろば</rt></ruby>にある、<ruby>無料<rt>むりょう</rt></ruby>で誰（だれ）でも<ruby>気軽<rt>きがる</rt></ruby>にたのしめる<ruby>人気<rt>にんき</rt></ruby>スポットは<ruby>何<rt>なに</rt></ruby>でしょう？",
        "opts": [
            "A: 足湯（あしゆ）",
            "B: 温泉（おんせん）たまご作り場（つくりば）",
            "C: 温泉（おんせん）プール",
        ],
        "ans": "A: 足湯（あしゆ）",
        "exp": "あわら<ruby>温泉<rt>おんせん</rt></ruby>の<ruby>足湯<rt>あしゆ</rt></ruby>はいくつかの<ruby>浴槽<rt>よくそう</rt></ruby>があり、<ruby>源泉<rt>げんせん</rt></ruby>かけ<ruby>流<rt>なが</rt></ruby>しの<ruby>湯<rt>ゆ</rt></ruby>を<ruby>無料<rt>むりょう</rt></ruby>でたのしめます。",
        "image_prefix": "onsen",
    },
    # ⑩ 既存（ラスト）：関野先生の問題
    {
        "q": "<ruby>関野<rt>せきの</rt></ruby><ruby>先生<rt>せんせい</rt></ruby>はかっこいい。○か×か",
        "opts": ["〇", "×"],
        "ans": "〇",
        "exp": "<ruby>関野<rt>せきの</rt></ruby><ruby>先生<rt>せんせい</rt></ruby>はとってもかっこいいです！",
        "image_prefix": None,  # 出題時には画像なし（回答後に結果画像を表示）
        "result_images": {
            "correct": "tenshi",  # 正解（〇）：天使のイラスト
            "incorrect": "enma",  # 不正解（×）：エンマ大王のイラスト
        },
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
    st.subheader(
        f"あなたのスコア: {total_q} もん ちゅう {st.session_state.score} もん せいかい"
    )

    if st.button(
        "さいしょから もういちど ちょうせんする", type="primary", key="restart"
    ):
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
    if q_data.get("image_prefix"):
        img = get_quiz_image(q_data["image_prefix"])
        if img is not None:
            st.image(img, use_container_width=True)

    # 問題文
    st.markdown(f"### {q_data['q']}", unsafe_allow_html=True)

    # 回答エリア
    answer_container = st.container()

    with answer_container:
        if not st.session_state.answered:
            # 回答選択用ボタン
            for i, opt in enumerate(q_data["opts"]):
                if st.button(
                    opt, key=f"q_{current_idx}_opt_{i}", use_container_width=True
                ):
                    st.session_state.selected_opt = opt
                    st.session_state.answered = True
                    if opt == q_data["ans"]:
                        st.session_state.score += 1
                    st.rerun()
        else:
            # 回答後：結果と解説の表示
            user_choice = st.session_state.selected_opt
            is_correct = user_choice == q_data["ans"]

            if is_correct:
                st.success(f"⭕️ せいかい！ （あなたのこたえ: {user_choice}）")
            else:
                st.error(
                    f"❌ ざんねん... 不正解（ふせいかい） （あなたのこたえ: {user_choice} / せいかい: {q_data['ans']}）"
                )

            # 最終問題などの特別な結果イラスト表示処理
            if "result_images" in q_data:
                res_prefix = (
                    q_data["result_images"]["correct"]
                    if is_correct
                    else q_data["result_images"]["incorrect"]
                )
                res_img = get_quiz_image(res_prefix)
                if res_img is not None:
                    st.image(res_img, width=200)

            # 解説ボックス
            st.markdown(
                f"""
                <div class="explanation-box">
                    💡 <b>かいせつ:</b><br>{q_data['exp']}
                </div>
                """,
                unsafe_allow_html=True,
            )

            # 次の問題へ進むボタン
            if st.button(
                "つぎの もんだいへ ➔",
                type="primary",
                key=f"next_{current_idx}",
                use_container_width=True,
            ):
                st.session_state.current_q += 1
                st.session_state.answered = False
                st.session_state.selected_opt = None
                st.rerun()
