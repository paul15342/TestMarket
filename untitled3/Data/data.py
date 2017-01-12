from selenium import webdriver
import xlrd

def ExcelData(rowx,colx):
    path=r'D:\DeskTop\testData.xlsx'
    book=xlrd.open_workbook(path)
    sh=book.sheet_by_index(0)
    cell_values=sh.cell_value(rowx,colx)
    return cell_values