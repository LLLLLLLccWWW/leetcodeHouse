function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  const len = arr.length;
  const returnedArray = new Array<number>(len);

  for (let i = 0;i < len; i++){
    returnedArray[i] = fn(arr[i],i);
  }  

  return returnedArray;
};
