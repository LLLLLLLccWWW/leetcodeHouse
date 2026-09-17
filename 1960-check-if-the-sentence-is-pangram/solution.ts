function checkIfPangram(sentence: string): boolean {
    // 統計字串中不重複的字元個數是否為 26
    return new Set(sentence).size === 26
};
