type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    return{
        toBe:(otherVal:unknown):boolean => {
            if(val !== otherVal){
                throw new Error("Not Equal");
            }
            return true;
        },
        notToBe:(otherVal:unknown):boolean => {
            if  (val === otherVal) {
                throw new Error("Equal");
            }
            return true;
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
