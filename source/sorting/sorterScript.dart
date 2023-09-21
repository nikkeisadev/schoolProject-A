import 'dart:async';
import 'dart:io';

void main(){
  var contents = File('ki.txt');
  Directory current = Directory.current;
  var splitSource = contents.readAsStringSync().replaceAll("\n", "").trim().split(';');
  var mainList = [];
  bool itsString = false;
  bool itsInt = false;

  print("""

----> S O R T E R
Writen in Dart(Google), by Nikke! Sorter sortiring values from a given file.
[$current | is your working directory, place ki.txt here!] <----
""");

  for (var i = 0; i < splitSource.length; i++) {
    var currentElement = splitSource[di];

    if(double.tryParse(currentElement) == null){

      if(itsInt){
        print('$currentElement<---- The file contains wrong character(s) [!]\nCharacter type: int, at line [$i]');
        break;
      }
      print('$currentElement is a String. [$i]');
      mainList.add(currentElement);
      itsString = true;

    } else {
      if(itsString){
        print('$currentElement<---- The file contains wrong character(s) [!]\nCharacter type: string, at line [$i]');
        break;
      }
      print('$currentElement is a Number. [$i]');
      mainList.add(currentElement);
      itsInt = true;

      }
  }
  print('Elements successfuly added! [🗸]');
  
  print("Select a sorting method [1/2]\nDescending order, or Ascending order?");
  String? orderMethod = stdin.readLineSync();  
  
  if(orderMethod == 1){
      print('You selected the descending order  [🗸]')
      var descendingOrder = mainList
      descendingOrder.sort((a, b) => a.compareTo(b));
      print('The results: $descendingOrder')
  }
  
  else if (orderMethod > 1){
      print('You selected the ascending order  [🗸]')
      var ascendingOrder = mainList
      ascendingOrder.sort((a, b) => a.compareTo(b));
      print('The results: $ascendingOrder')
    }
} 
