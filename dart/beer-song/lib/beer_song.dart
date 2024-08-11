class BeerSong {
    List<String> _verse(int n) {
        switch (n) {
            case 2:
                return ["2 bottles of beer on the wall, 2 bottles of beer.", "Take one down and pass it around, 1 bottle of beer on the wall."];
            case 1:
                return ["1 bottle of beer on the wall, 1 bottle of beer.", "Take it down and pass it around, no more bottles of beer on the wall."];
            case 0:
                return ["No more bottles of beer on the wall, no more bottles of beer.", "Go to the store and buy some more, 99 bottles of beer on the wall."];
            default:
                return ["$n bottles of beer on the wall, $n bottles of beer.", "Take one down and pass it around, ${n-1} bottles of beer on the wall."];
        }
    }

    List<String> recite(int start, int n) {
        List<String> verses = [];
        int end = start - n + 1;

        for (int i = start; i > end; i--) {
            verses.addAll(_verse(i));
            verses.add("");
        }

        verses.addAll(_verse(end));

        return verses;
    }
}
