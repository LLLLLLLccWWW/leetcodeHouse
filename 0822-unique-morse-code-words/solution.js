/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    const morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."
    ];

    const seen = new Set();

    for(const word of words){
        let code = '';
        for (var i = 0;i<word.length;i++){
            // 'a' 的 ASCII Code 是 97，減去 97 可得到 0 ~ 25 的索引
            const index = word.charCodeAt(i) - 97;
            code += morseCodes[index];
        }
        seen.add(code);
    }
    return seen.size;
};
