# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:56:41 2023

@author: Jubair Ali
"""

from io import StringIO
import fitz
import random
import tkinter as tk



FILENAME = 'FSAE_Rules.pdf'

# #Open pdf file
# pdf = fitz.open(FILENAME)

# """
# ===================================================================
#  Get table of contents from pdf and make a new table of contents
#  list with contents that link to specific rules.
#  The format for each entry in ToC is [Heading level, text, page#]
# ===================================================================
# """
# TOC = pdf.get_toc()

# TOClist = []
# for x in TOC:
#     if x[0] >= 3:
#         TOClist.append(x)

# lenToc = len(TOClist)

# """
# ==================================================================
#  Using the table of contents, we will get the location of the left
#  and right page margins. These coordinates will be used to get the
#  width of the text blocks we extract.
# ==================================================================
# """
# xmin = 70
# xmax = 550
# ymin = 70
# ymax = 725
# page = pdf.load_page(1)
# blocks = page.get_textpage().extractBLOCKS()

# print(page.cropbox)

# for x in blocks:
#     if "TABLE" in x[4]:
#         ymin = x[1]-5
#         break

# xmin = blocks[-1][0]-15
# xmax = blocks[-1][2]+10
# ymax = blocks[-1][3]+12

# contDict = {}
# indexList = list(range(0,lenToc))



# randI = random.choice(indexList)
# getCont = TOClist[randI]
# pagenum = getCont[2]

# test = pdf.load_page(pagenum-1)

# # test.set_cropbox(fitz.Rect(100,100,600,700))
# spaceindex = getCont[1].find(' ')
# print(spaceindex)
# newStr = getCont[1][:spaceindex]
# print(newStr)
# loc = [] #test.search_for(newStr + ".")


# multPage = 0

# if randI != lenToc - 1:

#     pagenum2 = TOClist[randI+1][2]

#     multPage = pagenum2 - pagenum

# else:
#     multPage = -1

# print("Multpage " + str(multPage))

# counter = 0

# while True:

#     temp_page = pdf.load_page(pagenum + counter - 1)
#     temp_loc = temp_page.search_for(newStr + ".")

#     for x in temp_loc:

#         loc.append((x,pagenum + counter))

#     counter += 1

#     if counter > multPage:
#         break

# print(loc)

# y0 = ymin
# y1 = ymax

# if len(loc) != 0 :

#     if randI not in contDict:

#         contDict.update({randI:(list(range(0,len(loc))),len(loc)-1)})

#     randb = random.choice(contDict.get(randI)[0])
#     randb = contDict.get(randI)[0].pop(randb)

#     y0 = loc[randb][0].y0-5
#     page_t1 = pdf.load_page(loc[randb][1]-1)


#     if randb < contDict.get(randI)[1]:

#         y1 = loc[randb+1][0].y0

#         if loc[randb][1] != loc[randb+1][1]:


#             page_t2 = pdf.load_page(loc[randb+1][1]-1)

#             page_t1.set_cropbox(fitz.Rect(xmin,y0,xmax,ymax))
#             page_t2.set_cropbox(fitz.Rect(xmin,ymin,xmax,y1))

#             page_t1.get_pixmap().save("ctest2.png")
#             page_t2.get_pixmap().save("ctest3.png")

#             t1_img = page_t1.get_pixmap()
#             t2_img = page_t2.get_pixmap()

#             t1_img.set_origin(0,0)
#             t2_img.set_origin(0,0)
#             t1_height = t1_img.height
#             t2_width = t2_img.width
#             t2_height = t2_img.height

#             #t1_img.set_origin(0,-t1_height)
#             #t1_img.height = t1_height + t2_height
#             #t1_img.copy(t2_img,(0,0,t2_width,t2_height))

#             # print(t1_img)
#             # print (" ")
#             # print(t2_img)

#             #t1_img = t1_img + t2_img

#             #print(t1_img)
#             pix = fitz.Pixmap(t1_img.colorspace,fitz.Rect(0,0,t2_width,t2_height+t1_height),False)
#             pix.set_origin(0, 0)
#             pix.copy(t1_img,t1_img.irect)
#             pix.set_origin(0, -t1_height)
#             pix.copy(t2_img,t2_img.irect)

#             print("con")
#             pix.save("ctest.png")

#             print(page_t1.get_text("words"))


#         else:

#             print("con2")
#             page_t1.set_cropbox(fitz.Rect(xmin,y0,xmax,y1))

