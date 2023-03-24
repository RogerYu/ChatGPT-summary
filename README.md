# 中金计算机 - 纪要/文章速读整理器

这是一个基于 Streamlit 的应用程序，它可以将上传的 PDF、Word 文档或文本文件进行自动摘要，以便更快地阅读和理解。

## 功能说明
该应用程序提供以下功能：

文件上传：支持上传 PDF、Word 文档或文本文件。
文本摘要：使用 OpenAI 的 GPT-3.5 模型，将文本内容进行自动摘要。
摘要输出：将自动摘要的结果以无序列表的形式输出。

## 使用方法
访问网站 https://share.streamlit.io/sixty-north/streamlit-book。
点击页面上方的“Open in Streamlit”按钮，打开应用程序界面。
点击“Upload a PDF or Word document”按钮，选择要上传的文件。
点击“Summarize”按钮，等待摘要结果的生成。
查看摘要结果，并进行必要的修改。


## 环境要求
该应用程序需要安装以下依赖项：

Streamlit
requests
PyPDF2
docx2txt
python-dotenv
可以通过 pip 命令安装以上依赖项：
bash
Copy code
pip install streamlit requests PyPDF2 docx2txt python-dotenv

## 注意事项
该应用程序仅供测试体验，禁止商用。
该应用程序使用的 GPT-3.5 模型需要支付费用，使用时请遵守相关条款。
摘要结果仅供参考，不代表原文准确性。
如果上传的文件类型不受支持，将会提示“Unsupported file type”错误信息。
