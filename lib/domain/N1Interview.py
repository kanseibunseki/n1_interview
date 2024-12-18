class N1Interview:
    def __init__(self, theme, purpose, timestamp, interviewId, participant_count):
        self.theme = theme
        self.purpose = purpose
        self.timestamp = timestamp
        self.interviewId = interviewId
        self.participant_count = participant_count

    # 辞書形式に変換するメソッド
    def to_dict(self):
        return {
            "theme": self.theme,
            "purpose": self.purpose,
            "timestamp": self.timestamp,
            "interviewId": self.interviewId,
            "participant_count": self.participant_count,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            theme=data.get('theme'),
            purpose=data.get('purpose'),
            timestamp=data.get('timestamp'),
            interviewId=data.get('interviewId'),
            participant_count=data.get('participant_count', 0)  # デフォルト値として0を設定
        )
