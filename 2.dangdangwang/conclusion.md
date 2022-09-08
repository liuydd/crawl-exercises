I.
The first version's mistake: It repeated the last book's information 20 times per page.
The reason of the problem: book_dict is a dictionary that is mutable. So the blank dictionary should be inside the loop rather than be in front of which.
II.
The second version's mistake: It repeated the first page's books' information twice
The reason of the problem: The serial number of the pages starts from 1 rather than 0. So the range should be range(1,26) rather than range(25).
III.
Don't use the change of the type to get the contents. Use '.string'