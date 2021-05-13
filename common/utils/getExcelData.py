import xlrd,re,json

def get_excelData(workBook,sheetName,caseName):
    """
    :param sheetName: sheet表名
    :param caseName:  从excle中第一列关键字（字母）
    :return: # [{}，{}，{}]
    """
    workSheet = workBook.sheet_by_name(sheetName)
    list_title = workSheet.row_values(0)
    try:
        num_url = list_title.index('url')
        num_headers = list_title.index('headers')
        num_method = list_title.index('method')
        num_reqData = list_title.index('reqData')
        num_expectData = list_title.index('expectData')
        num_testPoint = list_title.index('testPoint')
        lis = []

        idx = 0
        try:
            for one in workSheet.col_values(0):
                result = ''.join(re.findall(r'[A-Za-z]', one))  # 抽取字母字符串
                if caseName == result:
                    dict0 = {"url": "", "headers": "", "method": "", "reqData": "", "expectData": ""}
                    dict0['url'] = workSheet.cell_value(idx, num_url)
                    dict0['headers'] = workSheet.cell_value(idx, num_headers)
                    dict0['method'] = workSheet.cell_value(idx, num_method)
                    dict0['reqData'] = workSheet.cell_value(idx, num_reqData)
                    dict0['expectData'] = workSheet.cell_value(idx, num_expectData)
                    dict0['testPoint']= workSheet.cell_value(idx, num_testPoint)

                    # json字符串转换成字典
                    dict0['reqData'] = json.loads(dict0['reqData'])
                    dict0['expectData'] = json.loads(dict0['expectData'])
                    try:
                        dict0['headers'] = json.loads(dict0['headers'])
                    except:
                        # print('header无')
                        dict0['headers'] = None
                    lis.append(dict0)
                idx += 1
            return lis
        except:
            print("excle中header值或参数或期望不是json字符串")
    except:
        print("检查excle中标题是否正确")


if __name__ == '__main__':
    workBook = xlrd.open_workbook('../../test_case_data/bmy/bmy_case.xlsx')
    li = get_excelData(workBook,"登录模块","Login")
    print(li)

# {"Authorization": "","Content-Type":"application/x-www-form-urlencoded"}