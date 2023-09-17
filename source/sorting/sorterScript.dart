import 'dart:async';
import 'dart:io';

void main(){
  var contents = File('ki.txt');
  Directory current = Directory.current;
  var splitSource = contents.readAsStringSync().replaceAll("\n", "").trim().split(';');
  var numList = [];
  var strList = [];

  print("""

----> S O R T E R
Writen in Dart(Google), by Nikke! Sorter sortiring values from a given file.
[$current | is your working directory, place ki.txt here!] <----
""");

  for (var i = 0; i < splitSource.length; i++) {
    var currentElement = splitSource[i];

    if(double.tryParse(currentElement) == null){

      print('$currentElement is a String.');
      strList.add(currentElement);

    } else {

      print('$currentElement is a Number.');
      numList.add(currentElement);

      }
  }
}