"""Create html by choosing style, color, blocks, etc.
Uses html comments <!-- example --> to find the places where to append new html

Todo:
    * 
    * 
"""

#Fix PATH tests and main program
try: #Path when running tests
    import sys
    import os
    sys.path.insert(0, os.path.abspath('..'))
    from sheetmaker import constants
except: #Path when running sheetmaker.py
    import constants


class HtmlSheet(object):
    """The html sheet to be created and customized."""


    def __init__(self, title, date, author_name=None):
        """Return a new HtmlSheet object.

        Args:
            title (str): Html title and file name.
            date (str): Today's date.
            

        Attrib:
            title (str): Html title and file name.
            date (str): Creation date displayed in footer.
            color (int): Color code style.
            main_columns (int): Number of columns for sheet structure.
            author_name (str): Name of the author
            author_picture (str): Url path to picture, displayed in footer.
            author_web (str): Url displayed in footer.
            sponsor_name (str): Name displayed in footer.
            sponsor_web (str): Url displayed in footer.

        """
        self.title = title
        self.date = date
        self.author_name = author_name
    

    def create_empty_sheet(self):
        """Create a basic html file and a files folder that will be used to make the sheet."""
        html = constants.EMPTY_SHEET.format(self.title)
        return(html, None)


    def set_style(self, color_number):
        """Select the color style, the number of rows and adjust css style that will be used for the html.

        Args:
            color_number (int): Color number for the html style (predefined colors).

        """
        self.color = color_number
        color_main = {1: "#fa6900", #main color - orange
                      2: "#000000", #black
                      3: "#b60205", #red
                      4: "#fbca04", #yellow
                      5: "#0e8a16", #green
                      6: "#1d76db", #blue
                     }
        color_secundary = {1: "#fee5d3", #secundary color, lighter than main color
                           2: "#cccccc",
                           3: "#e99695",
                           4: "#fef2c0",
                           5: "#c2e0c6",
                           6: "#bfd4f2",
                          }
        html = constants.COLOR_STYLE.format(color_main[self.color], color_secundary[self.color])        
        return(html, "<!-- css -->")

    
    def build_columns(self, columns_number):
        """Creates main_columns html

        Args:
            columns_number (int): Main columns for the html file (1,2 or 3 only allowed).

        """
        self.columns_number = columns_number
        if self.columns_number == 1:
            html = constants.COLUMNS1
        elif self.columns_number == 2:
            html = constants.COLUMNS2
        elif self.columns_number == 3:
            html = constants.COLUMNS3
        return(html, "<!-- columns -->")


    def build_header(self, author_name, sponsor_name, sponsor_web):
        """Creates html header.

        Args:   
            author_name (str): Name displayed in header and footer.

        """
        self.author_name = author_name
        html = constants.HEADER.format(self.title, author_name, sponsor_name, sponsor_web)
        return(html, "<!-- header -->")


    def build_footer(self):
        """Creates html footer.

        Args:
            author_picture (str): Url path to picture, displayed in footer.
            author_web (str): Url displayed in footer.
            sponsor_name (str): Name displayed in footer.
            sponsor_web (str): Url displayed in footer.
        """
        html = constants.FOOTER.format(self.date)
        return(html, "<!-- footer -->")  

    
    
    def build_rows_block(self, selected_column, title, rows_number, text):
        """Creates a html rows block.

        Args:
            selected_column (int): Column in which block will be created.
            title (str): Block title.
            rows_number (int): Numbers of rows to create.
            text (list): Text for each row.

        """
        rows = ""
        for i in range(rows_number):
            if i % 2 == 0:
                rows += constants.ROWS_BLOCK_EVEN.format(text[i])
            else:
                rows += constants.ROWS_BLOCK_ODD.format(text[i])
        html = constants.ROWS_BLOCK.format(title, rows)
        return(html, "<!-- column" + str(selected_column) + " -->")


    def build_text_block(self, selected_column, title, text):
        """Creates a html text block.

        Args:
            selected_column (int): Column in which block will be created.
            title (str): Block title.
            text (str): Text for block.

        """
        html = constants.TEXT_BLOCK.format(title, text)
        return(html, "<!-- column" + str(selected_column) + " -->")


    def update_html_file(self, html_to_add):
        """Reads html file, appends new html and writes it to file

        Args:
            html_to_add (tuple): Text to write in file and Text string to continue writting from there.

        """
        #Only reads file if it exists.
        new_html = html_to_add[0]
        from_here = html_to_add[1]
        if from_here:
            with open(self.title + ".html", 'r', encoding="utf8") as sheet:
                html = (sheet.read())
                html = html.replace(from_here, new_html + " " + from_here)
        else:
            html = new_html
        with open(self.title + ".html", 'w', encoding="utf8") as sheet:
            sheet.write(html)

