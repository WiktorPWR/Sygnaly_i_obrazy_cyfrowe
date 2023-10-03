import matplotlib.pyplot as plt
from matplotlib import transforms

img = plt.imread('C:\\Users\\student\\Desktop\\obraz1.jpg')

fig = plt.figure()
ax = fig.add_subplot(111)
rotation_in_degrees = 10
tr = transforms.Affine2D().rotate_deg(rotation_in_degrees)

ax.imshow(img, transform=tr + ax.transData)
plt.show()
