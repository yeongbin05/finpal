import base64
import matplotlib.pyplot as plt
from io import BytesIO
ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()

buffer = BytesIO()
plt.savefig(buffer,format='png')
image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
buffer.close()
