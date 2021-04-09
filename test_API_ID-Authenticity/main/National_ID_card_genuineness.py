import numpy as np
from numpy import *
from skimage.io import imread, imshow

# import cv2


# image1 = Image.open("nigerian-nin-card.jpg")
# print(image1.format)
# print(image1.mode)
# print(image1.size)
##image.show()
#
# nin_card = tf.io.read_file("nigerian-nin-card.jpg")
#
# nin_card = tf.io.decode_image(nin_card)

#
# plt.figure()
# plt.imshow(nin_card)


image1 = imread("ID card (original) 1.jpg")  # add as_gray = True to change to gray
# imshow(image1) #- You can always show this later


# print("Shape of image 1: ", image1.shape)
image1_shape = image1.shape  # To check the shape of the image

""" FEATURE EXTRACTION """
feature = np.reshape(image1, image1_shape)
# print(feature)
feature_matrix_image1 = np.zeros((image1_shape[0], image1_shape[1]))
# print(feature_matrix_image1)
# print(feature_matrix_image1.shape)


for i in range(0, image1.shape[0]):
    for j in range(0, image1.shape[1]):
        feature_matrix_image1[i][j] = (
            int(image1[i, j, 0]) + int(image1[i, j, 1]) + int(image1[i, j, 2])
        ) / 3

# print(" ")
# print("Feature matrix of image 1")
# print(feature_matrix_image1) #- You can uncomment this when needed
# print(feature_matrix_image1.shape) #- still retains the shape of the feature

"""sample of the feature """

feature_sample = np.reshape(feature_matrix_image1, (image1_shape[0] * image1_shape[1]))
# print("Feature sample:")
# print(" ")
# print(feature_sample)
# print(feature_sample.shape)

""" Comparing feature extraction in a test image """


def check_image_similarity(image_test):

    image1_test = imread(image_test)
    imshow(image1_test)  # I can always show this later
    print("Shape of ", str(image_test), " is:", image1_test.shape)
    image1_test_shape = image1_test.shape
    #    feature_image1_test = np.reshape(image1_test, image1_test_shape)

    # imshow(image1_test)
    feature_matrix_image1_test = np.zeros((image1_test_shape[0], image1_test_shape[1]))

    for p in range(0, image1_test.shape[0]):
        for q in range(0, image1_test.shape[1]):
            feature_matrix_image1_test[p][q] = (
                int(image1_test[p, q, 0])
                + int(image1_test[p, q, 1])
                + int(image1_test[p, q, 2])
            ) / 3

    # print(" ")
    # print("Feature matrix of test image 1")
    # print(feature_matrix_image1_test)   # You can always uncomment this

    shape = np.shape(feature_matrix_image1_test)
    padded_array = np.zeros((534, 801))
    padded_array[: shape[0], : shape[1]] = feature_matrix_image1_test

    feature_sample_image_test1 = np.reshape(
        padded_array, (image1_shape[0] * image1_shape[1])
    )

    # print(" ")
    # print("Feature sample of test image 1")
    # print(" ")
    # print(feature_sample_image_test1)
    # print(feature_sample_image_test1.shape)

    """ Checking for the similarity vector - Cosine similarity """  # Perhaps i should use/check for correlation between the two
    from sklearn.metrics.pairwise import cosine_similarity

    print(" ")
    print("Checking for the similarity vector - Cosine similarity: ")
    print(
        "Cosine similarity:",
        cosine_similarity([feature_sample], [feature_sample_image_test1]),
    )

    """ Therefore, the genuinity of the when compared to an original ID card is: """

    for similarity in cosine_similarity([feature_sample], [feature_sample_image_test1]):
        similarity = str(similarity).replace("[", "")
        similarity = str(similarity).replace("]", "")

        # if True:
        #     # image_test = str(image_test).replace(".jpg", "")
        #     print(
        #         "The",
        #         "card genuinity percentage is:",
        #         (float(similarity) * 100),
        #         "%",
        #     )

        # elif image_test.endswith(".jpeg"):
        #     image_test = str(image_test).replace(".jpeg", "")
        #     print(
        #         str(image_test),
        #         "'s",
        #         "card genuinity percentage is:",
        #         (float(similarity) * 100),
        #         "%",
        #     )
        # elif image_test.endswith(".png"):
        #     image_test = str(image_test).replace(".png", "")
        #     print(
        #         str(image_test),
        #         "'s",
        #         "card genuinity percentage is:",
        #         (float(similarity) * 100),
        #         "%",
        #     )

        if (float(similarity) * 100) < 75:
            print("This ID card is not GENUINE!")
            return "This ID card is not GENUINE!"
        else:
            print("This ID card is GENUINE")
            return "This ID card is GENUINE"


# request = input("Enter the name of the image file e.g 'victor.jpg' : ")
# check_image_similarity(request)
