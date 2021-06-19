lr = 0.2
X = [[-1, -1, 1], [-1, 1, 1], [1, -1, 1],[1, 1, 1]] #input
Y = [-1, -1, -1, 1]  # Required Output


def NetValue(W):
    FinalW1, FinalW2, FinalBias = W
    Net = []
    for i in X:
        NetV = FinalW1 * i[0] + FinalW2 * i[1]
        Net.append(NetV)

    return Net


def ANDwithCorr_LR():
    weight1 = weight2 = b = 0
    WeightBiasMat = []
    count = 0
    while count < 4:
        for i in X:
            # print(i)
            temp = []
            weight1 += i[0]
            weight2 += i[0]
            b += 1
            if (weight1 and weight2) >= 0:
                weight1 *= i[0] * 1 * lr
                weight2 *= i[0] * 1 * lr
                b *= 1 * lr
            else:
                weight1 *= i[0] * -1 * lr
                weight2 *= i[0] * -1 * lr
                b *= -1 * lr

            temp.append(round(weight1, 3))
            temp.append(round(weight2, 3))
            temp.append(round(b, 3))

            WeightBiasMat.append(temp)
            count += 1

    print("Weight Matrix>>>", WeightBiasMat)
    print()

    ResultFromNet = NetValue(WeightBiasMat[-1])
    Prediction = []
    print("NetWeightMatrix", ResultFromNet)
    print()
    for i in ResultFromNet:
        if i > 0:
            Prediction.append(1)
        else:
            Prediction.append(-1)
    print("Required >>>{} \nPredicted From Correlation Learning Rule >>>{}".format(Y, Prediction))


ANDwithCorr_LR()
