export class UI {
    static elements = {
        sidebar: document.getElementById('sidebar'),
        chatList: document.getElementById('chat-list'),
        chatArea: document.getElementById('chat-area'),
        currentTitle: document.getElementById('current-chat-title'),
        userInput: document.getElementById('user-input'),
        sendBtn: document.getElementById('send-btn'),
        newChatBtn: document.getElementById('new-chat'),
        settingsBtn: document.getElementById('settings-btn')
    };

    static renderChatList(chats, currentId, switchChatFn) {
        this.elements.chatList.innerHTML = chats.map(chat => `
            <div class="chat-item ${chat.id === currentId ? 'active' : ''}" 
                 onclick="${switchChatFn}('${chat.id}')">
                <div class="chat-title">${chat.title}</div>
                <small>${new Date(chat.createdAt).toLocaleDateString()}</small>
            </div>
        `).join('');
    }

    static scrollToBottom() {
        this.elements.chatArea.scrollTop = this.elements.chatArea.scrollHeight;
    }
}