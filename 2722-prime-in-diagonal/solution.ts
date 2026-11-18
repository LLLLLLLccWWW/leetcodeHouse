function diagonalPrime(nums: number[][]): number {
    const isPrime = (x:number): boolean => {
        if (x < 2) return false;
        if (x === 2 || x === 3) return true;
        if (x % 2 === 0 || x % 3 === 0) return false;

        const limit = Math.floor(Math.sqrt(x));
        for (let d = 5; d <= limit; d += 6){
            if(x % d === 0 || x % (d + 2) === 0){
                return false;
            }
        }
        return true;
    };

    const n = nums.length;
    let ans = 0;

    for (let i = 0; i < n; i++){
        const d1 = nums[i][i];
        if(d1 > ans && isPrime(d1)){
            ans = d1;
        }
        const d2 = nums[i][n - 1 - i];
        if(d2 > ans && isPrime(d2)){
            ans = d2;
        }
    }
    return ans
};
