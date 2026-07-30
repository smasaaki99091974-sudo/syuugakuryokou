<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><ruby>修<rt>しゅう</rt>学<rt>がく</rt>旅<rt>りょ</rt>行<rt>こう</rt></ruby>クイズ</title>
  <style>
    /* 生徒さんが見やすく押しやすい全体デザイン */
    body {
      font-family: 'Hiragino Kaku Gothic ProN', 'メイリオ', sans-serif;
      background-color: #fff8e7;
      color: #4a3e3d;
      margin: 0;
      padding: 20px;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      box-sizing: border-box;
    }

    /* ルビ（フリガナ）の見やすさ調整 */
    ruby {
      ruby-align: center;
    }
    rt {
      font-size: 0.55em;
      color: #e65100;
      font-weight: bold;
    }

    /* クイズカード */
    .quiz-card {
      background-color: #ffffff;
      border: 4px solid #ffd54f;
      border-radius: 24px;
      padding: 25px;
      max-width: 600px;
      width: 100%;
      box-shadow: 0 8px 16px rgba(0,0,0,0.1);
      text-align: center;
    }

    /* タイトル */
    .title {
      background-color: #ffe082;
      color: #5d4037;
      padding: 12px 20px;
      border-radius: 16px;
      font-size: 1.5rem;
      font-weight: bold;
      margin-bottom: 20px;
      display: inline-block;
    }

    /* 問題文エリア */
    .question-box {
      background-color: #e1f5fe;
      border-radius: 16px;
      padding: 20px;
      font-size: 1.3rem;
      margin-bottom: 25px;
      line-height: 1.8;
      border: 2px dashed #81d4fa;
    }

    /* 選択肢ボタンのリスト */
    .options {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }

    /* ボタン共通スタイル */
    .btn {
      background-color: #a5d6a7;
      color: #1b5e20;
      border: none;
      border-radius: 16px;
      padding: 16px 20px;
      font-size: 1.2rem;
      font-weight: bold;
      cursor: pointer;
      transition: transform 0.1s, background-color 0.2s;
      box-shadow: 0 4px 0 #66bb6a;
    }

    .btn:hover {
      background-color: #81c784;
    }

    .btn:active {
      transform: translateY(4px);
      box-shadow: none;
    }

    /* 正解・不正解の表示 */
    .result-box {
      font-size: 1.3rem;
      font-weight: bold;
      margin-top: 20px;
      padding: 15px;
      border-radius: 16px;
      line-height: 1.6;
    }

    .correct {
      background-color: #c8e6c9;
      color: #2e7d32;
    }

    .incorrect {
      background-color: #ffcdd2;
      color: #c62828;
    }

    /* 次へ進むボタン */
    .next-btn {
      background-color: #ffab91;
      color: #d84315;
      box-shadow: 0 4px 0 #ff7043;
      margin-top: 20px;
      width: 100%;
    }

    .next-btn:hover {
      background-color: #ff8a65;
    }

    .hidden {
      display: none;
    }
  </style>
