import cv2

def remove_blobs(file_path):
    img = cv2.imread(file_path)
    cv2.imshow('origin', img)

    #Converting mage to Gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", img)

    #Converting image to B&W
    ret, img = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
    cv2.imshow('b&w', img)

    #Find image contours
    contours, heirarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print('Len: ', len(contours))
    #Max Blog Size
    threshold_blob_area = 15

    #Iterate through all contours
    for i in range(1, len(contours)):
        index_level = int(heirarchy[0][i][1])
        if index_level <= i:
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            #print(area)
            if area < threshold_blob_area:
                #Drawa white color for blobs
                cv2.drawContours(img, [cnt], -1, 225, -1, 1)

    cv2.imwrite('result.jpg', img)