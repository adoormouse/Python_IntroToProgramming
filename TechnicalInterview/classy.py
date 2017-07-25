"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):
    def __init__(self):
        self.items = []
        self.itemValue = {'tophat': 2, "bowtie":4, "monicle":4}
        self.classValue = 0

    def addItem(self, item=""):
        item = str(item)

        if item == 'tophat' or item == 'bowtie' or item == 'monicle':
            self.items.append(item)
            self.classValue += self.itemValue.get(item)
            return 0

        self.items.append(item)
        return 0

    def getClassiness(self):
        return self.classValue


# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())
me.addItem("tophat")
# # Should be 2
print(me.getClassiness())
#
me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# # Should be 11

print("My Class Value")
print(me.getClassiness())
#
# me.addItem("bowtie")
# # Should be 15
# print
# me.getClassiness()