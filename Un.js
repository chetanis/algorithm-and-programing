
//U(n) = 2U(n-1) + 3U(n-3) with n>2 , U0 = 0 ; U1 = 1 ; U2 = 2
function Un(n) {
    var x=0,y=1,z=2,un;
    switch (n) {
        case 0:
            return 0;
        case 1:
            return 1;
        case 2:
            return 2;
    }
    for (let i = 3; i <= n; i++) {
        un = 2*z + 3*x;
        x=y;y=z;z=un;
    }
    return un;
}
console.log(Un(5))