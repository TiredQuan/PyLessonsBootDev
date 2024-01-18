def filter_messages(messages):
    filtered_messages, filtered_count = [],[]
    for message in messages: #for each message in messages
        split_message = message.split() #splitting the message into shit that we can check
        increment = 0 #increment to count swears
        for i in range(0, len(split_message)-1): #for each word in split message
            if split_message[i] == "dang": #if it is 'dang'
                split_message.pop(i) #pop it out
                increment += 1 #increment the increment
        filtered_messages.append(" ".join(split_message))
        filtered_count.append(increment)
    return filtered_messages, filtered_count