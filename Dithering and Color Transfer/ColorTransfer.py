
import numpy as np

def colorTransfer(source, target):
    sourceLMS = np.zeros_like(source)
    targetLMS = np.zeros_like(target)

    transformMatrix = np.array([[0.3811, 0.5783, 0.0402],
                                [0.1967, 0.7244, 0.0782],
                                [0.0241, 0.1288, 0.8444]])

    transformMatrix2 = np.array([[0.57735, 0, 0],
                                 [0, 0.4082483, 0],
                                 [0, 0, 0.7071068]])

    transformMatrix3 = np.array([[1, 1, 1],
                                 [1, 1, -2],
                                 [1, -1, 0]])

    sourceHeight, sourceWidth, dS = source.shape
    targetHeight, targetWidth, dT = target.shape

    for j in range(0, sourceWidth):
        for i in range(0, sourceHeight):
            sourceLMS[i][j] = np.matmul(transformMatrix, source[i][j])

    for j in range(0, targetWidth):
        for i in range(0, targetHeight):
            targetLMS[i][j] = np.matmul(transformMatrix, target[i][j])

    sourceLMS[sourceLMS == 0] = 1
    targetLMS[targetLMS == 0] = 1

    sourceLMS = np.log10(sourceLMS).astype('float32')
    targetLMS = np.log10(targetLMS).astype('float32')

    sourceABL = np.zeros_like(sourceLMS)
    targetABL = np.zeros_like(targetLMS)

    mult2and3 = np.matmul(transformMatrix2, transformMatrix3)

    for j in range(0, sourceWidth):
        for i in range(0, sourceHeight):
            sourceABL[i][j] = np.matmul(mult2and3, sourceLMS[i][j])
    for j in range(0, targetWidth):
        for i in range(0, targetHeight):
            targetABL[i][j] = np.matmul(mult2and3, targetLMS[i][j])


    meanASource = np.mean(sourceABL[:, :, 1])
    meanBSource = np.mean(sourceABL[:, :, 2])
    meanLSource = np.mean(sourceABL[:, :, 0])

    varASource = np.var(sourceABL[:, :, 1])
    varBSource = np.var(sourceABL[:, :, 2])
    varLSource = np.var(sourceABL[:, :, 0])

    meanATarget = np.mean(targetABL[:, :, 1])
    meanBTarget = np.mean(targetABL[:, :, 2])
    meanLTarget = np.mean(targetABL[:, :, 0])

    varATarget = np.var(targetABL[:, :, 1])
    varBTarget = np.var(targetABL[:, :, 2])
    varLTarget = np.var(targetABL[:, :, 0])

    newABLsource = np.zeros_like(sourceABL)
    newABLsource[:, :, 1] = np.subtract(sourceABL[:, :, 1], meanASource)
    newABLsource[:, :, 2] = np.subtract(sourceABL[:, :, 2], meanBSource)
    newABLsource[:, :, 0] = np.subtract(sourceABL[:, :, 0], meanLSource)

    dividedAndMultipliedABLsource = np.zeros_like(newABLsource)
    dividedAndMultipliedABLsource[:, :, 1] = np.multiply((varATarget / varASource), newABLsource[:, :, 1])
    dividedAndMultipliedABLsource[:, :, 2] = np.multiply((varBTarget / varBSource), newABLsource[:, :, 2])
    dividedAndMultipliedABLsource[:, :, 0] = np.multiply((varLTarget / varLSource), newABLsource[:, :, 0])

    primeABLsource = np.zeros_like(dividedAndMultipliedABLsource)
    primeABLsource[:, :, 1] = np.add(dividedAndMultipliedABLsource[:, :, 1], meanATarget)
    primeABLsource[:, :, 2] = np.add(dividedAndMultipliedABLsource[:, :, 2], meanBTarget)
    primeABLsource[:, :, 0] = np.add(dividedAndMultipliedABLsource[:, :, 0], meanLTarget)

    transformMatrix4 = np.array([[1, 1, 1], [1, 1, -1], [1, -2, 0]])

    transformMatrix5 = np.array([[4.4679, -3.5873, 0.1193], [-1.2186, 2.3889, -0.1624], [0.0497, -0.2439, 1.2045]])


    mult4and2 = np.matmul(transformMatrix4, transformMatrix2)

    for j in range(0, sourceWidth):
        for i in range(0, sourceHeight):
            sourceLMS[i][j] = np.matmul(mult4and2, primeABLsource[i][j])
    sourceLMS = 10 ** sourceLMS

    LMStoRGB = np.zeros_like(source)

    for j in range(0, sourceWidth):
        for i in range(0, sourceHeight):
            LMStoRGB[i][j] = np.matmul(transformMatrix5, sourceLMS[i][j]).clip(0,255)
    return LMStoRGB
