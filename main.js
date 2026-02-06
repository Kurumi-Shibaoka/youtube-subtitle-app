
document.getElementById("btn").onclick = async () => {

    // 入力されたURLを取得
    const url = document.getElementById("url").value;

    // 選択された言語を取得（ja / ko）
    const lang = document.querySelector(
    'input[name="lang"]:checked'
    ).value;

    // Flask APIへリクエスト送信
    const res = await fetch("http://127.0.0.1:5000/app/subtitle",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            url: url,
            lang: lang
        })
    });

    // レスポンス(JSON)を取得
    const data = await res.json();

    // 結果を画面に表示
    document.getElementById("result").textContent = data.text;
};