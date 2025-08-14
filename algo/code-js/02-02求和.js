// 求和 计算不大于n的项的总和
// 1 + 4 + 10 + ... 
// 后一项 = (前一项 + 1) * 2


function getSum(n) {
    let sum = 0
    let i = 1
    while (i <= n) {
        sum += i
        i ++
        i *= 2
    }
    return sum
}

// 调用函数
let n = 5
let result = getSum(n)
console.log(result) // 5