class InterviewContext:
    def __init__(self, contexts, interviewId, theme, timestamp):
        self.contexts = contexts  # list型
        self.interviewId = interviewId
        self.theme = theme
        self.timestamp = timestamp

    # 辞書形式に変換するメソッド
    def to_dict(self):
        return {
            "contexts": self.contexts,
            "interviewId": self.interviewId,
            "theme": self.theme,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            contexts=data.get('contexts', []),  # デフォルト値として空リストを設定
            interviewId=data.get('interviewId'),
            theme=data.get('theme'),
            timestamp=data.get('timestamp')
        )
