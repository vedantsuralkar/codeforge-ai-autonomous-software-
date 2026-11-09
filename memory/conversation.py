
from langchain_core.chat_history import InMemoryChatMessageHistory


# ==========================================
# CONVERSATION MEMORY
# ==========================================

class ConversationMemory:

    def __init__(self):

        self.sessions = {}

    # ======================================
    # GET OR CREATE SESSION
    # ======================================

    def get_session(self, session_id):

        if session_id not in self.sessions:

            self.sessions[session_id] = (
                InMemoryChatMessageHistory()
            )

        return self.sessions[session_id]

    # ======================================
    # SAVE USER MESSAGE
    # ======================================

    def add_user_message(self, session_id, message):

        history = self.get_session(session_id)

        history.add_user_message(message)

    # ======================================
    # SAVE AI RESPONSE
    # ======================================

    def add_ai_message(self, session_id, message):

        history = self.get_session(session_id)

        history.add_ai_message(message)

    # ======================================
    # GET CONVERSATION HISTORY
    # ======================================

    def get_history(self, session_id):

        history = self.get_session(session_id)

        return history.messages

    # ======================================
    # CLEAR MEMORY
    # ======================================

    def clear_history(self, session_id):

        if session_id in self.sessions:

            self.sessions[session_id].clear()

            return "Conversation cleared!"

        return "Session not found!"


# ==========================================
# CREATE MEMORY OBJECT
# ==========================================

conversation_memory = ConversationMemory()
