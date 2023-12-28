import language_tool_python
tool = language_tool_python.LanguageTool('en-US')

def language_tool_detect(sentence):
    corrected_sentence = tool.correct(sentence)
    return corrected_sentence