</head>
<body>

  <div class="quiz-card">
    <div class="title">
      <ruby>修<rt>しゅう</rt>学<rt>がく</rt>旅<rt>りょ</rt>行<rt>こう</rt></ruby>クイズ
    </div>

    <!-- クイズ画面 -->
    <div id="quiz-screen">
      <div id="question-number" style="font-size: 1.1rem; margin-bottom: 10px; color: #795548;"></div>
      <div id="question-text" class="question-box"></div>
      <div id="options-container" class="options"></div>
      <div id="result-message" class="result-box hidden"></div>
      <button id="next-button" class="btn next-btn hidden" onclick="nextQuestion()">
        <ruby>次<rt>つぎ</rt></ruby>の<ruby>問<rt>もん</rt>題<rt>だい</rt></ruby>へ ➔
      </button>
    </div>

    <!-- 結果画面 -->
    <div id="score-screen" class="hidden">
      <h2 style="font-size: 1.8rem; color: #e65100;">
        🎉 クイズ<ruby>終<rt>お</rt></ruby>わり！ 🎉
      </h2>
      <p id="final-score" style="font-size: 1.5rem; margin: 25px 0;"></p>
      <button class="btn" style="background-color: #ffe082; color: #5d4037; box-shadow: 0 4px 0 #ffca28; width: 100%;" onclick="restartQuiz()">
        もう<ruby>一<rt>いち</rt>度<rt>ど</rt></ruby>挑戦する！
      </button>
    </div>
  </div>

  <script>
    // すべての漢字にフリガナ（rubyタグ）を付けたクイズデータ
    const quizData = [
      {
        question: "<ruby>旅<rt>たび</rt></ruby>の<ruby>荷<rt>に</rt>物<rt>もつ</rt></ruby>をつめるとき、いちばん<ruby>大<rt>だい</rt>事<rt>じ</rt></ruby>なことはなにかな？",
        options: [
          "<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>で<ruby>準<rt>じゅん</rt>備<rt>び</rt></ruby>をする",
          "おもちゃをたくさんつめる",
          "おうちの<ruby>人<rt>ひと</rt></ruby>にぜんぶやってもらう"
        ],
        answerIndex: 0,
        explanation: "正解！<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>の<ruby>荷<rt>に</rt>物<rt>もつ</rt></ruby>は<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>で<ruby>準<rt>じゅん</rt>備<rt>び</rt></ruby>すると、どこに何があるかわかるね！"
      },
      {
        question: "<ruby>集<rt>しゅう</rt>合<rt>ごう</rt></ruby><ruby>時<rt>じ</rt>刻<rt>こく</rt></ruby>のどれくらいまえに<ruby>着<rt>つ</rt></ruby>くとあんしんかな？",
        options: [
          "<ruby>直<rt>ちょく</rt>前<rt>ぜん</rt></ruby>（１<ruby>分<rt>ふん</rt></ruby>まえ）",
          "５<ruby>分<rt>ふん</rt></ruby>～１０<ruby>分<rt>ふん</rt></ruby>まえ",
          "３０<ruby>分<rt>ふん</rt></ruby>あとに<ruby>着<rt>つ</rt></ruby>く"
        ],
        answerIndex: 1,
        explanation: "正解！５<ruby>分<rt>ふん</rt></ruby>～１０<ruby>分<rt>ふん</rt></ruby>まえに<ruby>着<rt>つ</rt></ruby>くと、ゆとりをもって<ruby>行<rt>こう</rt>動<rt>どう</rt></ruby>できるね！"
      },
      {
        question: "バスや<ruby>電<rt>でん</rt>車<rt>しゃ</rt></ruby>のなかでのマナーで正しいものはどれかな？",
        options: [
          "<ruby>大<rt>おお</rt></ruby>きな<ruby>声<rt>こえ</rt></ruby>ではしゃぐ",
          "<ruby>静<rt>しず</rt></ruby>かにすごす",
          "おかしをちらかす"
        ],
        answerIndex: 1,
        explanation: "正解！みんなが<ruby>使<rt>つか</rt></ruby>う<ruby>場<rt>ば</rt>所<rt>しょ</rt></ruby>では<ruby>静<rt>しず</rt></ruby>かにするのがマナーだね！"
      },
      {
        question: "<ruby>体<rt>からだ</rt></ruby>の<ruby>調<rt>ちょう</rt>子<rt>し</rt></ruby>が悪くなったときは、どうすればいいかな？",
        options: [
          "<ruby>我<rt>が</rt>慢<rt>まん</rt></ruby>する",
          "すぐ<ruby>先<rt>せん</rt>生<rt>せい</rt></ruby>や看護師さんに<ruby>話<rt>はな</rt></ruby>す",
          "だまってどこかへ行く"
        ],
        answerIndex: 1,
        explanation: "正解！がまんしないで、すぐに<ruby>先<rt>せん</rt>生<rt>せい</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えようね！"
      }
    ];

    let currentQuestionIndex = 0;
    let score = 0;

    function showQuestion() {
      const q = quizData[currentQuestionIndex];
      document.getElementById("question-number").innerHTML = `だい ${currentQuestionIndex + 1} <ruby>問<rt>もん</rt></ruby> / ぜんぶで ${quizData.length} <ruby>問<rt>もん</rt></ruby>`;
      document.getElementById("question-text").innerHTML = q.question;
      
      const optionsContainer = document.getElementById("options-container");
      optionsContainer.innerHTML = "";
      
      document.getElementById("result-message").classList.add("hidden");
      document.getElementById("next-button").classList.add("hidden");

      q.options.forEach((opt, index) => {
        const btn = document.createElement("button");
        btn.className = "btn";
        btn.innerHTML = opt;
        btn.onclick = () => checkAnswer(index);
        optionsContainer.appendChild(btn);
      });
    }

    function checkAnswer(selectedIndex) {
      const q = quizData[currentQuestionIndex];
      const resultBox = document.getElementById("result-message");
      const buttons = document.querySelectorAll("#options-container .btn");

      buttons.forEach(btn => btn.disabled = true);

      if (selectedIndex === q.answerIndex) {
        score++;
        resultBox.className = "result-box correct";
        resultBox.innerHTML = `⭕ <strong>せいかい！</strong><br>${q.explanation}`;
      } else {
        resultBox.className = "result-box incorrect";
        resultBox.innerHTML = `❌ <strong>ざんねん！</strong><br>${q.explanation}`;
      }

      resultBox.classList.remove("hidden");
      document.getElementById("next-button").classList.remove("hidden");
    }

    function nextQuestion() {
      currentQuestionIndex++;
      if (currentQuestionIndex < quizData.length) {
        showQuestion();
      } else {
        showScoreScreen();
      }
    }

    function showScoreScreen() {
      document.getElementById("quiz-screen").classList.add("hidden");
      document.getElementById("score-screen").classList.remove("hidden");
      document.getElementById("final-score").innerHTML = 
        `${quizData.length} <ruby>問<rt>もん</rt></ruby> ちゅう <strong>${score}</strong> <ruby>問<rt>もん</rt></ruby> せいかいできたよ！`;
    }

    function restartQuiz() {
      currentQuestionIndex = 0;
      score = 0;
      document.getElementById("score-screen").classList.add("hidden");
      document.getElementById("quiz-screen").classList.remove("hidden");
      showQuestion();
    }

    // アプリ起動
    showQuestion();
  </script>

</body>
</html>
