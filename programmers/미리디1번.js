
// 숫자 입력시 자리수 다 더하고 1자리가 될때의 값




function solution(n) {
    var answer = 0;

    function hap(x){
        let num = 0
        x = x.toString()
        for (let i = 0 ; i <x.length; i++) {
            num += parseInt(x[i])
        }
        answer = num
        return answer
    }
    hap(n);
    while( answer >= 10){
        hap(answer)
    }
    return answer;
}

