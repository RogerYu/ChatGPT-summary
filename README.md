# ChatGPT-summary
程序说明
这是一个用于纪要/文章速读整理的 Streamlit 程序，用于上传 PDF、Word 文档或文本文件，并对其中的内容进行自动化文本摘要。程序包括三个部分，文本读取、文本摘要和 Streamlit 应用。本程序采用 OpenAI 的 API 进行文本摘要。

程序依赖
streamlit
requests
PyPDF2
docx2txt
python-dotenv
openai
使用方法
在本地环境中安装上述依赖库。

下载程序代码并将其保存在本地文件夹中。

在程序根目录下创建一个名为 ".env" 的文件，将您在 OpenAI 中获得的 API 密钥复制到该文件中：

makefile
Copy code
OPENAI_API_KEY=<your_api_key>
打开终端并进入程序所在的目录。

在终端中输入以下命令以运行程序：

arduino
Copy code
streamlit run app.py
在 Streamlit 应用中，单击 "Upload a PDF or Word document" 按钮上传 PDF、Word 文档或文本文件。

如果上传的是 PDF 或 Word 文档，程序将自动提取文件中的文本内容。

在 "Enter your text here" 文本框中输入要摘要的内容。

单击 "Summarize" 按钮以获得文本的摘要。

程序将自动将文本分段，并对每个段落进行摘要处理，最终将所有段落的摘要合并为一个整体。

摘要结果将会显示在应用界面的文本框中。

注意事项
本程序仅供测试体验，严禁商用。
本程序采用 OpenAI 的 API 进行文本摘要，需要 OpenAI 的 API 密钥方能正常工作。
本程序需要访问互联网才能正常工作。
上传的文件大小应不超过 200 MB。
上传的文件类型必须是 PDF、Word 文档或文本文件，其他类型的文件不被支持。
摘要结果可能存在一定程度的错误和失真，不可完全代替人工摘要。
本程序不提供任何形式的保证，用户需自行承担使用风险。
