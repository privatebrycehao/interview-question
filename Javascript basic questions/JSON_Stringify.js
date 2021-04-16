function stringify(value) {
        const lastKey = Object.keys(value).pop();
        let objString = '';
        if (typeof value === 'object' && !Array.isArray(value)) {
            objString += '{';
            for (const key in value) {
                objString += `"${key}":${stringify(value[key])}`;
                if (key !== lastKey) {
                    objString += ',';
                }
            }
            objString += '}';
        } else if (Array.isArray(value)) {
            objString += '['
            value.forEach((item, index) => {
                if (index !== value.length - 1) {
                    objString += `${stringify(item)},`
                } else {
                    objString += `${stringify(item)}`
                }
                
         })
            objString += ']'
            
        } else if (typeof value === 'string' || typeof value === 'number') {
            objString += `"${value}"`;
        }
        return objString;
}
