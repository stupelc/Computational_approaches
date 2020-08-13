import numpy as np
import xlrd
import collections

Dress = collections.namedtuple('Dress',['Style','Price','Rating','Size','Season','NeckLine','SleeveLength','waiseline'
    ,'Material','FabricType','Decoration','PatternType'])
# note : print (data[0].Price)


# return the examples and the classifications
def read_data ():
    location = ("Attribute DataSet.xlsx")
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

def separate_data (data):
    trainSize = int(data.__len__() * 0.8);
    testSize = int (data.__len__() * 0.2);
    train = data[:trainSize]
    test = data[-testSize:]
    return train, test


def main():
    data, classifications = read_data();
    train, test = separate_data(data);



if __name__ == '__main__':
    main()
