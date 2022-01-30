# -*- coding: utf-8 -*-

import cv2
import numpy as np



class Image_Stitching():
    def __init__(self):
        self.ratioOfSafe = 0.85
        self.numberOfMinMatches = 10
        self.sift = cv2.SIFT_create()
        self.smoothing_window_size = 20000

    def registration(self, image1, image2):
        image1 = cv2.normalize(image1, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
        image2 = cv2.normalize(image2, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')

        kp1, des1 = self.sift.detectAndCompute(image1, None)
        kp2, des2 = self.sift.detectAndCompute(image2, None)
        matcher = cv2.BFMatcher()
        raw_matches = matcher.knnMatch(des1, des2, k=2)
        good_points = []
        good_matches = []

        for m1, m2 in raw_matches:
            if m1.distance < self.ratioOfSafe * m2.distance:
                good_points.append((m1.trainIdx, m1.queryIdx))
                good_matches.append([m1])
        cv2.drawMatchesKnn(image1, kp1, image2, kp2, good_matches, None, flags=2)

        if len(good_points) > self.numberOfMinMatches:
            image1_kp = np.float32(
                [kp1[i].pt for (_, i) in good_points])
            image2_kp = np.float32(
                [kp2[i].pt for (i, _) in good_points])
            H, masks = cv2.findHomography(image2_kp, image1_kp, cv2.RANSAC, 5.0)

        return H, masks

    def laplace(self, img1, img2):

        height_img1 = img1.shape[0]
        width_img1 = img1.shape[1]
        width_img2 = img2.shape[1]
        height_panorama = height_img1 + 200
        width_panorama = width_img1 + width_img2 + 200
        H, masks = self.registration(img1, img2)

        m = np.ones((img1.shape[0], img1.shape[1], 3), dtype='float32')

        panorama1 = np.zeros((height_panorama, width_panorama, 3))
        panorama1[0:img1.shape[0], 0:img1.shape[1], :] = img1

        panorama2 = cv2.warpPerspective(img2, H, (width_panorama, height_panorama))
        mask_left = cv2.warpPerspective(m, H, (width_panorama, height_panorama))

        mask_left[5:, 5:, :] = mask_left[:-5, :-5, :]

        lpb = self.Laplacian_blending(panorama2, panorama1, mask_left, 4)
        # For blur testing:
        # lpb = cv2.blur(lpb, (20, 20))
        return lpb

    def Laplacian_blending(self, img1, img2, mask, levels=20):

        G1 = img1.copy()
        G2 = img2.copy()
        GM = mask.copy()

        gp1 = [G1]
        gp2 = [G2]
        gpM = [GM]

        for i in range(levels):
            G1 = cv2.pyrDown(G1)
            G2 = cv2.pyrDown(G2)
            GM = cv2.pyrDown(GM)
            gp1.append(np.float64(G1))
            gp2.append(np.float64(G2))
            gpM.append(np.float64(GM))

        # generate Laplacian Pyramids for A,B and masks
        lp1 = [gp1[levels - 1]]
        lp2 = [gp2[levels - 1]]
        gpMr = [gpM[levels - 1]]

        for i in range(levels - 1, 0, -1):

            L1 = np.subtract(gp1[i - 1], cv2.pyrUp(gp1[i]))
            L2 = np.subtract(gp2[i - 1], cv2.pyrUp(gp2[i]))
            lp1.append(L1)
            lp2.append(L2)
            gpMr.append(gpM[i - 1])  # also reverse the masks


        LS = []
        for l1, l2, gm in zip(lp1, lp2, gpMr):
            ls = l1 * gm + l2 * (1.0 - gm)
            LS.append(ls)


        ls_ = LS[0]
        for i in range(1, levels):
            ls_ = cv2.pyrUp(ls_)
            ls_ = cv2.add(ls_, LS[i])

        return ls_


