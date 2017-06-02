
function sortBy(field, reverse, primer) {
  const key = x => (primer ? primer(x[field]) : x[field]);
  return (a, b) => {
    const A = key(a);
    const B = key(b);
    let ret;
    if (A < B) {
      ret = -1;
    } else if (A > B) {
      ret = 1;
    } else {
      ret = 0;
    }
    return ret * [-1, 1][+!!reverse];
  };
}

module.exports = {
  sortBy,
};
