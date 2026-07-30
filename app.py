<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ちほうの なまえ クイズ</title>
  <style>
    body {
      font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif;
      background-color: #fff9e6; /* かわいいパステルイエロー */
      color: #555;
      text-align: center;
      padding: 20px;
      margin: 0;
    }

    h1 {
      color: #ff8c00;
      font-size: 28px;
      background-color: #ffffff;
      padding: 15px;
      border-radius: 20px;
      display: inline-block;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      border: 3px dashed #ffb74d;
    }

    .quiz-container {
      background-color: #ffffff;
      max-width: 500px;
      margin: 20px auto;
      padding: 25px;
      border-radius: 25px;
      box-shadow: 0 8px 16px rgba(0,0,0,0.1);
      border: 4px solid #ffd54f;
    }

    .question {
      font-size: 22px;
      font-weight: bold;
      margin-bottom: 15px;
      color: #333;
    }

    /* フリガナ（ruby）を見やすく調整 */
    ruby {
      ruby-position: over;
    }
    rt {
      font-size: 11px;
      color: #e65100;
    }

    .quiz-image {
      max-width: 100%;
      height: auto;
      max-height: 200px;
      border-radius: 15px;
      margin-bottom: 20px;
      border: 3px solid #ffe082;
    }

    .options {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .option-btn {
      background-color: #81c784; /* パステルグリーン */
      color: white;
      border: none;
      padding: 12px 20px;
      font-size: 18px;
      font-weight: bold;
      border-radius: 15px;
      cursor: pointer;
      transition: transform 0.1s, background-color 0.2s;
      box-shadow: 0 4px 0 #66bb6a;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }

    .option-btn:hover {
      background-color: #66bb6a;
    }

    .option-btn:active {
      transform: translateY(4px);
      box-shadow: none;
    }

    /* ボタンの中の画像サイズ */
    .option-img {
      max-height: 40px;
      width: auto;
      border-radius: 5px;
    }

    .result {
      margin-top: 20px;
      font-size: 24px;
      font-weight: bold;
      min-height: 36px;
    }

    .correct {
      color: #ff4081; /* かわいいピンク */
    }

    .incorrect {
      color: #1e88e5; /* 爽やかなブルー */
    }

    .next-btn {
      margin-top: 20px;
      background-color: #ff8a65;
      color: white;
      border: none;
      padding: 10px 25px;
      font-size: 18px;
      font-weight: bold;
      border-radius: 20px;
      cursor: pointer;
      box-shadow: 0 4px 0 #e64a19;
      display: none;
    }

    .next-btn:active {
      transform: translateY(4px);
      box-shadow: none;
    }
  </style>
</head>
<body>

  <h1>🗾 にほんの <ruby>地方<rt>ちほう</rt></ruby> クイズ 🗾</h1>

  <div class="quiz-container">
    <div id="question" class="question"></div>
    <div id="image-container"></div>
    <div id="options" class="options"></div>
    <div id="result" class="result"></div>
    <button id="next-btn" class="next-btn" onclick="nextQuestion()">つぎの <ruby>問題<rt>もんだい</rt></ruby>へ</button>
  </div>

  <script>
    // クイズのデータ構造（問題ごとに画像や選択肢画像を設定可能）
    const quizData = [
      {
        question: "1問目：<ruby>日本<rt>にほん</rt></ruby>で いちばん <ruby>北<rt>きた</rt></ruby>にある <ruby>地方<rt>ちほう</rt></ruby>は どこかな？",
        image: null,
        options: [
          { text: "<ruby>北海道<rt>ほっかいどう</rt></ruby><ruby>地方<rt>ちほう</rt></ruby>", image: null },
          { text: "<ruby>九州<rt>きゅうしゅう</rt></ruby><ruby>地方<rt>ちほう</rt></ruby>", image: null },
          { text: "<ruby>関東<rt>かんとう</rt></ruby><ruby>地方<rt>ちほう</rt></ruby>", image: null }
        ],
        answer: 0
      },
      {
        question: "2問目：とうきょうや かながわが ある <ruby>地方<rt>ちほう</rt></ruby>は どこかな？",
        image: null,
        options: [
          { text: "<ruby>近畿<rt>きんき</rt></ruby><ruby>地方<rt>ちほう</rt></ruby>", image: null },
          { text: "<ruby>関東<rt>かんとう</rt></ruby><ruby>地方<rt>ちほう</rt></ruby>", image: null },
          { text: "<ruby>東北<rt>とうほく</rt></ruby><ruby>地方<rt>ちほう</rt></ruby>", image: null }
        ],
        answer: 1
      },
      {
        question: "3問目：この <ruby>地方<rt>ちほう</rt></ruby>の なまえは なにかな？",
        image: "hokuriku.png", // 問題画像
        options: [
          { text: "<ruby>北陸<rt>ほくりく</rt></ruby><ruby>地方<rt>ちほう</rt></ruby>", image: null },
          { text: "<ruby>東海<rt>とうかい</rt></ruby><ruby>地方<rt>ちほう</rt></ruby>", image: null },
          { text: "<ruby>関東<rt>かんとう</rt></ruby><ruby>地方<rt>ちほう</rt></ruby>", image: "higasi.png" } // 解答（選択肢）の画像
        ],
        answer: 0
      }
    ];

    let currentQuiz = 0;

    const questionEl = document.getElementById('question');
    const imageContainerEl = document.getElementById('image-container');
    const optionsEl = document.getElementById('options');
    const resultEl = document.getElementById('result');
    const nextBtn = document.getElementById('next-btn');

    function loadQuiz() {
      // 画面のリセット
      resultEl.innerHTML = '';
      nextBtn.style.display = 'none';
      optionsEl.innerHTML = '';
      imageContainerEl.innerHTML = '';

      const currentQuizData = quizData[currentQuiz];

      // 問題文の設定
      questionEl.innerHTML = currentQuizData.question;

      // 問題画像の表示（画像が指定されている場合のみ）
      if (currentQuizData.image) {
        const img = document.createElement('img');
        img.src = currentQuizData.image;
        img.alt = "問題の画像";
        img.className = "quiz-image";
        imageContainerEl.appendChild(img);
      }

      // 選択肢ボタンの作成
      currentQuizData.options.forEach((option, index) => {
        const button = document.createElement('button');
        button.className = 'option-btn';
        
        // テキストを設定
        const textSpan = document.createElement('span');
        textSpan.innerHTML = option.text;
        button.appendChild(textSpan);

        // 選択肢の中に画像が指定されている場合（3問目のhigasi画像など）
        if (option.image) {
          const optImg = document.createElement('img');
          optImg.src = option.image;
          optImg.alt = "選択肢の画像";
          optImg.className = "option-img";
          button.appendChild(optImg);
        }

        button.onclick = () => selectOption(index);
        optionsEl.appendChild(button);
      });
    }

    function selectOption(selectedIndex) {
      const currentQuizData = quizData[currentQuiz];
      const buttons = optionsEl.querySelectorAll('.option-btn');

      // ボタンの無効化
      buttons.forEach(btn => btn.disabled = true);

      if (selectedIndex === currentQuizData.answer) {
        resultEl.innerHTML = '<span class="correct">⭕ せいかい！ すごいね！</span>';
      } else {
        resultEl.innerHTML = '<span class="incorrect">❌ ざんねん！ もういちど かんがえてみよう！</span>';
      }

      nextBtn.style.display = 'inline-block';
    }

    function nextQuestion() {
      currentQuiz++;
      if (currentQuiz < quizData.length) {
        loadQuiz();
      } else {
        // 全問終了時
        questionEl.innerHTML = "🎉 クイズ しゅうりょう！";
        imageContainerEl.innerHTML = '';
        optionsEl.innerHTML = '<p style="font-size:20px; font-weight:bold;">ぜんぶの もんだいが おわったよ！<br>よく がんばったね！</p>';
        resultEl.innerHTML = '';
        nextBtn.style.display = 'none';
      }
    }

    // 初回読み込み
    loadQuiz();
  </script>
</body>
</html>
