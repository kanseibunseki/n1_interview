# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage

from ..classes.InterviewConfig import InterviewConfig


class InterviewManager:
    """Manages the overall interview process"""
    def __init__(self, theme):
        self.theme = theme
        self.messages = []
        self.context = ""
        self.question_count = 0
        self.current_question = "こんにちは！音楽サブスクサービスについてのインタビューを始めましょう。"
        self.ai_response_audio_html = ""
        self.last_question_displayed = False
        self.phase = InterviewConfig.PHASES[0]

    def get_current_phase(self):
        """Determine the current interview phase"""
        phase_thresholds = [5, 10, 15, 20]
        for i, threshold in enumerate(phase_thresholds):
            if self.question_count <= threshold:
                return InterviewConfig.PHASES[i]
        return "summary"

    def get_ai_response(self, messages):
        """Get AI response using ChatOpenAI"""
        llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # response = llm(messages)
        response = llm.invoke(messages)
        return response.content

    def process_user_response(self, user_input):
        """Process user's response and generate AI response"""
        # Update messages and context
        self.messages.append(HumanMessage(content=user_input))
        self.context += f"ユーザー: {user_input}\n"
        self.question_count += 1

        # Update phase
        self.phase = self.get_current_phase()

        if self.phase != "summary":
            # Generate next question
            system_message = SystemMessage(
                content=InterviewConfig.get_template(
                    self.phase, 
                    theme=self.theme, 
                    context=self.context
                )
            )
            messages = [system_message] + self.messages
            ai_response = self.get_ai_response(messages)
            
            self.messages.append(AIMessage(content=ai_response))
            self.context += f"AI: {ai_response}\n"
            self.current_question = ai_response
        else:
            # Generate summary
            summary = self.get_ai_response([
                SystemMessage(
                    content=InterviewConfig.get_template(
                        "summary",
                        theme=self.theme, 
                        context=self.context
                    )
                )
            ])
            return summary

        return None