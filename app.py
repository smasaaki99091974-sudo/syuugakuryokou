import io
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="金沢・福井 修学旅行クイズ", page_icon="🏯", layout="centered"
)


# ---- 画像を自動生成する関数 ----
def generate_quiz_image(place_key):
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.axis("off")

    if place_key == "higashi":
        # ひがし茶屋街：格子風デザインと和風カラー
        fig.patch.set_facecolor("#faf0e6")
        ax.set_facecolor("#faf0e6")
        for x in np.linspace(0.1, 0.9, 15):
            ax.axvline(x, color="#8b4513", linewidth=3)
        ax.axhline(0.5, color="#8b4513", linewidth=6)
        ax.text(
            0.5,
            0.5,
            "ひがし茶屋街\n(出格子・木虫籠)",
            ha="center",
            va="center",
            fontsize=18,
            color="#4a2e18",
            weight="bold",
            bbox=dict(
                boxstyle="round,pad=0.5", facecolor="#fff8dc", edgecolor="#8b4513"
            ),
        )

    elif place_key == "aquarium":
        # 越前松島水族館：海と魚のイメージ
        fig.patch.set_facecolor("#e0f7fa")
        ax.set_facecolor("#e0f7fa")
        ax.scatter(
            [0.2, 0.4, 0.7, 0.85],
            [0.3, 0.7, 0.4, 0.8],
            s=[300, 500, 400, 250],
            color="#0288d1",
            alpha=0.6,
        )
        ax.text(
            0.5,
            0.5,
            "越前松島水族館\n(さんごの海 / 海上さんぽ)",
            ha="center",
            va="center",
            fontsize=18,
            color="#01579b",
            weight="bold",
            bbox=dict(
                boxstyle="round,pad=0.5", facecolor="#ffffff", edgecolor="#0288d1"
            ),
        )

    elif place_key == "museum":
        # 恐竜博物館：化石・太古のイメージ
        fig.patch.set_facecolor("#f5f5dc")
        ax.set_facecolor("#f5f5dc")
        ax.plot(
            [0.1, 0.3, 0.5, 0.7, 0.9],
            [0.2, 0.6, 0.3, 0.7, 0.2],
            color="#5d4037",
            lw=4,
            ls="--",
        )
        ax.text(
            0.5,
            0.5,
            "福井県立恐竜博物館\n(フクイラプトル)",
            ha="center",
            va="center",
            fontsize=18,
            color="#3e2723",
            weight="bold",
            bbox=dict(
                boxstyle="round,pad=0.5", facecolor="#fff8e1", edgecolor="#5d4037"
            ),
        )

    elif place_key == "onsen":
        # あわら温泉：温泉・和みイメージ
        fig.patch.set_facecolor("#fff3e0")
        ax.set_facecolor("#fff3e0")
        ax.text(
            0.5,
            0.5,
            "あわら温泉 湯まち広場\n(足湯)",
            ha="center",
            va="center",
            fontsize=18,
            color="#e65100",
            weight="bold",
            bbox=dict(
                boxstyle="round,pad=0.5", facecolor="#ffffff", edgecolor="#ff9800"
            ),
        )

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)


# ---- クイズのデータ ----
quiz_list = [
    {
        "q": "ひがし茶屋街の美しい建物に見られる、外から中が見えにくく、中から外が見えやすい木製の格子（こうし）を何と呼ぶでしょう？",
        "opts": ["A: 出格子", "B: 木虫籠（きむすこ）", "C: 千本格子"],
        "ans": "B: 木虫籠（きむすこ）",
        "exp": "金沢の町家特有の細い木格子のことで、光を取り入れつつプライバシーを守る工夫がされています。",
        "image_key": "higashi",
    },
    {
        "q": "越前松島水族館で大人気の、透明なアクリルガラスの上に寝転がって海の上に浮いているような体験ができるコーナーの名前は？",
        "opts": ["A: さんごの海", "B: 海の浮島", "C: 水上さんぽ"],
        "ans": "A: さんごの海",
        "exp": "床一面が透明なガラス張りになっていて、魚たちが泳ぐプールの上に寝そべることができます。",
        "image_key": "aquarium",
    },
    {
        "q": "福井県勝山市で発見され、名前にも「フクイ」とついている肉食恐竜の名前は次のうちどれでしょう？",
        "opts": ["A: フクイサウルス", "B: フクイティタン", "C: フクイラプトル"],
        "ans": "C: フクイラプトル",
        "exp": "フクイラプトルは福井県で発見された肉食恐竜です（フクイサウルスは草食恐竜です）。",
        "image_key": "museum",
    },
    {
        "q": "あわら温泉の湯まち広場にある、無料で誰でも気軽に楽しめる人気スポットは何でしょう？",
        "opts": ["A: 足湯", "B: 温泉卵作り場", "C: 温泉プール"],
        "ans": "A: 足湯",
        "exp": "あわら温泉の足湯は複数の浴槽があり、源泉かけ流しの湯を無料で楽しめます。",
        "image_key": "onsen",
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

    # 関連イラスト画像の表示
    img = generate_quiz_image(q_data["image_key"])
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
    
