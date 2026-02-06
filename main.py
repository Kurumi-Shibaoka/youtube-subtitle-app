from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def youtube_url(url: str) -> str | None:
    '''
    YouTubeのURLから動画IDを取得する
    '''
    try:
        return YouTube(url).video_id  # ex) "JlgT56YU8gc"
    except RegexMatchError:
        return None
    except Exception:
        return None

def get_subtitle_text(language_code: str, transcript_list: list) -> str | None:
    '''
    指定した言語コード（ja / ko）の字幕テキストを返す
    '''
    for transcript in transcript_list:
        if transcript.language_code == language_code:
            return '\n'.join([item.text for item in transcript.fetch()])
    return None

@app.route("/app/subtitle",methods=["POST","OPTIONS"])
def subtitle_api():
    '''
    YouTube字幕を取得してJSONで返すAPI
    '''
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json()
    url = data.get("url")
    lang = data.get("lang")

    video_id = youtube_url(url)
    if not video_id:
        return jsonify({"error":"youtubeのURLを確認してください。"}),400

    api = YouTubeTranscriptApi()
    transcript_list = api.list(video_id)

    text = get_subtitle_text(lang, transcript_list)
    return jsonify({
        "text": text
    })

if __name__=="__main__":
    app.run(debug=True)


