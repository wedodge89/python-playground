# DEVELOPER FUNDAMENTALS

## 1. Don't read the dictionary.
You can always Google things. You don't need to memorize every function and bit of syntax. What matters more is familiarizing yourself with the way a language works and how to think computationally. Don't learn a language as if you are trying to ace a test, but learn how to use it.

## 2. Comment your code.
Comments tell the interpreter to skip over a section of text, rather than try to run it as code. In Python, comments are denoted with #. \
Guidelines: 
* Don't add unnecessary clutter.
* Keep comments concise.
* Comments should always add clarity.
* Can this comment be fixed with more readable code?
* See [Writing Comments in Python (Guide)](https://realpython.com/python-comments-guide/) by Jaya Zhané

## 3. Understanding Data Structures
Some data structures make more sense in certain situations than others. A good programmer gets familiar with these situations so that they can use the best, most efficient data for a given situation.
* _Lists_ work well for data that needs to stay in order.
* _Dictionaries_ work well for data where order is not important, but where different values and data types work together.

## 4. What is good code?
* Clean-Follows a style endorsed by language-specific community. No extraneous details or comments. Clear what each line of code does.
* Readable-Easy to understand. Comments are concise and helpful. Variable names that make clear their purpose.
* Predictability-Code is not so compact or feature-dense that it is difficult to tell what it does.
* DRY-*D*on't *R*epeat *Y*ourself. Use functions, arguments, conditionals, etc. to keep code from being repetitive.

## 5. Test your assumptions.
* You should know and be able to predict how code will work.
* You should understand code well enough to teach others.
* Use print() or return to investiage objects.