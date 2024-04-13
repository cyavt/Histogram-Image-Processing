import cv2
import matplotlib.pyplot as plt


def plot_histograms(image_path):

    image = cv2.imread("lenna.png")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Calculate histogram for the grayscale image
    gray_hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Calculate histograms for RGB channels
    color = ('r', 'g', 'b')
    plt.figure(figsize=(10, 5))

    # Plot grayscale histogram
    plt.subplot(2, 1, 1)
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.plot(gray_hist, color='gray')
    plt.xlim([0, 256])

    # Plot RGB histograms
    plt.subplot(2, 1, 2)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    for i, col in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.tight_layout()
    plt.show()


# Replace 'path_to_image.jpg' with the path to your image file
plot_histograms('path_to_image.jpg')