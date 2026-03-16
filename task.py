from rq.decorators import job
from redis import Redis
import os
from datetime import datetime, timezone
 
redis_conn = Redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))
 
@job('notifications', connection=redis_conn)
def send_notification(notification_id, email, message):
    print(f"[Worker] Starting notification {notification_id} to {email}...")
    time.sleep(3)
    sent_at = datetime.now(timezone.utc).isoformat()
    print(f"[Worker] Done sending notification {notification_id} at {sent_at}")
 
    return {
        "notification_id": notification_id,
        "email": email,
        "status": "sent",
        "sent_at": sent_at,
    }
 