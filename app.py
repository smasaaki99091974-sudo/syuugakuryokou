import streamlit as st
import streamlit.components.v1 as components

# 画面全体のレイアウト設定
st.set_page_config(page_title="たのしい クイズアプリ", page_icon="✨", layout="centered")

# HTML / CSS / JavaScript の定義
html_code = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>たのしい クイズアプリ</title>
  <style>
    body {
      font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif;
      background-color: #FFF0F5; /* やさしいピンク */
      color: #333333;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 90vh;
      margin: 0;
      padding: 10px;
      box-sizing: border-box;
    }

    .quiz-card {
      background-color: #FFFFFF;
      border: 4px solid #FFB6C1;
      border-radius: 20px;
      padding: 20px;
      width: 100%;
      max-width: 480px;
      box-shadow: 0 8px 15px rgba(0,0,0,0.1);
      text-align: center;
    }

    h1 {
      color: #FF69B4;
      font-size: 22px;
      margin-bottom: 15px;
    }

    .question-number {
      font-size: 16px;
      font-weight: bold;
      color: #4682B4;
      margin-bottom: 10px;
    }

    .question-text {
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 20px;
      line-height: 1.6;
    }

    .options {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .option-btn {
      background-color: #E0F7FA;
      border: 2px solid #81D4FA;
      border-radius: 12px;
      padding: 12px 15px;
      font-size: 17px;
      font-weight: bold;
      color: #006064;
      cursor: pointer;
      transition: all 0.2s;
    }

    .option-btn:hover {
      background-color: #B2EBF2;
      transform: translateY(-2px);
    }

    .result-message {
      font-size: 22px;
      font-weight: bold;
      margin-top: 15px;
      min-height: 36px;
    }

    .next-btn {
      margin-top: 20px;
      background-color: #FF9800;
      color: white;
      border: none;
      border-radius: 12px;
      padding: 12px 25px;
      font-size: 17px;
      font-weight: bold;
      cursor: pointer;
      display: none;
    }

    .next-btn:hover {
      background-color: #F57C00;
    }

    ruby {
      ruby-align: center;
    }

    rt {
      font-size: 11px;
      color: #FF4081;
    }
  </style>
</head>
<body>

<div class="quiz-card">
  <h1>✨修学旅行＆恐竜クイズ✨</h1>
  <div id="quiz-area">
    <div class="question-number" id="q-num">だい1もん</div>
    <div class="question-text" id="q-text"></div>
    <div class="options" id="options-container"></div>
    <div class="result-message" id="result-msg"></div>
    <button class="next-btn" id="next-btn" onclick="nextQuestion()">つぎの もんだいへ ＞</button>
  </div>
</div>

<script>
  const quizData = [
    {
      question: "①<ruby>１日目<rt>いちにちめ</rt></ruby>に <ruby>行<rt>い</rt></ruby>くところは どこ？ 🐟",
      options: ["越前松島水族館", "福井県立恐竜博物館", "ひがし茶屋街"],
      answer: "越前松島水族館"
    },
    {
      question: "②<ruby>２日目<rt>ふつかめ</rt></ruby>に <ruby>行<rt>い</rt></ruby>くところは どこ？ 🦖",
      options: ["越前松島水族館", "福井県立恐竜博物館", "ひがし茶屋街"],
      answer: "福井県立恐竜博物館"
    },
    {
      question: "③<ruby>３日目<rt>みっかめ</rt></ruby>に <ruby>行<rt>い</rt></ruby>くところは？ 🍵",
      options: ["越前松島水族館", "福井県立恐竜博物館", "ひがし茶屋街"],
      answer: "ひがし茶屋街"
    },
    {
      question: "④ティラノサウルスの <ruby>大<rt>おお</rt></ruby>きさは？ 📏",
      options: ["１，軽自動車", "２，観光バス", "３，新幹線の車両"],
      answer: "２，観光バス"
    },
    {
      question: "⑤<ruby>福井県<rt>ふくいけん</rt></ruby>で <ruby>発見<rt>はっけん</rt></ruby>された <ruby>恐竜<rt>きょうりゅう</rt></ruby>は？ 🦴",
      options: ["１，３種類", "２，６種類", "３，１０種類"],
      answer: "２，６種類"
    },
    {
      question: "⑥<ruby>恐竜<rt>きょうりゅう</rt></ruby>の <ruby>子孫<rt>しそん</rt></ruby>は どれでしょう。 🐦",
      options: ["１，トカゲ／ワニ", "２，鳥", "３，哺乳類"],
      answer: "２，鳥"
    },
    {
      question: "⑦この キャラクターは なに？ ♨️",
      options: ["湯巡権三（ゆめぐりごんぞう）", "あわら温泉マン", "恐竜はかせ"],
      answer: "湯巡権三（ゆめぐりごんぞう）"
    },
    {
      question: "⑧<ruby>関野<rt>せきの</rt></ruby><ruby>先生<rt>せんせい</rt></ruby>の <ruby>問題<rt>もんだい</rt></ruby> 💡",
      options: ["選択肢１", "選択肢２", "選択肢３"],
      answer: "選択肢１"
    }
  ];

  let currentQuestionIndex = 0;

  function loadQuestion() {
    const currentQuiz = quizData[currentQuestionIndex];
    document.getElementById("q-num").textContent = `だい ${currentQuestionIndex + 1} もん（ぜん ${quizData.length} もん）`;
    document.getElementById("q-text").innerHTML = currentQuiz.question;
    
    const optionsContainer = document.getElementById("options-container");
    optionsContainer.innerHTML = "";
    
    document.getElementById("result-msg").textContent = "";
    document.getElementById("next-btn").style.display = "none";

    currentQuiz.options.forEach(option => {
      const button = document.createElement("button");
      button.className = "option-btn";
      button.textContent = option;
      button.onclick = () => checkAnswer(option, currentQuiz.answer);
      optionsContainer.appendChild(button);
    });
  }

  function checkAnswer(selected, correct) {
    const buttons = document.querySelectorAll(".option-btn");
    buttons.forEach(btn => btn.disabled = true);

    const resultMsg = document.getElementById("result-msg");
    if (selected === correct) {
      resultMsg.innerHTML = "<span style='color: #4CAF50;'>⭕ せいかい！</span>";
    } else {
      resultMsg.innerHTML = `<span style='color: #F44336;'>❌ ざんねん…</span><br><span style='font-size:16px; color:#555;'>せいかいは: ${correct}</span>`;
    }

    document.getElementById("next-btn").style.display = "inline-block";
  }

  function nextQuestion() {
    currentQuestionIndex++;
    if (currentQuestionIndex < quizData.length) {
      loadQuestion();
    } else {
      showFinalResult();
    }
  }

  function showFinalResult() {
    document.getElementById("quiz-area").innerHTML = `
      <h2>🎉 おつかれさまでした！ 🎉</h2>
      <p style="font-size: 20px;">ぜんぶの もんだいが おわったよ！</p>
      <button class="next-btn" style="display:inline-block;" onclick="location.reload()">もういちど チャレンジ</button>
    `;
  }

  loadQuestion();
</script>

</body>
</html>
"""

# Streamlit上でHTMLを表示（高さは650pxに設定）
components.html(html_code, height=650, scrolling=True)
