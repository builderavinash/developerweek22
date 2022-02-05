import agorartc
import symbl
import ctypes


class MyAudioFrameObserver(agorartc.AudioFrameObserver):

    def __init__(self, connection_object):
        self.connection_object = connection_object

    def onRecordAudioFrame(self, type1, samples, bytesPerSample, channels, samplesPerSec, buffer1, renderTimeMs, avsync_type):
        pass

    def onPlaybackAudioFrame(self, type1, samples, bytesPerSample, channels, samplesPerSec, buffer1, renderTimeMs, avsync_type):
        pass

    def onMixedAudioFrame(self, type1, samples, bytesPerSample, channels, samplesPerSec, buffer1, renderTimeMs, avsync_type):

        channel = channels
        samplewidth = bytesPerSample
        framerate = samplesPerSec

        audio_array = (ctypes.c_ubyte * samples * bytesPerSample * channels).from_address(buffer1)
        audio_data=bytes(audio_array)

        self.connection_object.send_audio(audio_data)


    def onPlaybackAudioFrameBeforeMixing(self, uid, type1, samples, bytesPerSample, channels, samplesPerSec, buffer1, renderTimeMs, avsync_type):
        pass

