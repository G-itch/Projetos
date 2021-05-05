import 'package:flutter/material.dart';
import 'package:trip/app_controller.dart';
import 'package:trip/login.dart';

import 'home_page.dart';

class AppWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: Appcontroller.instance,
      builder: (context, child) {
        return MaterialApp(
          theme: ThemeData(
              primarySwatch: Colors.blue,
              brightness: Appcontroller.instance.darttheme
                  ? Brightness.dark
                  : Brightness.light),
          home: loginpage(),
        );
      },
    );
  }
}
