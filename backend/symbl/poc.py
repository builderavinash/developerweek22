import symbl
import json
from os.path import exists

DATA_TYPE_ALL = "all"
DATA_TYPE_ACTION_ITEMS = "action_items"
DATA_TYPE_TOPICS = "topics"
DATA_TYPE_FOLLOW_UPS = "follow_ups"
DATA_TYPE_QUESTIONS = "questions"
DATA_TYPES=[DATA_TYPE_ALL, DATA_TYPE_ACTION_ITEMS, DATA_TYPE_TOPICS, DATA_TYPE_FOLLOW_UPS, DATA_TYPE_QUESTIONS]

def getFileName(data_type):
    return "mockdata/%s.output" % (data_type)

def saveAndReturn(data_type, data):
    file=open(getFileName(data_type), 'w')
    file.write(json.dumps(data.to_dict(), default=str))
    file.close()
    return data

# Process audio file
def processAudio(mock=True, local_path="", data_type="all"):
    outputFile=getFileName(data_type)

    if mock:
        if exists(outputFile):
            return open(outputFile).read()
    if len(local_path) == 0:
        local_path = r'i-want-to-work-2.mp3'

    conversation_object = symbl.Audio.process_file(
        file_path=local_path)

    if data_type == DATA_TYPE_ALL:
        return saveAndReturn(data_type, conversation_object.get_messages())
    elif data_type == DATA_TYPE_ACTION_ITEMS:
        return saveAndReturn(data_type, conversation_object.get_action_items())
    elif data_type == DATA_TYPE_QUESTIONS:
        return saveAndReturn(data_type, conversation_object.get_questions())
    elif data_type == DATA_TYPE_FOLLOW_UPS:
        return saveAndReturn(data_type, conversation_object.get_follow_ups())
    elif data_type == DATA_TYPE_TOPICS:
        return saveAndReturn(data_type, conversation_object.get_topics())

def main():
    for data_type in DATA_TYPES:
        data=processAudio(mock=True, data_type=data_type)
        print(data)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()