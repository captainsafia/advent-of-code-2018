*dusts off shoulders*

So it's been a while since I've done this.

That's right, I'm *blogging* again. Prepare your food rations and gallons of water because a disaster is coming through!

In all seriousness, I won't joke too much about me getting back on the old blogging steed. 

Since it's officially December 1st, which constantly scares me because I was not expecting it to come this fast, the [Advent of Code](https://adventofcode.com/) has started.

I figured that I would play along this year. I haven't done it before, but I'm no stranger to solving the odd programming puzzle or two. I figured I'd start blogging along the experience of me solving these problems, in real-time. I've also been looking for a way to pick up some new programming languages. So, I decided that I'll be doing each day of the challenge using a different programming language.

It's the first day so the text for the challenge has been released. You can read the [day 1 challenge](https://adventofcode.com/2018/day/1) here. Be sure to read it before continuing with the rest of the blog post.

Alright. Ready? Let's go.

The fundamental problem here is that given a newline-delimited file with a list of numbers with "+" or "-" we want to figure out what the resulting number will be after all the numbers have been summed or subtracted, starting from 0.

I saved the data into a file called `frequencies.txt` and I'll be using it throughout the code. For this first challenge, I'll start with a language that is familiar and well-worn to me: Python. It was the first programming language (other than HTML and CSS) that I had learned as a pre-teen. It feels fitting to use it here.

I started by implementing a pretty naive solution. I read the file into a list data structure, looped through the strings, checked to see if the string started with "-" or "+" add executed the following computation. Here's what the code for this looks like.

```python
with open("frequencies.txt") as frequencies:
    result = 0
    numbers = frequencies.read().splitlines()
    for number in numbers:
        if number.startswith("-"):
            number_as_int = int(number[1:])
            result -= number_as_int
        elif number.startswith("+"):
            number_as_int = int(number[1:])
            result += number_as_int
        else:
            raise Exception("{} is not in the valid format.".format(number))
    print(result)
```

This code is correct, I validated the result I got against the Advent of Code page to confirm this. Is there a way we can make it better?

Now, this is usually the part in these blog posts where someone figures out some clever optimization for the code or uses some special language features to reduce the lines of code. As an open source developer and avid code reader, I always prefer to keep code readable. Any change I make to the code would have to maintain the readability of the code.

As it turns out, I can get away with removing the `.startswith` logic in the codebase. Python's `int` function can handle converting numeric strings with any sign. So it'll appropriately handle converting "+2" and "-3". Knowing this, the code can be trimmed down to the code below.

```python
with open("frequencies.txt") as frequencies:
    result = 0
    numbers = frequencies.read().splitlines()
    for number in numbers:
        result += int(number)
    print(result)
```

Well, isn't this neat! It's still fairly readable. You don't miss the point of the code by skimming through it really quickly. I like that.

I could leverage another Python feature here, the list comprehension, to make the code even more succinct. Here's how it would look.

```python
with open("frequencies.txt") as frequencies:
    result = sum([int(number) for number in frequencies.read().splitlines()])
    print(result)
```

Now, this is where I personally draw a line. Does this code get the job done? Yes. Is it nice and short? Yes. Is it easy to get a sense of what is going on here from a quick skim? Ehhhhhhhhhhh.

If I were to chose the iteration I would choose to implement, I'd probably choose the second. It balances white space and variable naming easily and doesn't overdo it with using language-specific features.

Someone who has never read Python before but has experience programming can under the second iteration quite easily, not so much the second. I think this is one of the most important things about good code: it should be easy to read and understand as long as someone understands the basic concepts of programming.

OK. That's enough preaching for one day. Hopefully, you enjoyed reading this. If you'd like to see the solutions and try them out yourself, you can check out [this GitHub repo](https://github.com/captainsafia/advent-of-code-2018).

See you tomorrow!