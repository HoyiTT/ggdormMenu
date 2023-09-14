import 'package:flutter/material.dart';

class Button extends StatelessWidget{

  final String text;
  final Color bgColor;
  final Color textColor;

  const Button({Key key, this.text, this.bgColor, this.textColor}) : super(key: key);



  @override
  Widget build(BuildContext context) {
    return Container(
                    decoration: BoxDecoration(
                      color: bgColor,
                      borderRadius: BorderRadius.circular(45),
                    ),
                    child:  Padding(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 45,
                        vertical: 20,
                      ),
                      child: Text(
                        text,
                        style: TextStyle(
                          color: textColor,
                          fontSize: 22,
                        ),
                      ),
                    ),
                  );
  }
}