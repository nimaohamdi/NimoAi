export class ChatManager {
    constructor() {
        this.chats = [];
        this.currentChatId = null;
    }

    loadChats() {
        this.chats = JSON.parse(localStorage.getItem(CONFIG.STORAGE_KEYS.CHATS)) || [];
    }

    saveChats() {
        localStorage.setItem(CONFIG.STORAGE_KEYS.CHATS, JSON.stringify(this.chats));
    }

    createNewChat() {
        const chat = {
            id: Date.now().toString(36),
            title: "New Conversation",
            messages: [],
            createdAt: Date.now()
        };
        this.chats.unshift(chat);
        this.currentChatId = chat.id;
        this.saveChats();
        return chat;
    }

    getCurrentChat() {
        return this.chats.find(c => c.id === this.currentChatId);
    }
}