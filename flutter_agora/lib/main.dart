import 'dart:async';

import 'package:agora_rtc_engine/rtc_engine.dart';
import 'package:agora_rtc_engine/rtc_local_view.dart' as RtcLocalView;
import 'package:agora_rtc_engine/rtc_remote_view.dart' as RtcRemoteView;
import 'package:flutter/material.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:device_info_plus/device_info_plus.dart';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:universal_html/html.dart' as html;

const channel = "tempChannel";
const appId = "f096eac98b50484b9cabac5fdfa5087b";
const token1 = "006f096eac98b50484b9cabac5fdfa5087bIAB5nHEwBy+ULE3bF5bO1IJMovVKfbbSLvk+fRjOh1TQOG/A5uMAAAAAEAD1z9KPDsX/YQEAAQAOxf9h";
const token2 = "006f096eac98b50484b9cabac5fdfa5087bIACOpNrD592V4/JIn83yuLIfl7s8w107/jvYlBbAegwIuW/A5uMAAAAAEAD1z9KP58n/YQEAAQDnyf9h";
String token = token1;


void setToken() async {

  var deviceInfoPlugin = DeviceInfoPlugin();
  var deviceInfo = await deviceInfoPlugin.deviceInfo;
  final map = deviceInfo.toMap();
  print('device info $map');
  if (map["bootloader"] == "unknown") {
    print('this is device 1');
    token=token1;
  } else {
    print('this is device 2');
    token=token2;
  }

}

void main() => runApp(
    MaterialApp(home: MyApp())
);

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int? _remoteUid;
  bool _localUserJoined = false;
  late RtcEngine _engine;

  @override
  void initState() {
    super.initState();
    setToken();
    initAgora();
  }

  Future<void> initAgora() async {
    // retrieve permissions
    if (kIsWeb) {
      await html.window.navigator.permissions?.query({"name": "camera"});
      await html.window.navigator.permissions?.query({"name": "microphone"});
    } else {
      await [Permission.microphone, Permission.camera].request();
    }

    //create the engine
    _engine = await RtcEngine.create(appId);
    await _engine.enableVideo();
    _engine.setEventHandler(
      RtcEngineEventHandler(
        joinChannelSuccess: (String channel, int uid, int elapsed) {
          print("local user $uid joined");
          setState(() {
            _localUserJoined = true;
          });
        },
        userJoined: (int uid, int elapsed) {
          print("remote user $uid joined");
          setState(() {
            _remoteUid = uid;
          });
        },
        userOffline: (int uid, UserOfflineReason reason) {
          print("remote user $uid left channel");
          setState(() {
            _remoteUid = null;
          });
        },
      ),
    );

    await _engine.joinChannel(token, channel, null, 0);
  }

  // Create UI with local view and remote view
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Agora Video Call'),
      ),
      body: Stack(
        children: [
          Center(
            child: _remoteVideo(),
          ),
          Align(
            alignment: Alignment.topLeft,
            child: Container(
              width: 100,
              height: 150,
              child: Center(
                child: _localUserJoined
                    ? RtcLocalView.SurfaceView()
                    : CircularProgressIndicator(),
              ),
            ),
          ),
        ],
      ),
    );
  }

  // Display remote user's video
  Widget _remoteVideo() {
    if (_remoteUid != null) {
      return RtcRemoteView.SurfaceView(uid: _remoteUid!);
    } else {
      return Text(
        'Please wait for remote user to join',
        textAlign: TextAlign.center,
      );
    }
  }
}