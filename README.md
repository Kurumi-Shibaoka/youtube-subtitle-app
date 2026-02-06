# YouTube 字幕取得アプリ

※ 本アプリは学習目的で作成したものです。

## 概要
YouTubeのURLと言語を指定すると、
字幕テキストを取得して表示するWebアプリです。

このアプリは、訓練校にてWebアプリ開発の学習の一環として
初めて作成した作品です。

///////////// Sample URL /////////////

https://youtu.be/JlgT56YU8gc?si=RNG-fKAwpaduh4wf
https://www.youtube.com/watch?v=JlgT56YU8gc
上記のURLどちらからでもIDの11文字を取得可能 ex) "JlgT56YU8gc"

---

## 機能
- YouTube URL入力
- 言語選択（日本語 / 韓国語）
- 字幕データの取得
- 字幕テキストの表示

---

## 使用技術

### フロントエンド
- HTML
- CSS
- JavaScript
- Fetch API（非同期通信）

### バックエンド
- Python
- Flask

### ライブラリ
- youtube-transcript-api
- pytube

---

## 画面イメージ
- URL入力フォーム
- 言語選択（ラジオボタン）
- 字幕表示エリア

---

## 補足
初めて作成したWebアプリのため、
シンプルな構成を意識しています。
当時、韓国語の番組をよく観ていたので韓国語を選びました。

フロントエンドとAPIを分けて実装することで、
Webアプリの基本的な構造を理解することを目的としました。
