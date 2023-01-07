// 사분면에서 풍선을 놔두고 레이저를 쏠때 직선으로 나감
// 같은 직선에 있으면 한번에 터짐
//0,0에서 쏨
// 효율성에서 시간 초과

function solution(balloons) {
    var answer = balloons.length;
    let check_i = []
    let check_j = []
    for (let i = 0 ; i <balloons.length; i++) {
        check_i.push(0)
        check_j.push(0)
    }
    for (let i = 0 ; i <balloons.length; i++) {
        if (check_i[i] == 0) {
            for (let j = i+1 ; j <balloons.length; j++) {
                if (check_j[j] == 0) {
                    if (balloons[i][1]/balloons[i][0] == balloons[j][1]/balloons[j][0]){
                        if ((balloons[i][0] >= 0 && balloons[i][1] >= 0) == true && (balloons[j][0] >= 0 && balloons[j][1] >= 0) == true){
                            answer -= 1
                            check_j[j] = 1
                            check_i[j] = 1
                        }
                        if ((balloons[i][0] < 0 && balloons[i][1] >= 0) == true && (balloons[j][0] < 0 && balloons[j][1] >= 0) == true){
                            answer -= 1
                            check_j[j] = 1
                            check_i[j] = 1
                        }
                        if ((balloons[i][0] >= 0 && balloons[i][1] < 0) == true && (balloons[j][0] >= 0 && balloons[j][1] < 0)== true){
                            answer -= 1
                            check_j[j] = 1
                            check_i[j] = 1
                        }
                        if ((balloons[i][0] < 0 && balloons[i][1] < 0) == true && (balloons[j][0] < 0 && balloons[j][1] < 0) == true){
                            answer -= 1
                            check_j[j] = 1
                            check_i[j] = 1
                        }
                    }
                }
            }
        }
    }
    return answer;
}