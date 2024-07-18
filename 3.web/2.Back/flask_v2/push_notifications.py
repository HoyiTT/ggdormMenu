from pyfcm import FCMNotification

# FCM 서버 키
fcm_server_key = "Y16656c2970f104a906cb580135b4057c0150f881"

def send_push_notification(device_token, title, message):
    push_service = FCMNotification(api_key=fcm_server_key)

    registration_id = device_token
    message_title = title
    message_body = message

    result = push_service.notify_single_device(registration_id=registration_id,
                                              message_title=message_title,
                                              message_body=message_body)

    return result