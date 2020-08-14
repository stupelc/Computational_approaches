import numpy as np
import xlrd
from xlwt import Workbook
import collections

Dress = collections.namedtuple('Dress',['Style','Price','Rating','Size','Season','NeckLine','SleeveLength','waiseline'
    ,'Material','FabricType','Decoration','PatternType'])

att_dict = {
    0 : 'Style',
    1: 'Price',
    2 : 'Rating',
    3 : 'Size',
    4 : 'Season',
    5: 'NeckLine',
    6: 'SleeveLength',
    7 : 'waiseline',
    8 : 'Material',
    9 : 'FabricType',
    10 : 'Decoration',
    11 :'PatternType'
}

# note : print (data[0].Price)


# return the examples and the classifications
def read_data ():
    location = ("Attribute DataSet new.xls")
    wb = xlrd.open_workbook(location)
    sheet = wb.sheet_by_index(0)
    data = []
    classification = []

    # Reading on all the examples
    for i in range(1, sheet.nrows):  # scape on the attribute name
        data.append(
            Dress(sheet.cell_value(i, 1),  # Style
                  sheet.cell_value(i, 2),  # Price
                  sheet.cell_value(i, 3),  # Rating
                  sheet.cell_value(i, 4),  # Size
                  sheet.cell_value(i, 5),  # Season
                  sheet.cell_value(i, 6),  # NeckLine
                  sheet.cell_value(i, 7),  # SleeveLength
                  sheet.cell_value(i, 8),  # waiseline
                  sheet.cell_value(i, 9),  # Material
                  sheet.cell_value(i, 10),  # FabricType
                  sheet.cell_value(i, 11),  # Decoration
                  sheet.cell_value(i, 12)))  # PatternType
        classification.append(int(sheet.cell_value(i, 13)))  # Classification (0/1)

    return data, classification

# Returns the most common value of each attribute
def most_common_values ():
    location = ("Attribute DataSet.xlsx")
    wb = xlrd.open_workbook(location)
    sheet = wb.sheet_by_index(0)
    att_most_common_dict = {}  # includes all the attributes and the most common value on each of them
    single_att_examples = []  # include single attribute with all his values and their num of performances

    # Reading on all the examples
    for i in range(1, sheet.ncols):  # move on each attribute
        for j in range(1, sheet.nrows):
            single_att_examples.append(sheet.cell_value(j, i))
        c = collections.Counter(single_att_examples)  # count how much each element appears
        most_coomon = c.most_common()[0][0]  # find the mosot common item
        if (most_coomon == 'null'):
            most_coomon = c.most_common()[1][0]
        att_most_common_dict[i] = most_coomon  # update the dictionary
        single_att_examples = []  # clear the array of examples

    return att_most_common_dict

def filling_missing_parts ():
    most_common = most_common_values()

    # for writing
    wb_new = Workbook()
    # add_sheet is used to create sheet.
    sheet1 = wb_new.add_sheet('Sheet 1')

    # for reading
    location = ("Attribute DataSet.xlsx")
    wb = xlrd.open_workbook(location)
    sheet = wb.sheet_by_index(0)
    # create new exel file without missing data
    for i in range(1, sheet.ncols):  # move on each attribute
        for j in range(1, sheet.nrows):
            if (sheet.cell_value(j, i) == 'null'):
                sheet1.write(j, i, most_common[i])
            else:
                sheet1.write(j, i, sheet.cell_value(j, i))

    wb_new.save("Attribute DataSet new.xls")


def separate_data (data):
    trainSize = int(data.__len__() * 0.8)
    testSize = int (data.__len__() * 0.2)
    train = data[:trainSize]
    test = data[-testSize:]
    return train, test


def main():
    # Dealing with missing data
    filling_missing_parts()

    # Reading and separating the data to train and test
    data, classifications = read_data()
    train, test = separate_data(data)



if __name__ == '__main__':
    main()