#             #page_t1.add_redact_annot(loc[randb][0])
#             #page_t1.apply_redactions()
#             buffer = "h___"
#             page_t1.add_freetext_annot(loc[randb][0],buffer,fill_color=(1,1,1))

#             page_t1.get_pixmap().save("ctest.png")

#             textPage = page_t1.get_textpage()
#             #print(textPage.extractWORDS())


#     else:

#         blocks = page_t1.get_textpage().extractBLOCKS()
#         y1 = blocks[-1][3]+12

#         print("con3")
#         page_t1.set_cropbox(fitz.Rect(xmin,y0,xmax,y1))
#         page_t1.get_pixmap().save("ctest.png")

#         print(page_t1.get_text("words"))



#     print(contDict)

# else:
#     loc = test.search_for(newStr)

# #test.set_cropbox(fitz.Rect(xmin,loc[0].y0,xmax,loc[0].y1))
# #test.get_pixmap().save("test1.png")


"""
==================================================================
 This class creates a pdf object using fitz given the pdf of
 FSAE rules. It then allows you to generate a random question
 from the FSAE rules pdf. The quetions are outputted as images.
==================================================================
"""
class FSAE_QGen:

    #Instantiation of FSAEQuiz class
    def __init__(self,filename):

        self.filename = filename
        self.pdf = fitz.open(filename)

        self.TOC = self.pdf.get_toc()

        #creation of table of contents which point to rules
        self.TOClist = []

        for x in self.TOC:
            if x[0] >= 3:
                self.TOClist.append(x)

        self.TOClen = len(self.TOClist)

        #creation of minimum and maximum x and y values indicating
        #the margins of the page

        self._xmin = 70
        self._xmax = 550
        self._ymin = 70
        self._ymax = 725

        page = self.pdf.load_page(1)
        blocks = page.get_textpage().extractBLOCKS()

        for x in blocks:
            if "TABLE" in x[4]:
                self._ymin = x[1]-7
                break

        self._xmin = blocks[-1][0]-15
        self._xmax = blocks[-1][2]+10
        self._ymax = blocks[-1][3]+12

        #creation of indexes which keeps track of the questions seen
        self.indexlist = list(range(0,self.TOClen))

        #this is a dictionary that will keep track of subsections
        #to a rule if there is one. It will populate if it comes
        #as the program generates questions
        #format: {rule_int: [[0..list_index],count,nRules,[list_of_rules]]}
        #rule_int: index number of the rule from table of contents
        #[0..list]: list of indexes of sub rules
        #count: number of subrules not used in questions
        #nRules: total number of sub rules
        #[list_of_rules]: list of the coordinates of the sub rules
        self._sub_rule = {}

        #Zoom is the magnification of image
        self.zoom = 2

    #function that gets a random question and returns an image of
    #that question and answers in a tuple. Also removes that rule
    #from the list of rules.
    def get_question(self):

        rand_rule = random.choice(self.indexlist)
        content = self.TOClist[rand_rule]
        pagenum = content[2]

        #check if the rule spans multiple pages

        multipage = 0

        if rand_rule < self.TOClen-1:

            pagenum2 = self.TOClist[rand_rule+1][2]
            multipage = pagenum2 - pagenum

        #get the code for the rule from Section Header

        space_index = content[1].find(' ')
        rule_code = content[1][:space_index]
        print(rule_code)

        # check if rule has has been used,
        # if not find the location of subrules if any and add to dictionary

        if rand_rule not in self._sub_rule:

            subrule = []
            counter = 0

            while True:
                print(pagenum)
                temp_page = self.pdf.load_page(pagenum + counter - 1)
                temp_loc = temp_page.search_for(rule_code)

                for x in temp_loc:

                    subrule.append((x,pagenum + counter))

                counter += 1

                if counter > multipage:
                    break

            num_rules = len(subrule)

            self._sub_rule[rand_rule]=[list(range(1,num_rules)),num_rules,num_rules,subrule]


        #if subrules exist then select one at random. If not, set the rule to
        #the first rule
        chosen_rule = []
        rand_sub = 0

        if self._sub_rule[rand_rule][1] > 1 :

            rand_sub = random.choice(self._sub_rule[rand_rule][0])
            self._sub_rule[rand_rule][0].remove(rand_sub)
            self._sub_rule[rand_rule][1] -= 1

            chosen_rule = self._sub_rule[rand_rule][3][rand_sub]

        else:
            print("in sub")
            print(self._sub_rule[rand_rule])
            chosen_rule = self._sub_rule[rand_rule][3][0]

        print("num chosen = ",rand_sub)
        print(chosen_rule)

        #remove rule from list by removing the index number if entire
        #rule has been used
        if self._sub_rule[rand_rule][1] <= 1 :
            self.indexlist.remove(rand_rule)

        #to find end coordinates, determine if next rule is a sub rule,
        #if not, the next rule will point to next header
        next_rule = []

        if rand_sub < (self._sub_rule[rand_rule][2] - 1):

            next_rule = self._sub_rule[rand_rule][3][rand_sub+1]

        else:

            if rand_rule < (self.TOClen - 1):

                next_content = self.TOClist[rand_rule + 1]
                space_index2 = next_content[1].find(' ')
                next_code = next_content[1][:space_index2]

                temp_page = self.pdf.load_page(next_content[2] - 1)
                temp_loc = temp_page.search_for(next_code)
                print("next code = ",next_code)
                print("next rule = ", next_rule)

                next_rule = (temp_loc[0],next_content[2])
                #print(self.TOC)


            else:

                next_rule = None

        #set the cropbox of the pdf page that contains the rule
        x0 = self._xmin
        x1 = self._xmax
        y0 = chosen_rule[0].y0 - 5
        y1 = self._ymax

        page1 = self.pdf.load_page(chosen_rule[1]-1)

        is_multipage = 0

        if next_rule != None:

            is_multipage = next_rule[1] - chosen_rule[1]

        #getting the lower y coordinate of cropbox
        if next_rule != None and is_multipage == 0:
            y1 = next_rule[0].y0 - 5

        else:

            words = page1.get_textpage().extractWORDS()
            y1 = words[-1][3] + 7

        print("cropbox = ",fitz.Rect(x0,y0,x1,y1))
        page1.set_cropbox(fitz.Rect(x0,y0,x1,y1))


        #If the rule spans multiple pages, the need to make cropbox of
        #2nd page

        y0_2 = self._ymin
        y1_2 = self._ymax

        page2 = None

        if is_multipage != 0:

            y1_2 = next_rule[0].y0 - 5
            page2 = self.pdf.load_page(next_rule[1] - 1)
            page2.set_cropbox(fitz.Rect(x0,y0_2,x1,y1_2))

        #make a list of words which we can then choose a word for the question
        word_list = page1.get_text("words")
        word_list2 = []
        choose_list = 1

        #removal of words that are less than 6 characters
        word_list.pop(0)
        wordlen = 6
        word_list = self.__rem_words_in_list(word_list,wordlen)

        if page2 != None:

            word_list2 = page2.get_text("words")

            if len(word_list2) > 0:

                word_list2 = self.__rem_words_in_list(word_list2,wordlen)
                choose_list = random.choice([1,2])

        #select word for the question then remove it from page
        select_word = None
        answer = "None"

        if choose_list == 1:
            select_word = random.choice(word_list)
        else:
            select_word = random.choice(word_list2)

        answer = select_word[4]
        word_rect = fitz.Rect(select_word[0],select_word[1],select_word[2],select_word[3])
        replace_text = answer[0] + "_" * (len(answer) - 1)

        if choose_list == 1:
            page1.add_freetext_annot(word_rect,replace_text,fill_color = (1,1,1))
        else:
            page2.add_freetext_annot(word_rect,replace_text,fill_color = (1,1,1))

        #return the image
        mat = fitz.Matrix(self.zoom,self.zoom)

        if page2 == None:

            return (page1.get_pixmap(matrix = mat).tobytes("ppm"),answer)

        else:

            p1_img = page1.get_pixmap(matrix = mat)
            p2_img = page2.get_pixmap(matrix = mat)

            p1_img.set_origin(0,0)
            p2_img.set_origin(0,0)
            p1_height = p1_img.height
            p2_width = p2_img.width
            p2_height = p2_img.height
            height = p1_height + p2_height

            new_pix = fitz.Pixmap(p1_img.colorspace,fitz.Rect(0,0,p2_width,height),False)
            new_pix.set_origin(0, 0)
            new_pix.copy(p1_img,p1_img.irect)
            new_pix.set_origin(0, -p1_height)
            new_pix.copy(p2_img,p2_img.irect)


            return (new_pix.tobytes("ppm"),answer)




    #Method for removing words in a list of word blocks taken from pdf.get_text
    @staticmethod
    def __rem_words_in_list(word_list,word_len):

        i = 0

        while True:

            if len(word_list[i][4]) < word_len:
                word_list.pop(i)
                i -= 1

            i += 1

            if i >= len(word_list):
                break

        return word_list





# newQuiz = FSAE_QGen(FILENAME)
# print(newQuiz.pdf)
# newQuiz.get_question()




