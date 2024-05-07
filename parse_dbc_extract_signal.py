def group_messages_by_sender(dbc):
    sender_messages = {}
    for message in dbc.messages:
        sender = message.senders[0] if message.senders else "Unknown"
        if sender not in sender_messages:
            sender_messages[sender] = []
        sender_messages[sender].append(message)
    return sender_messages
