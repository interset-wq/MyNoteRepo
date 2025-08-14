from ebooklib import epub
from uuid import uuid4


book = epub.EpubBook()

"""必须元数据"""
book.set_identifier(str(uuid4()))
book.set_title('样书')
book.set_language('zh-CN')

"""其他元数据"""
book.add_author('Aleksandar Erkalovic')
# 添加封面图
with open('./image.jpg', 'rb') as f:
    book.set_cover("image.jpg", f.read())

"""添加章节"""
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

# create table of contents
# - add manual link
# - add section
# - add auto created links to chapters

book.toc = (
    epub.Link('intro.xhtml', 'Introduction', 'intro'),
    (epub.Section('所有章节'), (c1, c2))
)

# add navigation files
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# define css style
style = '''
@namespace epub "http://www.idpf.org/2007/ops";

body {
font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
}

h2 {
    text-align: left;
    text-transform: uppercase;
    font-weight: 200;     
}

ol {
    list-style-type: none;
}

ol > li:first-child {
    margin-top: 0.3em;
}


nav[epub|type~='toc'] > ol > li > ol  {
list-style-type:square;
}


nav[epub|type~='toc'] > ol > li > ol > li {
    margin-top: 0.3em;
}

'''

# add css file
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
book.add_item(nav_css)

# create spin, add cover page as first page
book.spine = ['cover', 'nav', c1, c2]

# create epub file
epub.write_epub('test.epub', book)
