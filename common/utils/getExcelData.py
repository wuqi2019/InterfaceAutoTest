import xlrd,re,json

"""调试中不可用"""
workBook = xlrd.open_workbook('../data/营运车接口测试用例V1.0.xls')

# 可以自动识别用例数
def get_excelData(sheetName,caseName):
    """
    :param sheetName: sheet表名
    :param caseName:  从excle中第一列关键字（字母）
    :return: # [({参数},{期望}),({},{}),({},{})]
    """

    workSheet = workBook.sheet_by_name(sheetName)

    lis = []
    idx = 0
    try:
        for one in workSheet.col_values(0):
            result = ''.join(re.findall(r'[A-Za-z]', one))  # 抽取字母字符串
            if caseName == result:
                url= workSheet.cell_value(idx, 5)
                headers= workSheet.cell_value(idx, 8)
                colData = workSheet.cell_value(idx, 9)
                colexpect = workSheet.cell_value(idx, 11)
                lis.append((json.loads(colData), json.loads(colexpect)))  # 如果读取excle想获取字典，表中就必须是json字符串
            idx += 1
        return lis
    except:
        print("excle中参数和期望不是 json字符串")