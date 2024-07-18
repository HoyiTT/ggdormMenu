self.addEventListener('install', event => {
    console.log('Service Worker installing.');
    self.skipWaiting();
});

self.addEventListener('activate', event => {
    console.log('Service Worker activating.');
});

self.addEventListener('push', event => {
    let data = event.data.json();
    const options = {
        body: data.body,
        icon: 'icon.png',
        badge: 'badge.png',
        tag: 'push-notification-tag',
        data: { url: data.url }
    };
    event.waitUntil(
        self.registration.showNotification(data.title, options)
    );
});

self.addEventListener('notificationclick', event => {
    event.notification.close();
    event.waitUntil(
        clients.openWindow(event.notification.data.url)
    );
});
