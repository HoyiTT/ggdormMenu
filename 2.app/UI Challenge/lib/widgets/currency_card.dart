import 'package:flutter/material.dart';

class CurrencyCard extends StatelessWidget{

  final String name, code, amount;
  final IconData icon;
  final bool isInverted;
  final double ofs;

  final _blackColor = const Color(0xFF1F2123);

  const CurrencyCard({
    Key key,
    this.name, 
    this.code, 
    this.amount, 
    this.icon,
    this.isInverted,
    this.ofs,
    }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Transform.translate(
      offset: Offset(0, ofs * -20),
      child: Container(
                  clipBehavior: Clip.hardEdge, // overflow된 아이콘을 절단
                  decoration: BoxDecoration(
                    color: isInverted ? Colors.white :  _blackColor,
                    borderRadius: BorderRadius.circular(25),
                  ),
                  child: Padding(
                    padding: 
                      const EdgeInsets.all(30),// 세로 가로 
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Column( 
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              name,
                              style: TextStyle(
                                color: isInverted ? _blackColor : Colors.white ,
                                fontSize: 32,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                            const SizedBox(
                              height: 15,
                            ),
                            Row(
                              children: [
                                Text(
                                  amount,
                                  style: TextStyle(
                                    color : isInverted ? _blackColor :Colors.white,
                                    fontSize: 20,
                                  ),
                                ),
                                const SizedBox(
                                  width: 5,
                                  ),
                                Text(
                                  code,
                                  style: TextStyle(
                                    color: isInverted ? _blackColor.withOpacity(0.8) : Colors.white.withOpacity(0.8),
                                    fontSize: 20,
                                  ),
                                )],
                            ),
                          ],
                        ),
                          Transform.scale( // 아이콘의 크기를 변경
                            scale: 2.2, // 아이콘의 크기를 2.2배
                            child: Transform.translate(
                              offset: const Offset(-5, 12,), // 아이콘의 x,y 좌표를 변경
                              child: Icon(
                              icon,
                              color: isInverted ? _blackColor : Colors.white, 
                              size: 88,
                              ),
                            ),
                        ),
    
                      ],
                    ),
                  ),
                ),
    );
  }
}