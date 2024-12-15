import os
import base64
from io import BytesIO
import tempfile

from openai import OpenAI
from gtts import gTTS
from pydub import AudioSegment

class AudioProcessor:
    """音声関連の処理を扱うクラス"""
    @staticmethod
    def speech_to_text(audio_bytes):
        # OpenAIクライアントの初期化
        client = OpenAI()

        # 一時ファイルに音声データを書き込む
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio.write(audio_bytes)
            temp_audio_path = temp_audio.name

        try:
            # Whisper APIを使用して音声をテキストに変換
            with open(temp_audio_path, "rb") as audio_file:
                response = client.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-1"
                )
            return response.text  # テキスト部分を返す
        finally:
            # 一時ファイルを削除
            os.unlink(temp_audio_path)

    @staticmethod
    def text_to_speech(text):
        """テキストを音声に変換し、速度を少し上げる"""
        tts = gTTS(text=text, lang='ja')
        audio_io = BytesIO()
        tts.write_to_fp(audio_io)
        audio_io.seek(0)
        
        audio = AudioSegment.from_file(audio_io, format="mp3")
        faster_audio = audio.speedup(playback_speed=1.2)
        
        buffer = BytesIO()
        faster_audio.export(buffer, format="mp3")
        audio_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        return f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_base64}"></audio>'
