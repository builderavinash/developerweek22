import agorartc
import backend.agora.capture_audio as capture_audio
import time
import symbl

app_id="f096eac98b50484b9cabac5fdfa5087b"
channel="tempChannel"
token="006f096eac98b50484b9cabac5fdfa5087bIACotJFQJ/VmkPQRO0ay9j08kY14idaTA01AigKcPBOYc2/A5uMAAAAAEAD1z9KP8CEAYgEAAQDwIQBi"
credentials={
    "app_id":"715a416176563176755571796f484c5662614a6c483377786a48796634375136",
    "app_secret":"6e39365a414732764f4b44324736734639356350454b3772317042706c4570397944335a6271504c6e6e6d397a61696b68426643375368355876624b534b5a48"
}

def main():
    connection_object = symbl.Streaming.start_connection(credentials=credentials)

    rtc = agorartc.createRtcEngineBridge()
    eventHandler = agorartc.RtcEngineEventHandlerBase()
    rtc.initEventHandler(eventHandler)
    rtc.initialize(app_id, None,
                        agorartc.AREA_CODE_GLOB & 0xFFFFFFFF)  # If you do not have an App ID, see Appendix (https://github.com/AgoraIO-Community/Agora-Python-SDK#appendix).
    rtc.enableVideo()
    rtc.joinChannel(token,channel, "", 0)

    time.sleep(10)
    rtc.leaveChannel()  # Leave channel
    print('print once: ', connection_object.conversation.get_messages())
    connection_object.stop()
    rtc.release()

    # rtc = agorartc.createRtcEngineBridge()
    # eventHandler = capture_audio.MyRtcEngineEventHandler(rtc)
    # rtc.initEventHandler(eventHandler)
    # # Please input your APP ID here.
    # rtc.initialize(app_id, None, agorartc.AREA_CODE_GLOB & 0xFFFFFFFF)
    # afo = capture_audio.MyAudioFrameObserver()
    # rtc.joinChannel(token, channel, "", 0)
    # rtc.startPreview()
    # rtc.enableVideo()
    # agorartc.registerAudioFrameObserver(rtc, afo)
    # input()  # Press any key to come to an end.
    # agorartc.unregisterAudioFrameObserver(rtc, afo)
    # rtc.leaveChannel()
    # rtc.release()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()