import 'package:flutter/cupertino.dart';

class Appcontroller extends ChangeNotifier {
  static Appcontroller instance = Appcontroller();
  bool darttheme = false;
  changetheme() {
    darttheme = !darttheme;
    notifyListeners();
  }
}
