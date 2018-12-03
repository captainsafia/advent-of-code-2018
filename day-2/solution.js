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
