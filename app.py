import os
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="金沢・福井 修学旅行クイズ", page_icon="🏯", layout="centered"
)


# ---- 各問題の画像（写真）を読み込む関数 ----
def get_quiz_image(file_prefix):
    # .jpg または .png の両方の拡張子に対応
    jpg_path = f"{file_prefix}.jpg"
    png_path = f"{file_prefix}.png"

    if os.path.exists(jpg_path):
        return Image.open(jpg_path)
    elif os.path.exists(png_path):
        return Image.open(png_path)
    else:
        # ファイルがない場合は案内用ダミーテキストを表示（エラーで止まらないようにする）
        st.warning(
            f"画像ファイル '{file_prefix}.jpg' (または .png) が見つかりません。GitHubにアップロードしてください。"
        )
        return None


# ---- クイズのデータ（各問題に対応する画像ファイル名のプレフィックスを指定） ----
quiz_list = [
    {
        "q": "ひがし茶屋街の美しい建物に見られる、外から中が見えにくく、中から外が見えやすい木製の格子（こうし）を何と呼ぶでしょう？",
        "opts": ["A: 出格子", "B: 木虫籠（きむすこ）", "C: 千本格子"],
        "ans": "B: 木虫籠（きむすこ）",
        "exp": "金沢の町家特有の細い木格子のことで、光を取り入れつつプライバシーを守る工夫がされています。",
        "image_prefix": "kimusuko",
    },
    {
        "q": "越前松島水族館で大人気の、透明なアクリルガラスの上に寝転がって海の上に浮いているような体験ができるコーナーの名前は？",
        "opts": ["A: さんごの海", "B: 海の浮島", "C: 水上さんぽ"],
        "ans": "A: さんごの海",
        "exp": "床一面が透明なガラス張りになっていて、魚たちが泳ぐプールの上に寝そべることができます。",
        "image_prefix": "aquarium",
    },
    {
        "q": "福井県勝山市で発見され、名前にも「フクイ」とついている肉食恐竜の名前は次のうちどれでしょう？",
        "opts": ["A: フクイサウルス", "B: フクイティタン", "C: フクイラプトル"],
        "ans": "C: フクイラプトル",
        "exp": "フクイラプトルは福井県で発見された肉食恐竜です（フクイサウルスは草食恐竜です）。",
        "image_prefix": "museum",
    },
    {
        "q": "あわら温泉の湯まち広場にある、無料で誰でも気軽に楽しめる人気スポットは何でしょう？",
        "opts": ["A: 足湯", "B: 温泉卵作り場", "C: 温泉プール"],
        "ans": "A: 足湯",
        "exp": "あわら温泉の足湯は複数の浴槽があり、源泉かけ流しの湯を無料で楽しめます。",
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

st.title("🏯 金沢・福井 修学旅行クイズ")

total_q = len(quiz_list)
current_idx = st.session_state.current_q

# ---- 全問題終了画面 ----
if current_idx >= total_q:
    st.balloons()
    st.header("🎉 クイズ終了！")
    st.subheader(f"あなたのスコア: {total_q} 問中 {st.session_state.score} 問正解")

    if st.button("最初からもう一度挑戦する", type="primary"):
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
    st.caption(f"第 {current_idx + 1} 問 / 全 {total_q} 問")

    # 画像の取得と表示
    img = get_quiz_image(q_data["image_prefix"])
    if img is not None:
        st.image(img, use_container_width=True)

    # 問題文
    st.markdown(f"### {q_data['q']}")

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
            st.success(f"⭕️ 正解！ （あなたの答え: {user_choice}）")
        else:
            st.error(
                f"❌ 不正解... （あなたの答え: {user_choice} / 正解: {q_data['ans']}）"
            )

        st.info(f"💡 **解説:** {q_data['exp']}")

        # 次の問題へ進むボタン
        if st.button("次の問題へ ➔", type="primary", use_container_width=True):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.selected_opt = None
            st.rerun()
