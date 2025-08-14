"""解析pdf"""


import pdfplumber

"""打开文件并创建PDF对象"""
with pdfplumber.open("../example.pdf") as pdf:
    """.metadata属性返回书籍基本信息的字典"""
    metadata = pdf.metadata
    # print(metadata) # {'Author': 'wyc', 'Comments': '', 'Company': '', 'CreationDate': "D:20250219184435+08'00'", 'Creator': 'WPS 文字', 'Keywords': '', 'ModDate': "D:20250219184435+08'00'", 'Producer': '', 'SourceModified': "D:20250219184435+08'00'", 'Subject': '', 'Title': '\u3000一．填空题：（加粗的文字为该题的答案）', 'Trapped': 'False'}

    """Page对象列表
    PDF文件的每一页都是一个Page对象
    """
    pages = pdf.pages

    """Page对象常用属性"""
    page = pages[0]
    # 页码(从1开始) 页面宽度和高度
    page_num = page.page_number
    width = page.width
    height = page.height
    # print(page_num, width, height) # 1 595.3 841.9

    """裁剪Page
    .crop()裁剪页面，返回Page对象
    第一个参数传入的元组是左上角和右下角的坐标
    """
    cropped_page = page.crop((85, 70, width-70, height-65))

    """将Page对象转换为PageImage对象
    裁剪Page对象之后，可以通过这种方式查看裁剪之后的效果
    这样慢慢调整可以将页面的页眉页脚裁剪掉，防止影响解析PDF
    """
    # cropped_page_img = cropped_page.to_image()
    # cropped_page_img.show()

    """解析文本"""
    text = cropped_page.extract_text()
    print(text)
