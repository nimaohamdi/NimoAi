import { CONFIG } from './config.js';
import { UI } from './ui.js';
import { ChatManager } from './chat.js';

class NimoAI {
    constructor() {
        this.chatManager = new ChatManager();
        this.settings = this.loadSettings();
        this.init();
    }

    loadSettings() {
        return JSON.parse(localStorage.getItem(CONFIG.STORAGE_KEYS.SETTINGS)) || {
            apiToken: "",
            model: CONFIG.DEFAULT_MODEL
        };
    }

    saveSettings() {
        localStorage.setItem(CONFIG.STORAGE_KEYS.SETTINGS, JSON.stringify(this.settings));
    }

    init() {
        this.chatManager.loadChats();
        if (this.chatManager.chats.length === 0) {
            this.chatManager.createNewChat();
        } else {
            this.chatManager.currentChatId = this.chatManager.chats[0].id;
        }

        this.renderAll();
        this.attachEventListeners();
    }

    renderAll() {
        UI.renderChatList(
            this.chatManager.chats, 
            this.chatManager.currentChatId,
            'window.switchChat'
        );
        this.renderCurrentChat();
    }

    renderCurrentChat() {
        const chat = this.chatManager.getCurrentChat();
        if (!chat) return;

        UI.elements.currentTitle.textContent = chat.title || CONFIG.APP_NAME;
        
        UI.elements.chatArea.innerHTML = chat.messages.map(msg => `
            <div class="message ${msg.role === 'user' ? 'user-message' : 'bot-message'}">
                ${msg.content.replace(/\n/g, '<br>')}
            </div>
        `).join('');

        UI.scrollToBottom();
    }

    attachEventListeners() {
        UI.elements.newChatBtn.addEventListener('click', () => {
            this.chatManager.createNewChat();
            this.renderAll();
        });

        UI.elements.sendBtn.addEventListener('click', () => this.sendMessage());
        
        UI.elements.userInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
    }

    async sendMessage() {
        // Implementation of streaming + API call (we'll expand this next)
        console.log("Send message triggered - ready for expansion");
    }
}

// Global functions for onclick handlers
window.switchChat = (id) => {
    window.nimoAI.chatManager.currentChatId = id;
    window.nimoAI.renderAll();
};

// Initialize App
window.addEventListener('load', () => {
    window.nimoAI = new NimoAI();
});