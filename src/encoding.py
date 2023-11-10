import chardet

text = """
��������,100,1
�������,1000,3
������,10,5
�����,50,5
����������,75,5
"""

result = chardet.detect(text.encode())
detected_encoding = result['encoding']

print(f"The detected encoding is: {detected_encoding}")