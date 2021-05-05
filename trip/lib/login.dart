import 'package:flutter/material.dart';
import 'package:trip/home_page.dart';

class loginpage extends StatefulWidget {
  @override
  _loginpageState createState() => _loginpageState();
}

class _loginpageState extends State<loginpage> {
  String email;
  String password;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SizedBox(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextField(
                onChanged: (text) {
                  email = text;
                },
                keyboardType: TextInputType.emailAddress,
                decoration: InputDecoration(
                  labelText: "Email",
                  border: OutlineInputBorder(),
                ),
              ),
              SizedBox(height: 8),
              TextField(
                onChanged: (text) {
                  password = text;
                },
                obscureText: true,
                decoration: InputDecoration(
                  labelText: "Password",
                  border: OutlineInputBorder(),
                ),
              ),
              SizedBox(height: 15),
              RaisedButton(
                color: Colors.blue,
                textColor: Colors.white,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10)),
                onPressed: () {
                  if (email == 'teste@email.com' && password == '12') {
                    Navigator.of(context).push(
                        MaterialPageRoute(builder: (context) => HomePage()));
                  } else {
                    print("login inválido");
                  }
                },
                child: Text("Entrar"),
              )
            ],
          ),
        ),
      ),
    );
  }
}
