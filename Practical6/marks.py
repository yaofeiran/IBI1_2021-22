marks=[45,36,86,57,53,92,65,45]
marks.sort()
print(marks)

average=(45+36+86+57+53+92+65+45)/8#calculate the avarage mark Rob has received
if average<60:
 print("Rob has failed ICA.")
else:
 print("Rob has passed ICA.")

#boxplot of the marks
import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(marks, vert=True,whis=1.5,patch_artist=True,notch=False)
plt.title("Distribution of marks")
plt.xlabel("Practicals")
plt.ylabel("marks")
plt.show()


