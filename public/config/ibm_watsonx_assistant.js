window.watsonAssistantChatOptions = {
    integrationID: "d86cf14f-35cf-4acc-9a10-099e76afcec6", // The ID of this integration.
    region: "eu-de", // The region your integration is hosted in.
    serviceInstanceID: "3dcdfd74-28c4-4b07-a6ec-d5058ec59a8f", // The ID of your service instance.
    onLoad: async (instance) => { await instance.render(); }
};
setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/latest/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
});