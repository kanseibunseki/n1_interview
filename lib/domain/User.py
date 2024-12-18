class User:
    def __init__(self, name="", age=0, uid=0, occupation="", survey_id_list=None, email=""):
        self.name = name
        self.age = age
        self.uid = uid
        self.occupation = occupation
        self.survey_id_list = survey_id_list  # リストとして定義
        self.email = email

    # 辞書形式に変換するメソッド
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "uid": self.uid,
            "occupation": self.occupation,
            "survey_id_list": self.survey_id_list,  # リストをそのまま辞書に追加
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            age=data.get('age'),
            uid=data.get('uid'),
            occupation=data.get('occupation'),
            survey_id_list=data.get('survey_id_list', []),  # デフォルト値として空リストを設定
            email=data.get('email')
        )
