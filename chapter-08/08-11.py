showMessages = [
    "ohayo gozaimasu",
    "arigato senpai",
    "onii chan i love you",
    "good morning world",
    "i love python",
]

sendMessages = []


def show_messages(messages, workList):

    for message in messages:
        print(message)
        workList.append(message)
        showMessages.remove(message)


show_messages(showMessages[:], sendMessages)


def sent_messages(workList):
    for work in workList:
        print(work)


sent_messages(sendMessages[:])


print(sendMessages)
