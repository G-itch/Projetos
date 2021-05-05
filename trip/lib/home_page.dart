import 'package:flutter/material.dart';
import 'package:trip/app_controller.dart';

class HomePage extends StatefulWidget {
  @override
  State<HomePage> createState() {
    return HomePageState();
  }
}

class HomePageState extends State<HomePage> {
  int cont = 0;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Olá Mundo!"),
          actions: [
            customswitch(),
          ],
        ),
        floatingActionButton: FloatingActionButton(
          child: Icon(Icons.add),
          onPressed: () {
            setState(() {
              cont++;
            });
          },
        ),
        body: Container(
          width: double.infinity,
          height: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("Counter: $cont"),
              customswitch(),
              Container(height: 50),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    width: 50,
                    height: 50,
                    color: Colors.blue,
                  ),
                  Container(
                    width: 50,
                    height: 50,
                    color: Colors.red,
                  ),
                  Container(
                    width: 50,
                    height: 50,
                    color: Colors.green,
                  ),
                ],
              )
            ],
          ),
        ));
  }
}

class customswitch extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Switch(
      value: Appcontroller.instance.darttheme,
      onChanged: (value) {
        Appcontroller.instance.changetheme();
      },
    );
  }
}
