const longest_substring_with_k_distinct = function(str, k) {

    var windowStart=0, map = new Map(), maxSub= -Infinity
  
    for(windowEnd=0;windowEnd<str.length;windowEnd++)
    {
      var letter = str.charAt(windowEnd)
      if(!map.get(letter))
        map.set(letter, 1)
      else {
        update = map.get(letter) +1
        map.set(letter, update)
      }
  
      while(map.size > k)
      {
        maxSub = Math.max(maxSub, windowEnd - windowStart)
  

        var startLetter = str.charAt(windowStart)
        update = map.get(startLetter) -1
        map.set(startLetter, update)
  
        // console.log(update)
        // return "ok";

        if(map.get(startLetter) == 0)
          map.delete(startLetter)
        
        
        windowStart += 1
  

      }
    }
    return maxSub;
  };
  

  console.log(longest_substring_with_k_distinct("araaci", 2))