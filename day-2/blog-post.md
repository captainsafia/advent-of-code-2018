It's Day 2 of the Advent of Code 2018 Challenge. Once again, I'm blogging through the solution here. Before getting started, you should read the [day's challenge](https://adventofcode.com/2018/day/2).

I started off by downloading the list of box IDs into a `box-ids.txt` file. The general program will require that we run through the IDs, keeping a count of the times we find two and three of the same letter in the ID, and then multiplying these counts.

Since I've decided to do the challenge in a different language each day. Today, I'll be writing out the solution in Node. The Node standard library isn't as rich as Python's standard library. There are some standard libraries in Python that would be extremely applicable to this problem, but oh well. I dumped out the initial iteration of the algorithm above here.

```javascript
const fs = require("fs");

function getOccurenceCount(string) {
  let result = {};
  for (var index in string) {
    const char = string.charAt(index);
    result[char] = (result[char] || 0) + 1;
  }
  return result;
}

fs.readFile("box-ids.txt", (error, boxIdsBuffer) => {
  if (error) console.error(error);

  let countOfTwos = 0;
  let countOfThrees = 0;
  const boxIds = boxIdsBuffer.toString().split("\n");
  for (let index in boxIds) {
    const boxId = boxIds[index];
    occurenceCount = getOccurenceCount(boxId);
    occurenceCountList = Object.values(occurenceCount);
    countOfTwos += occurenceCountList.includes(2);
    countOfThrees += occurenceCountList.includes(3);
  }
  console.log(countOfThrees * countOfTwos);
});
```

Fun fact, it actually took me about 5 minutes extra to get this initial iteration because I didn't fully read the instructions (shame on me!). I assumed you had to add the number of times a character occurred twice, not just if a character occurred twice. That sentence was phrased awkwardly, but the copy and paste from the problem statement should hopefully clarify what I mean.

```
abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
```

As it turns out, there is a second part to this particular puzzle. I'll post the link for it [here](https://adventofcode.com/2018/day/2#part2). I'm not sure if you are going to be able to see it if you haven't completed the first part. I'll work on the second part now and then optimize both solutions later, because trust me, the above could definitely use a little love in some places.

For this second part, we will need to find the IDs that differ by exactly a single letter. I'm going to bet that I'll need to compute the [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) between the password strings at some point.

Intermission: It's been about 8 hours since I wrote the last sentence. I had to go and be a human being so now I'm back rushing to finish this. Here's the naive solution I cooked up for calculating the two passwords that have only a single string difference.

```javascript
const fs = require("fs");

function getOccurenceCount(string) {
  let result = {};
  for (var index in string) {
    const char = string.charAt(index);
    result[char] = (result[char] || 0) + 1;
  }
  return result;
}

function hammingDistance(s, t) {
  let distance = 0;

  for (let index in s) {
    if (s[index] !== t[index]) {
      distance += 1;
    }
  }

  return distance;
}

fs.readFile("box-ids.txt", (error, boxIdsBuffer) => {
  if (error) console.error(error);

  let countOfTwos = 0;
  let countOfThrees = 0;

  const boxIds = boxIdsBuffer.toString().split("\n");
  for (let index in boxIds) {
    const boxId = boxIds[index];
    occurenceCount = getOccurenceCount(boxId);
    occurenceCountList = Object.values(occurenceCount);
    countOfTwos += occurenceCountList.includes(2);
    countOfThrees += occurenceCountList.includes(3);
  }

  console.log(countOfThrees * countOfTwos);

  for (let index in boxIds) {
    const boxId = boxIds[index];
    boxIds.map(otherBoxId => {
      if (hammingDistance(boxId, otherBoxId) === 1) {
        for (let index in boxId) {
          if (boxId[index] === otherBoxId[index]) {
            process.stdout.write(boxId[index]);
          }
        }
        return;
      }
    });
  }
});
```

Alright! That gets the job done. There's a couple of ways to make this better. Using streams instance of converting the buffer to a string and iterating over it, reducing the number of repetitive for-loops, cleaning up the calculation for the number of occurrences.

Here's the final clean-up I did. Eh, it does the trick. Ship it!

```javascript
const fs = require("fs");

function getOccurenceCount(string) {
  let result = {};
  for (var index in string) {
    const char = string.charAt(index);
    result[char] = (result[char] || 0) + 1;
  }
  return result;
}

function hammingDistance(s, t) {
  let distance = 0;

  for (let index in s) {
    if (s[index] !== t[index]) {
      distance += 1;
    }
  }

  return distance;
}

fs.readFile("box-ids.txt", (error, boxIdsBuffer) => {
  if (error) console.error(error);

  let countOfTwos = 0;
  let countOfThrees = 0;

  const boxIds = boxIdsBuffer.toString().split("\n");
  for (let index in boxIds) {
    const boxId = boxIds[index];
    occurenceCount = getOccurenceCount(boxId);
    occurenceCountList = Object.values(occurenceCount);
    countOfTwos += occurenceCountList.includes(2);
    countOfThrees += occurenceCountList.includes(3);

    boxIds.map(otherBoxId => {
      if (hammingDistance(boxId, otherBoxId) === 1) {
        console.log(
          Array.from(boxId)
            .filter((character, index) => {
              return character === otherBoxId[index];
            })
            .join("")
        );
      }
    });
  }
  console.log(countOfThrees * countOfTwos);
});
```
