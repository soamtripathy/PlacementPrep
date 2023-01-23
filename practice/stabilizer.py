# Fitness is a big challenge for all the kids nowadays, Sp XYZ School has allotted N trays for N 0ids each kid will be allotted I tray No with N eggs Every rod is fanclOMly allotted Some number every day all kids who are getting the same number must form a group. All Tho t I group must consume eggs that are equal to group stEe for example if group sae a 3 then all the kids in that group must consume 3 ego=- tray Principal wanted a dashboard that displays The number of eggs left In each tray. Can you help wen a program that accepts the number number of trays al and the random number picked by each ktd and ennt the number of eggs left In each tray? Read the input from STDIN and print the output to STDOUT Do not write arbarary smogs anywhere r the program, as these contribute to. Standard output and testcases will fail
#Constraints Number or trays am
#Input Formal: Theist line & input must contain N. Me total number of trays The second line of Input costa. N random numbere that are selected ay ar ...Me Ea. numberire siTharateThY Thale wThe sPaThi
# 51.15511Forinal: The output contams a dashboard that displays the number of pope ten in each tray, separated by a single wade space 12522544
from collections import Counter
def stabilizer(arr, N):
    d = Counter(arr)
    l1 = []
    for i in arr:
        l1.append(N-d[i])
    return l1

print(stabilizer([15, 16, 22, 45, 75], 6))