#yTrue = [1,-2,3,3]
#yPred = [0,-3,2,1]

from sklearn.metrics import r2_score, mean_absolute_percentage_error

# print(mean_absolute_percentage_error(yTrue,yPred))
truePos = 80
falsePos = 40
trueNeg = 10
falseNeg = 20

#print(truePos/(truePos+falsePos))
#print(truePos/(truePos+falseNeg))
#print((truePos+trueNeg)/(trueNeg+truePos+falseNeg+falsePos))

yTrue = [1,0,0,1,1]
yPred = [0.5,0.6,0.2,0.1,0.7]

print(1/2*1/3+1/2*2/3)