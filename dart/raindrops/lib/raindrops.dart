class Raindrops {
  String convert(int num) {
    var phrase = "";

    if (num % 3 == 0) phrase += "Pling";
    if (num % 5 == 0) phrase += "Plang";
    if (num % 7 == 0) phrase += "Plong";

    return phrase.isEmpty ? num.toString() : phrase;
  }
}
