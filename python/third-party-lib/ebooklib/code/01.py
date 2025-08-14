from ebooklib import epub
# 生成uuid用来当作epub的识别码 uuid4生成的uuid几乎是唯一的
from uuid import uuid4


book = epub.EpubBook()

"""元数据 epub必须具备的书籍信息"""
# epub唯一识别码
book.set_identifier(str(uuid4()))
# 书名
book.set_title('样书')
# 语言
book.set_language('zh-CN')

"""其他元数据 可有可无"""
# 书籍作者
book.add_author('ebooklib')
# DC元数据 前两个参数写法固定 第三个参数写书籍简介信息
book.add_metadata('DC', 'description', 'This is description for my book')
# 自定义元数据 前3个参数写法固定 第四个参数字典中的 'key'和'value'可以随意修改
book.add_metadata(None, 'meta', '', {'name': 'key', 'content': 'value'})

"""EpubHtml设置章节内容
title和file_name这两个参数必须传入 用于后续生成书籍目录
title表示章节标题
content表示章节内容 使用html标签表示的字符串传入
"""
# Introduction章节
c1 = epub.EpubHtml(
    title='Introduction', 
    file_name='intro.xhtml', lang='zh-CN',
    content='<h2>简介</h2>\
        <p>简介章节就是简单的介绍一下主要内容。</p>\
        <p>如果你不擅长写简介，那就把随便写几句吧。</p>'
)

# about章节
c2 = epub.EpubHtml(
    title='About this book', file_name='about.xhtml',
    content='<h2>关于</h2>\
    <p>正如你说看到的，这并不是一本书。</p>'
)

"""把章节添加到epub中"""
book.add_item(c1)
book.add_item(c2)

"""添加CSS自定义排版样式"""

# 定义样式表
style = """
@namespace epub "http://www.idpf.org/2007/ops";

h2 {
    text-align: left;
    text-transform: uppercase;
    font-weight: 200;
    color: red;
}

ol {
    list-style-type: none;
}

ol > li:first-child {
    margin-top: 0.3em;
}


nav[epub|type~='toc'] > ol > li > ol  {
    list-style-type:square;
    color: blue;
}


nav[epub|type~='toc'] > ol > li > ol > li {
    margin-top: 0.3em;
    color: green;
}
"""

nav_css = epub.EpubItem(
    uid="style_nav", file_name="style/nav.css", 
    media_type="text/css", content=style
)
book.add_item(nav_css)


"""创建书籍目录"""
# href传入创建EpubHtml对象时传入的file_name
book.toc = (
    # 通过Link创建目录
    epub.Link(href='intro.xhtml', title='Introduction', uid='intro'),
    # 通过Section和章节列表(元组)创建目录
    (epub.Section('所有章节'), (c1, c2))
)

"""添加导航文件 这是固定写法"""
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

"""添加书脊"""
book.spine = ['nav', c1, c2]

"""输出epub"""
# name 文件地址
# book 传入EpubBook对象
epub.write_epub(name='样书.epub', book=book)
