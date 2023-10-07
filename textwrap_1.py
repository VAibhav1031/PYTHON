import textwrap

# string="hey there isd fknsjdndskvnkdsv"

# width=18
# wrapped_lines=textwrap.shorten(string,width,placeholder="...")
# print(wrapped_lines)

# Basically the  use of the   shorten  is to  short the  long  string   means  if you  so long text 
# and you  have  to display   thiss goess  onnn  string="hey there isd fknsjdndskvnkdsv"   hey there isd...


# wrap

# string="hey ther is something you may n=know"
# width=6
# wrapped_lines=textwrap.wrap(string,width)
# print(wrapped_lines)

# textwrap.wrap(text, width): This function wraps a single paragraph of text and returns a list of wrapped lines. The width parameter specifies the maximum width of each line.

# fill

# textwrap.fill(text, width): This function wraps a single paragraph of text and returns a single string where lines are separated by newline characters ('\n'). The width parameter specifies the maximum width of each line.

# text = "This is a long piece of text that needs to be wrapped to fit within a specific width."
# width = 20

# wrapped_text = textwrap.fill(text, width)
# print(wrapped_text)

# output:This is a long piece
# of text that needs
# to be wrapped to fit
# within a specific
# width.

# dedent

# textwrap.dedent(text): This function removes common leading whitespace from a block of text. It's useful for removing indentation in multiline strings.

# indent

# textwrap.indent(text, prefix, predicate=None): This function indents a block of text by adding a prefix to each line. You can specify an optional predicate function to conditionally apply the prefix only to specific lines

# text = "This is a block of text that should be indented."
# prefix = "    " 
# indented_text = textwrap.indent(text, prefix)
# print(indented_text)

# output:    This is a block of text that should be indented.
